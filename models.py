from django.db import models
from django.contrib.auth.models import User


class Currency(models.Model):
    currency_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=100)
    users = models.ManyToManyField(User)

# mapper:
    def populate_from_dict(self, dict):
        self.currency_id = dict['id']
        self.name = dict['name']
        self.symbol = dict['symbol']


class CurrencyHistory(models.Model):
    available_supply = models.FloatField()
    market_cap_eur = models.FloatField()
    market_cap_usd = models.FloatField()
    max_supply = models.FloatField()
    percent_change_1h = models.FloatField()
    percent_change_7d = models.FloatField()
    percent_change_24h = models.FloatField()
    price_btc = models.FloatField()
    price_eur = models.FloatField()
    price_usd = models.FloatField()
    rank = models.IntegerField()
    total_supply = models.FloatField()
    date = models.IntegerField(default=0)
    currency = models.ForeignKey("Currency", on_delete=models.CASCADE)

    def populate_from_dict(self, dict):
        self.available_supply = dict['available_supply'] if dict['available_supply'] is not None and dict['available_supply'] != "" else 0
        self.date = dict['last_updated'] if dict['last_updated'] is not None and dict['last_updated'] != "" else 0
        self.market_cap_eur = dict['market_cap_eur'] if dict['market_cap_eur'] is not None and dict['market_cap_eur'] != "" else 0
        self.market_cap_usd = dict['market_cap_usd'] if dict['market_cap_usd'] is not None and dict['market_cap_usd'] != "" else 0
        self.max_supply = dict['max_supply'] if dict['max_supply'] is not None and dict['max_supply'] != "" else 0
        self.percent_change_1h = dict['percent_change_1h'] if dict['percent_change_1h'] is not None and dict['percent_change_1h'] != "" else 0
        self.percent_change_7d = dict['percent_change_7d'] if dict['percent_change_7d'] is not None and dict['percent_change_7d'] != "" else 0
        self.percent_change_24h = dict['percent_change_24h'] if dict['percent_change_24h'] is not None and dict['percent_change_24h'] != "" else 0
        self.price_btc = dict['price_btc'] if dict['price_btc'] is not None and dict['price_btc'] != "" else 0
        self.price_eur = dict['price_eur'] if dict['price_eur'] is not None and dict['price_eur'] != "" else 0
        self.price_usd = dict['price_usd'] if dict['price_usd'] is not None and dict['price_usd'] != "" else 0
        self.rank = dict['rank']
        self.total_supply = dict['total_supply'] if dict['total_supply'] is not None and dict['total_supply'] != "" else 0

class MarketCap(models.Model):
    total_market_cap_usd = models.BigIntegerField()
    total_24h_volume_usd = models.BigIntegerField()
    bitcoin_percentage_of_market_cap = models.FloatField()
    active_currencies = models.IntegerField()
    active_assets = models.IntegerField()
    active_markets = models.IntegerField()
    last_updated = models.IntegerField()
    total_market_cap_eur = models.BigIntegerField()
    total_24h_volume_eur = models.BigIntegerField()

    def populate_from_dict(self, dict):
        self.total_market_cap_usd = dict['total_market_cap_usd']
        self.total_24h_volume_usd = dict['total_24h_volume_usd']
        self.bitcoin_percentage_of_market_cap = dict['bitcoin_percentage_of_market_cap']
        self.active_currencies = dict['active_currencies']
        self.active_assets = dict['active_assets']
        self.active_markets = dict['active_markets']
        self.last_updated = dict['last_updated']
        self.total_market_cap_eur = dict['total_market_cap_eur']
        self.total_24h_volume_eur = dict['total_24h_volume_eur']