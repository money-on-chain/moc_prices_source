from ....pairs.simple import USD_ARS
from ....base import EngineWebScraping, Engines, Decimal 
from ._parse import ars_quote



@Engines.register_decorator()
class Engine(EngineWebScraping):

    _description = "DolarHoy.com"
    _uri = "https://dolarhoy.com/cotizaciondolarblue"
    _coinpair = USD_ARS
    _max_age = 10800 # 3hs.
    _max_time_without_price_change = 0 # zero means infinity


    def _scraping(self, html):
        value = ars_quote(html, 'dólar libre')
        if not value:
            self._error = "Response format error"
            return None
        return {
            'price':  value
        }
