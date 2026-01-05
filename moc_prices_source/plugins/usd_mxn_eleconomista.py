from .pairs import USD_MXN
from .base import EngineWebScraping, engine_register, Decimal



@engine_register()
class Engine(EngineWebScraping):

    _name        = EngineWebScraping._name_from_file(__file__)
    _description = "ElEconomista.es"
    _uri         = "https://www.eleconomista.es/cruce/USDMXN"
    _coinpair    = USD_MXN

    _max_age                       = 3600 # 1hs.
    _max_time_without_price_change = 0    # zero means infinity

    _headers = {'User-agent': 'Mozilla/5.0'} # FIX: 403 Client Error Forbidden

    def _scraping(self, html):
        value = None
        for s in html.find_all('span', class_="ultimo_21334 last-value" ):
            d = s.string.strip().split()
            if len(d)==2 and d[1]=="/$":
                try:
                    value = Decimal(d[0].replace(',', '.'))
                except:
                    value = None
                if value:
                    break
        if not value:
            self._error = "Response format error"
            return None
        return {
            'price':  value
        }
