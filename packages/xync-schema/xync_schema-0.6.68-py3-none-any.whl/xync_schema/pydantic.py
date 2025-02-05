from datetime import datetime

from pydantic import BaseModel, model_validator

from xync_schema.enums import AdStatus, PmType
from xync_schema.models import Fiat, Agent, Direction, Pm, Pmcur, User


class PmexBankPyd(BaseModel):
    id: int | None = None
    exid: str
    name: str


class PmPyd(BaseModel):
    id: int | None = None
    name: str
    identifier: str | None = None
    type_: PmType | None = None
    logo: str | None = None
    banks: list[PmexBankPyd] | None = None


# class PmcurPyd(BaseModel):
#     id: int | None = None
#     pm_id: int
#     cur_id: int


class FiatUpd(BaseModel):
    detail: str | None = None
    name: str | None = None
    amount: float | None = None
    target: int | None = None


class FiatNew(FiatUpd):
    cur_id: int
    pm_id: int
    detail: str
    amount: float = 0
    target: int | None = None


class FiatPydIn(BaseModel):
    # unq
    id: int = None
    user_id: int | None = None
    user: User | None = None
    pmcur_id: int | None = None
    pmcur: Pmcur | None = None
    # df
    detail: str
    name: str = ""
    amount: float
    target: float | None = None

    banks: list[str] = []

    class Config:
        arbitrary_types_allowed = True

    @classmethod
    @model_validator(mode="before")
    def check_at_least_one_field(cls, values):
        if (values.get("pmcur") or values.get("pmcur_id")) and (values.get("user") or values.get("user_id")):
            return values
        raise ValueError("pmcur_id or pmcur is required")

    def args(self) -> tuple[dict, dict]:
        unq: tuple[str, ...] = "id", "user_id", "user", "pmcur_id", "pmcur"
        df: tuple[str, ...] = "detail", "name", "amount", "target"
        d = self.model_dump()
        return {k: getattr(self, k) for k in df if d.get(k)}, {k: getattr(self, k) for k in unq if d.get(k)}


# class FiatexPyd(BaseModel):
#     id: int | None = None
#     exid: str
#     ex_id: int
#     fiat_id: int


class AdPydIn(BaseModel):
    # unq
    id: int
    # df
    price: float
    min_fiat: float
    max_fiat: float | None = None
    detail: str | None = None
    auto_msg: str | None = None
    status: AdStatus = AdStatus.active
    agent_id: int | None = None
    direction_id: int | None = None
    agent: Agent | None = None
    direction: Direction | None = None
    payMeths: list[Pm]

    class Config:
        arbitrary_types_allowed = True

    @classmethod
    @model_validator(mode="before")
    def check_at_least_one_field(cls, values):
        if (values.get("agent") or values.get("agent_id")) and (values.get("direction") or values.get("direction_id")):
            return values
        raise ValueError("pmcur_id or pmcur is required")


class OrderPyd(BaseModel):
    id: int
    amount: float
    status: str
    actions: dict | None = {}
    fiat: Fiat.pyd()
    is_sell: bool
    contragent: int | None = None
    created_at: datetime
    payed_at: datetime | None = None
    appealed_at: datetime | None = None
    confirmed_at: datetime | None = None
    msgs: int = 0
    topic: int


class UreadMsgs(BaseModel):
    order_id: int
    unread_cnt: int
