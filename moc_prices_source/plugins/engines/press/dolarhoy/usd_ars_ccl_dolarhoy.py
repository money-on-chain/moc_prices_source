from ....pairs.simple import USD_ARS_CCL
from ....base import EngineWebScraping, Engines, Decimal
from ._parse import ars_quote



@Engines.register_decorator()
class Engine(EngineWebScraping):

    _description = "DolarHoy.com"
    _uri = "https://dolarhoy.com/cotizaciondolarcontadoconliqui"
    _coinpair = USD_ARS_CCL
    _max_age = 10800 # 3hs.
    _max_time_without_price_change = 0 # zero means infinity

    def _scraping(self, html):
        value = ars_quote(html, 'contado con liqui')
        if not value:
            self._error = "Response format error"
            return None
        return {
            'price':  value
        }
