from django.contrib import admin
from .models import CurrencyExchangeRate

@admin.register(CurrencyExchangeRate)
class CurrencyExchangeRateAdmin(admin.ModelAdmin):
    list_display = ['source_currency', 'exchanged_currency', 'valuation_date', 'original_amount', 'converted_amount', 'rate_value']

    class Media:
        js = (
            'https://code.jquery.com/jquery-3.6.1.min.js',
        )
