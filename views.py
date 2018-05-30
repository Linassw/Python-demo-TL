import json
import urllib.request
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth.models import User
from django.http import JsonResponse
from currencies.models import Currency
from currencies.models import CurrencyHistory
from currencies.models import MarketCap
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers


class DesktopView(generic.TemplateView):
    template_name = 'desktop.html'

    def get(self, request):

        # TODO: remove hardcoding
        data_json = urllib.request.urlopen("...url here...").read()
        data = json.loads(data_json)
        total_cap = self.lt_locale(str(int(data['total_market_cap_eur'])))

        cap_history = MarketCap.objects.order_by('-last_updated')[:12]
        return render(request, self.template_name, {'user_id': request.user.id, 'total_cap': total_cap, 'cap_history': cap_history})

	#quick and dirty	
    def lt_locale(self, string):

        if len(string) > 4:
            cursor = len(string)
            while cursor > 0:
                cursor = cursor - 3
                string = string[:cursor] + " " + string[cursor:]
        return string.replace('.', ',')




class SaveView(generic.View):

    def post(self, request):
        user = request.user
        currency_ids = json.loads(request.POST.get('currency_ids'))

        # 1. delete everything from Desktop where user_id = user_id
        try:
            user = User.objects.get(id=user.id)
            user.currency_set.clear()
            user.save()
        except User.DoesNotExist:
            pass
            # bad

        for currency in currency_ids:
            try:
                cur = Currency.objects.filter(currency_id=currency['currency_id'])[:1]
                cur[0].users.add(user)
                cur[0].save()
            except Currency.DoesNotExist:
                pass

        return HttpResponse('OK', content_type="application/json")

class LoadSidebar(generic.View):

    def get(self, request):

        db_currencies = Currency.objects.all()
        currencies = []

        for db_currency in db_currencies:
            histories = []
            cur_histories = CurrencyHistory.objects.filter(currency=db_currency).order_by('-date')
            currency = {'currency_id': db_currency.currency_id, 'name': db_currency.name, 'symbol': db_currency.symbol}
            for cur_history in cur_histories:
                history = {}
                history['available_supply'] = cur_history.available_supply
                history['last_updated'] = cur_history.date
                history['market_cap_eur'] = cur_history.market_cap_eur
                history['market_cap_usd'] = cur_history.market_cap_usd
                history['max_supply'] = cur_history.max_supply
                history['percent_change_1h'] = cur_history.percent_change_1h
                history['percent_change_7d'] = cur_history.percent_change_7d
                history['percent_change_24h'] = cur_history.percent_change_24h
                history['price_btc'] = cur_history.price_btc
                history['price_eur'] = cur_history.price_eur
                history['rank'] = cur_history.rank
                history['total_supply'] = cur_history.total_supply
                histories.append(history)
            currency['history'] = histories;
            currencies.append(currency)

        return JsonResponse(currencies, safe=False)

class UpdateCurrencies(generic.View):
    def get(self, request):
        #TODO: remove hardcoding
        data = urllib.request.urlopen("url...").read()
        data = json.loads(data)

        for currency in data:
            try:
                cur = Currency.objects.get(currency_id=currency['id'])
            except Currency.DoesNotExist:
                cur = Currency()
                cur.populate_from_dict(currency)
                cur.save()

            history = CurrencyHistory()
            history.populate_from_dict(currency)
            history.currency = cur
            history.save()

        return HttpResponse(data, content_type="application/json")


class UpdateGlobal(generic.View):
    def get(self, request):
        #TODO: remove URL hardcoding
        data = urllib.request.urlopen("url...").read()

        market_cap = MarketCap()
        market_cap.populate_from_dict(json.loads(data))
        market_cap.save()
        return HttpResponse(data, content_type="application/json")
