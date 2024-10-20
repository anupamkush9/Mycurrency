# exchange_currency/models.py
from django.db import models
from datetime import date

class CurrencyExchangeRate(models.Model):
    source_currency = models.CharField(max_length=3)
    exchanged_currency = models.CharField(max_length=3)
    valuation_date = models.DateField(default=date.today)
    original_amount = models.DecimalField(max_digits=18, decimal_places=6, db_index=True)
    converted_amount = models.DecimalField(max_digits=18, decimal_places=6, db_index=True)
    rate_value = models.DecimalField(max_digits=18, decimal_places=6, db_index=True)

    def __str__(self):
        return f"{self.source_currency}_{self.exchanged_currency}"
