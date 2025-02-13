from typing import Literal
from pydantic import BaseModel, model_validator, computed_field
from xync_schema.pydantic import BaseAd


class UserStatistics(BaseModel):
    userId: int
    totalOrdersCount: int
    successRate: str
    successPercent: int


class User(BaseModel):
    userId: int
    nickname: str
    avatarCode: str
    statistics: UserStatistics
    isVerified: bool
    lastOnlineMinutesAgo: int | None = None
    onlineStatus: str


class AvailableVolume(BaseModel):
    currencyCode: str  # coin
    amount: str  # of asset


class Price(BaseModel):
    type: Literal["FLOATING", "FIXED"]
    baseCurrencyCode: str
    quoteCurrencyCode: str
    value: str
    estimated: str | None = None


class OrderLimits(BaseModel):
    currencyCode: str | None = None
    min: str  # In
    max: str | None = None
    approximate: bool | None = None


class ChangeLogItem(BaseModel):
    status: Literal["ACTIVE", "INACTIVE", "ACTIVATING", "DEACTIVATING"]
    createDateTime: str
    initiatorUserId: int


class ChangeLog(BaseModel):
    items: list[ChangeLogItem]


class TakerFilter(BaseModel):
    accountAge: str
    completedOrders: str
    userRating: str


class FeeAvailableVolume(BaseModel):
    currencyCode: str  # coin
    amount: str  # of asset


class Fee(BaseModel):
    rate: str
    availableVolume: FeeAvailableVolume  # of asset


class KeyVal(BaseModel):
    name: Literal["PAYMENT_DETAILS_NUMBER", "PHONE"] = "PAYMENT_DETAILS_NUMBER"
    value: str


class BanksIn(BaseModel):
    name: Literal["BANKS"] = "BANKS"
    value: list[str]


class Bank(BaseModel):
    code: str
    nameRu: str
    nameEn: str


class Banks(BanksIn):
    value: list[Bank]


class Attrs(BaseModel):
    version: Literal["V1"] = "V1"
    values: list[KeyVal]


class AttrsV2In(BaseModel):
    version: Literal["V2"]
    values: list[KeyVal | BanksIn]


class AttrsV2(AttrsV2In):
    values: list[KeyVal | Banks]


class PmEpyd(BaseModel):
    code: str
    name: str
    originNameLocale: str
    nameEng: str


class PmEpydRoot(PmEpyd):
    banks: list[PmEpyd] | None = None


class FiatEpydIn(BaseModel):
    paymentMethodCode: str
    currencyCode: str
    name: str
    attributes: Attrs | AttrsV2In


class FiatEpyd(BaseModel):
    id: int
    userId: int
    paymentMethod: PmEpydRoot
    currency: str
    name: str = ""
    attributes: Attrs | AttrsV2


class InitVolume(BaseModel):
    currencyCode: str  # coin
    amount: str  # of asset


class _BaseCommonAd(BaseAd):
    type: Literal["PURCHASE", "SALE"]
    price: Price
    orderAmountLimits: OrderLimits  # cur/fiat

    @computed_field
    @property
    def is_sell(self) -> bool:
        return self.type == "SALE"


class AdEpyd(_BaseCommonAd):
    number: str
    user: User
    availableVolume: str  # of asset  # PURCHASE
    orderVolumeLimits: OrderLimits  # of asset
    takerFilter: TakerFilter
    paymentMethods: list[PmEpydRoot]  # PURCHASE


# class AdFullEpyd(AdEpyd):
#     availableVolume: AvailableVolume  # of asset # SALE
#
#     paymentConfirmTimeout: Literal["PT15M", "PT30M"]
#     price: Price
#     status: Literal["ACTIVE", "INACTIVE", "ACTIVATING"]
#     createDateTime: str
#     comment: str
#     orderConfirmationTimeout: Literal["PT3M", "PT15M"]
#     orderAcceptTimeout: Literal["PT10M"]


class MyAdEpydIn(_BaseCommonAd):
    orderConfirmationTimeout: Literal["PT3M", "PT15M"] | None = None  # purchase?
    paymentConfirmTimeout: Literal["PT3M", "PT15M"] | None = None  # sale?
    comment: str = ""
    initVolume: InitVolume  # of asset
    orderRoundingRequired: bool
    paymentMethodCodes: list[str] | None = None  # purchase
    paymentDetailsIds: list[int] | None = None  # sale

    @classmethod
    @model_validator(mode="before")
    def check_at_least_one_field(cls, values):
        if values.get("paymentMethodCodes") or values.get("paymentDetailsIds"):
            return values
        raise ValueError("paymentMethodCodes or paymentDetailsIds is required")


class MyAdEpyd(_BaseCommonAd):
    number: str
    availableVolume: AvailableVolume  # of asset
    orderVolumeLimits: OrderLimits  # coin/asset
    status: Literal["ACTIVE", "INACTIVE", "ACTIVATING", "DEACTIVATING"]
    paymentDetails: list[FiatEpyd] | None = None  # SALE
    paymentMethods: list[PmEpydRoot] | None = None  # PURCHASE

    @classmethod
    @model_validator(mode="before")
    def check_at_least_one_field(cls, values):
        if values.get("paymentMethods") or values.get("paymentDetails"):
            return values
        raise ValueError("paymentMethods or paymentDetails is required")


class AllAdFullEpyd(MyAdEpyd):
    createDateTime: str
    changeLog: ChangeLog
    orderConfirmationTimeout: str
    orderAcceptTimeout: str
    takerFilter: TakerFilter
    fee: Fee | None = None
