from ....pairs.simple import USD_ARS
from ....base import EngineWebScraping, Engines, Decimal
from decimal import InvalidOperation



to_dec = lambda x: Decimal(str(x).replace('.', '').replace(',', '.'))

@Engines.register_decorator()
class Engine(EngineWebScraping):

    _description = "InfoDolar.com"
    _uri = "https://www.infodolar.com/cotizacion-dolar-blue.aspx"
    _coinpair = USD_ARS
    _max_age = 3600 # 1hs.
    _max_time_without_price_change = 0 # zero means infinity


    def _scraping(self, html):
        value = None
        table = html.find('table', id="CompraVenta")
        if table:
            for row in table.find_all('tr'):
                name = row.find('td', class_='colNombre')
                if name is None or name.get_text(' ', strip=True) != 'Dólar Blue':
                    continue
                cells = row.find_all('td', class_='colCompraVenta')
                if len(cells) != 2:
                    break
                try:
                    prices = [to_dec(next(cell.stripped_strings).replace('$', '').strip())
                              for cell in cells]
                    value = (prices[0] + prices[1]) / Decimal(2)
                except (InvalidOperation, StopIteration):
                    pass
                break

        if not value:
            self._error = "Response format error"
            return None
        return {
            'price':  value
        }
