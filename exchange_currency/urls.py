from django.urls import path, include
from .views import ConvertCurrencyView, CurrencyExchangeRateListView, CurrencyExchangeRateViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'currency-exchange-rate', CurrencyExchangeRateViewSet, basename='currencyexchangerate')

urlpatterns = [
    path('api/v1/convert_currency/', ConvertCurrencyView.as_view(), name='convert_currency'),
    path('api/v1/currency-exchange-rate-list/', CurrencyExchangeRateListView.as_view(), name='currency_exchange_rate_list'),
    path('api/v1/', include(router.urls)),
]