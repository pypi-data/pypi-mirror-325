from asyncio import run

from x_model import init_db
from xync_schema.pydantic import AdPydIn, PmPyd, PmexBankPyd, CurEpyd

from xync_schema import models
from xync_schema.models import Ex, Agent, Direction, Pair, Coin, Cur, Pm, Fiatex, Pmex

from xync_client.TgWallet.pyd import AllAdFullEpyd, AdEpyd, PmEpydRoot, MyAdEpyd
from xync_client.loader import PG_DSN
from xync_client.Abc.Ex import BaseExClient
from xync_client.Abc.Base import FlatDict, MapOfIdsList
from xync_client.TgWallet.auth import AuthClient


class ExClient(BaseExClient, AuthClient):
    def __init__(self, ex: Ex, agent: Agent = None):
        if not agent:
            # ex should be with fetched .agents
            agent = [ag for ag in ex.agents if ag.auth][0]
        self.agent: Agent = agent  # need for AuthTrait
        super().__init__(ex)  # , "host_p2p"

    def pm_type_map(self, pm: Pm) -> str:
        return "V2" if pm.name.startswith("SBP") else "V1"

    # 00: todo: min-max for cur and coin ad amount, order, fee ..
    async def _settings(self) -> dict:
        settings = await self._post("/p2p/public-api/v2/offer/settings/get")
        return settings["data"]

    async def coin_mins(self) -> FlatDict:
        stg = await self._settings()
        lims = list(stg["offerSettings"]["offerVolumeLimitsPerMarket"].values())
        coins = {k: max(float(v[k]["minInclusive"]) for v in lims) for k, v in lims[0].items()}
        return coins

    # 19: Список поддерживаемых валют тейкера
    async def curs(self) -> list[CurEpyd]:
        coins_curs = await self._post("/p2p/public-api/v2/currency/all-supported")
        stg = await self._settings()
        roundings: dict[str, int] = stg["offerSettings"]["roundingScaleByFiatCurrency"]
        minimums: dict[str, str] = stg["offerSettings"]["minOrderAmountByCurrencyCode"]
        return [
            CurEpyd(
                exid=c["code"], ticker=c["code"], rounding_scale=roundings.get(c["code"]), minimum=minimums[c["code"]]
            )
            for c in coins_curs["data"]["fiat"]
        ]

    async def _pms(self, cur: str) -> dict[str, PmEpydRoot]:
        pms = await self._post("/p2p/public-api/v3/payment-details/get-methods/by-currency-code", {"currencyCode": cur})
        return {pm["code"]: PmEpydRoot(**pm) for pm in pms["data"]}

    # 20: Список платежных методов. todo: refact to pmexs?
    async def pms(self, cur: str = None) -> dict[str, PmPyd]:
        pms: dict[str:PmEpydRoot] = {}
        if cur:
            pms = await self._pms(cur)
        else:
            for cur in await self.curs():
                pms |= await self._pms(cur.exid)
        return {
            k: PmPyd(name=pm.nameEng, banks=[PmexBankPyd(exid=b.code, name=b.name) for b in pm.banks or []])
            for k, pm in pms.items()
        }

    # 21: Список платежных методов по каждой валюте
    async def cur_pms_map(self) -> MapOfIdsList:
        return {cur.exid: list(await self._pms(cur.exid)) for cur in await self.curs()}

    # 22: Список торгуемых монет (с ограничениям по валютам, если есть)
    async def coins(self) -> FlatDict:
        coins_curs = await self._post("/p2p/public-api/v2/currency/all-supported")
        return {c["code"]: c["code"] for c in coins_curs["data"]["crypto"]}

    # 23: Список пар валюта/монет
    async def pairs(self) -> MapOfIdsList:
        coins = await self.coins()
        curs = await self.curs()
        pairs = {cur.exid: set(coins.values()) for cur in curs}
        return pairs

    # 42: Объява по id
    async def ad(self, ad_id: int) -> AllAdFullEpyd:
        ad = await self._post("/p2p/public-api/v2/offer/get", {"offerId": ad_id})
        return AllAdFullEpyd(**ad["data"])

    # 24: Список объяв по (buy/sell, cur, coin, pm)
    async def ads(
        self, coin_exid: str, cur_exid: str, is_sell: bool, pm_exids: list[str | int] = None, amount: int = None
    ) -> list[AdEpyd]:
        params = {
            "baseCurrencyCode": coin_exid,
            "quoteCurrencyCode": cur_exid,
            "offerType": "SALE" if is_sell else "PURCHASE",
            "offset": 0,
            "limit": 100,
            # "merchantVerified": "TRUSTED"
        }
        ads = await self._post("/p2p/public-api/v2/offer/depth-of-market/", params, "data")
        return [AdEpyd(**ad) for ad in ads]

    async def ad_epyd2pydin(self, ad: MyAdEpyd | AdEpyd) -> AdPydIn:
        coin = await Coin.get_or_create_by_name(ad.price.baseCurrencyCode)
        cur = await Cur.get_or_create_by_name(ad.price.quoteCurrencyCode)
        pair, _ = await Pair.get_or_create(coin=coin, cur=cur, ex=self.ex)
        dr, _ = await Direction.get_or_create(pair=pair, sell=ad.is_sell)
        maker = self.agent.exid if isinstance(ad, MyAdEpyd) else await Agent.get(exid=ad.user.userId, ex=self.ex)

        adx = AdPydIn(
            id=ad.id,
            price=ad.price.value,
            min_fiat=ad.orderAmountLimits.min,
            max_fiat=ad.orderAmountLimits.max,
            direction=dr,
            agent=maker,
            detail=getattr(ad, "comment", None),
            # todo: maybe later adpm_banks
        )
        if ad.is_sell:
            adx.fiats_ = (await Fiatex.filter(pmexs__ex=self.ex, pmexs__exid__in=[p.code for p in ad.paymentMethods]),)
        else:
            adx.pms_ = (await Pmex.filter(pmexs__ex=self.ex, pmexs__exid__in=[p.code for p in ad.paymentMethods]),)

        return adx


async def _test():
    await init_db(PG_DSN, models, True)
    tgex = await Ex.get(name="TgWallet").prefetch_related("agents", "agents__ex")
    cl: ExClient = tgex.client()
    await cl.pms("RUB")
    await cl.set_pmcurexs()
    await cl.set_coinexs()
    ads: list[AdEpyd] = await cl.ads("USDT", "RUB", False)
    ad: AllAdFullEpyd = await cl.ad(ads[0].id)
    ad_pydin: AdPydIn = await cl.ad_epyd2pydin(ad)
    await cl.ad_pydin2db(ad_pydin)
    ads: list[AdEpyd] = await cl.ads("USDT", "RUB", True)
    ad: AdEpyd = ads[1]
    ad_pydin: AdPydIn = await cl.ad_epyd2pydin(ad)
    await cl.ad_pydin2db(ad_pydin)
    await cl.close()


if __name__ == "__main__":
    run(_test())
