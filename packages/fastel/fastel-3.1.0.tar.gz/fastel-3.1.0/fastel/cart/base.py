import abc
import copy
import json
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    MutableMapping,
    Optional,
    Tuple,
    Type,
    Union,
)

from bson import json_util
from bson.objectid import ObjectId
from pydantic import BaseModel, ValidationError

from .collections import get_collection
from .datastructures import BaseCartConfig, ItemConfig
from .exceptions import CartException
from .product_items import ProductItems


class BaseCart(
    metaclass=abc.ABCMeta,
):
    config_cls: ClassVar[Type[BaseCartConfig]]
    items: ProductItems
    coupon_code: Optional[str]
    _cache_cart: MutableMapping[str, Any]
    _subtotal: int
    _fee: int
    _discount: int

    _tax_ratio = 1.05

    # 結帳時訂單折扣後價格使用點數的比例
    _use_points_ratio = 1
    # 點數對金額的比例
    _points_ratio: int = 1
    # 金額對點數的比例
    _gift_points_ratio: int = 1

    INITIAL_CART = {
        "items": [],
        "extra_items": [],
        "discount_items": [],
        "total": 0,
        "subtotal": 0,
        "sales": 0,
        "tax": 0,
        "fee": 0,
        "discount": 0,
    }

    @property
    def subtotal(self) -> int:
        return self._subtotal

    @property
    def fee(self) -> int:
        return self._fee

    @property
    def discount(self) -> int:
        return self._discount

    @property
    def total(self) -> int:
        return self._subtotal + self._fee - self._discount

    @property
    def sales(self) -> int:
        sales_amount = sum(item.sales_amount for item in self.items)
        sales_fee = round(self._fee / self._tax_ratio, 7)
        sales_discount = round(self._discount / self._tax_ratio, 7)
        return round(sales_amount + sales_fee - sales_discount)

    @property
    def tax(self) -> int:
        return self.total - self.sales

    @property
    def no_shipping_cost_qty(self) -> int:
        result = 0
        for item in self.items:
            if item.product.no_shipping_cost:
                result += item.config.qty
        return result

    @property
    def no_global_free_shipping_total(self) -> int:
        result = 0
        for item in self.items:
            if item.product.no_global_free_shipping:
                result += item.amount
        return result

    @property
    def shipping_extra_price(self) -> int:
        result = 0
        for item in self.items:
            if item.product.shipping_extra_price:
                result += item.product.shipping_extra_price * item.config.qty
        return result

    def __getattr__(self, item: str) -> Any:
        if item in self.config_cls.__fields__:
            _model_field = self.config_cls.__fields__[item]
            return self._cache_cart.get(item, _model_field.default)
        return self.__dict__[item]

    def __setattr__(self, key: str, value: Any) -> None:
        if key in self.config_cls.__fields__:
            self._cache_cart[key] = value
        else:
            self.__dict__[key] = value

    def __init__(
        self,
        identity: str,
        coupon: Optional[str] = None,
        points: int = 0,
        gift_points: int = 0,
        use_full_points: bool = False,
        initial_raise: bool = True,
        initial_clear: bool = False,
        extra_cart_query: Dict[str, Any] = {},
    ):
        self.coupon_code = coupon
        self._cache_cart = self._load_cart(identity, extra_cart_query)
        self.points = points
        self.gift_points = gift_points
        self.use_full_points = use_full_points
        self._user = None
        self._user_profile = None

        if not identity.startswith("tmp_"):
            self._user = get_collection("user").find_one({"_id": ObjectId(identity)})
            self._user_profile = get_collection("user_profile").find_one(
                {"owner": identity}
            )

        try:
            self.items = self.product_multi_item_cls(
                products=[
                    {
                        "id": item["product"]["id"],
                        "config": item["config"],
                    }
                    for item in self._cache_cart["items"]
                ],
            )
        except Exception as exc:
            # we have to manually clear the cart in this case, otherwise the user won't be able to get_cart()
            if initial_clear:
                self.items = self.product_multi_item_cls(products=[])
                self.empty_cart()

            if initial_raise:
                raise CartException(exc)

        self.calc()

    def get_cart_ins(self) -> MutableMapping[str, Any]:
        cart_dict = copy.deepcopy(self._cache_cart)
        return cart_dict

    def to_dict(self) -> MutableMapping[str, Any]:
        cart_dict = copy.deepcopy(self._cache_cart)
        cart_dict = json.loads(json_util.dumps(cart_dict))
        return cart_dict

    def add_item(self, product_id: str, config: ItemConfig) -> MutableMapping[str, Any]:
        self.items.add_item(product_id, config)
        self.calc()
        self.save_cart()
        return self.to_dict()

    def delete_item(self, index: int) -> MutableMapping[str, Any]:
        self.items.delete_item(index)
        self.calc()
        self.save_cart()
        return self.to_dict()

    def edit_item(self, index: int, config: ItemConfig) -> MutableMapping[str, Any]:
        self.items.edit_item(index, config)
        self.calc()
        self.save_cart()
        return self.to_dict()

    def edit_config(
        self, config: Union[Dict[str, Any], BaseModel]
    ) -> MutableMapping[str, Any]:
        if not isinstance(config, BaseModel):
            try:
                config = self.config_cls.validate_optional(config)
            except ValidationError:
                raise CartException("validation_error")

        for key, value in config.dict(exclude_unset=True).items():
            setattr(self, key, value)

        self.calc()
        self.save_cart()
        return self.to_dict()

    def empty_cart(self) -> MutableMapping[str, Any]:
        self.items.clean_items()
        self.coupon_code = None
        self._total = 0
        self._sales = 0
        self._fee = 0
        self._tax = 0
        self.points = 0
        self.gift_points = 0
        self.order_note = ""
        self.use_full_points = False
        self.calc()
        self.save_cart()
        return self.to_dict()

    def save_cart(self) -> None:
        get_collection("cart").find_one_and_update(
            {"_id": self._cache_cart["_id"]}, {"$set": self._cache_cart}
        )

    def calc(self) -> None:
        subtotal = self.items.total
        product_items = self.items.to_dict()
        fee, fee_items = self._calc_fee()
        discount, discount_items = self._calc_discounts(
            subtotal=subtotal, coupon_code=self.coupon_code
        )

        (
            addon_discount,
            addon_discount_items,
            addon_fee,
            addon_fee_items,
        ) = self._calc_addon(
            subtotal=subtotal,
            product_items=product_items,
            fee=fee,
            fee_items=fee_items,
            discount=discount,
            discount_items=discount_items,
        )

        self._subtotal = subtotal
        self._fee = fee + addon_fee
        self._discount = discount + addon_discount

        self._cache_cart["subtotal"] = self.subtotal
        self._cache_cart["fee"] = self.fee
        self._cache_cart["discount"] = self.discount
        self._cache_cart["total"] = self.total
        self._cache_cart["sales"] = self.sales
        self._cache_cart["tax"] = self.tax
        self._cache_cart["items"] = product_items
        self._cache_cart["extra_items"] = fee_items + addon_fee_items
        self._cache_cart["discount_items"] = discount_items + addon_discount_items

    def _load_cart(
        self,
        identity: str,
        extra_cart_query: Dict[str, Any] = {},
    ) -> MutableMapping[str, Any]:
        cart = get_collection("cart").find_one(
            {"owner": str(identity), **extra_cart_query}
        )
        if not cart:
            cart = {
                **extra_cart_query,
                **self.INITIAL_CART,
                **self.config_cls.validate_optional(self._init_cart_extra()).dict(),
                "owner": str(identity),
            }
            cart_result = get_collection("cart").insert_one(cart)
            cart["_id"] = cart_result.inserted_id
        return cart  # type: ignore

    @abc.abstractmethod
    def _init_cart_extra(self) -> Dict[str, Any]:
        raise NotImplementedError("_init_cart_extra")

    @abc.abstractmethod
    def _calc_fee(self) -> Tuple[int, List[Dict[str, Any]]]:
        raise NotImplementedError("_calc_fee")

    @abc.abstractmethod
    def _calc_discounts(
        self, subtotal: int, coupon_code: Optional[str] = None
    ) -> Tuple[int, List[Dict[str, Any]]]:
        raise NotImplementedError("_calc_discounts")
