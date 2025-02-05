from typing import List, Literal, Optional

from pydantic import BaseModel


class B2CItem(BaseModel):
    ItemSeq: Optional[int]
    ItemName: str
    ItemCount: int
    ItemWord: str
    ItemPrice: int
    ItemTaxType: Optional[Literal["1", "2", "3"]]
    ItemAmount: int
    ItemRemark: Optional[str]


class IssueB2CModel(BaseModel):
    RelateNumber: str
    CustomerID: Optional[str]
    CustomerIdentifier: Optional[str]
    CustomerName: Optional[str]
    CustomerAddr: Optional[str]
    CustomerPhone: Optional[str]
    CustomerEmail: Optional[str]
    ClearanceMark: Optional[str]
    Print: Literal["0", "1"] = "0"
    Donation: Literal["0", "1"] = "0"
    LoveCode: Optional[str]
    CarrierType: Optional[Literal["1", "2", "3", ""]]
    CarrierNum: Optional[str]
    TaxType: Literal["1", "2", "3", "4", "9"] = "1"
    SpecialTaxType: Optional[Literal["1", "2", "3", "4", "5", "6", "7", "8"]]
    SalesAmount: int
    InvoiceRemark: Optional[str]
    Items: List[B2CItem]
    InvType: Literal["07", "08"]
    vat: Optional[Literal["0", "1"]]


class QueryB2CModel(BaseModel):
    RelateNumber: Optional[str]
    InvoiceNo: Optional[str]
    InvoiceDate: Optional[str]


class VoidB2CModel(BaseModel):
    InvoiceNo: str
    InvoiceDate: str
    Reason: str
