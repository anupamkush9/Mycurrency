from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from exchange_currency.currencybeacon import convert_currency
from .error_logger import log_error
from .serializer import CurrencyConversionSerializer, CurrencyExchangeRateSerializer, CurrencyFilterSerializer
from .models import CurrencyExchangeRate
from django.utils.dateparse import parse_date
from rest_framework import viewsets
from rest_framework.exceptions import ParseError

class ConvertCurrencyView(APIView):
    """
    A view to convert currency from source to exchanged currency.
    """

    def post(self, request):
        try:
            serializer = CurrencyConversionSerializer(data=request.data)
            if serializer.is_valid():
                source_currency = serializer.validated_data['source_currency']
                exchanged_currency = serializer.validated_data['exchanged_currency']
                amount = serializer.validated_data['amount']
                convert_currency_resp = convert_currency(source_currency, exchanged_currency, amount)
                if convert_currency_resp:
                    converted_amount = convert_currency_resp['response']['value']
                    rate = float(converted_amount)/float(amount)
                else:
                    return Response({"message":"Currently service is down, Please try after sometime"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                CurrencyExchangeRate.objects.create( source_currency=source_currency, exchanged_currency=exchanged_currency, original_amount=amount,
                                                     converted_amount=converted_amount, rate_value=rate)
                return Response({ 'source_currency': source_currency, 'exchanged_currency': exchanged_currency,
                                  'original_amount': amount, 'converted_amount': converted_amount, 'rate': rate }, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ParseError as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            log_error(message="Error in ConvertCurrencyView ==>> post method", exception=e)
            return Response({"message":"something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CurrencyExchangeRateListView(APIView):
    """
    Retrieve a list of Currency Exchange Rates filtered by date range and currency.
    """

    def get(self, request):
        try:
            serializer = CurrencyFilterSerializer(data=request.query_params)
            if serializer.is_valid():
                source_currency = serializer.validated_data['currency']
                from_date = serializer.validated_data['from_date']
                to_date = serializer.validated_data['to_date']
                if from_date:
                    from_date = parse_date(str(from_date))
                if to_date:
                    to_date = parse_date(str(to_date))
                try:
                    exchange_rates = CurrencyExchangeRate.objects.filter(source_currency__iexact=source_currency, valuation_date__range=(from_date, to_date) )
                    serializer = CurrencyExchangeRateSerializer(exchange_rates, many=True)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                except Exception as e:
                        return Response({"message": "An error occurred while retrieving the data.", "error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ParseError as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            log_error(message="Error in CurrencyExchangeRateListView ==>> get method", exception=e)
            return Response({"message":"something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CurrencyExchangeRateViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing CurrencyExchangeRate records.
    """
    queryset = CurrencyExchangeRate.objects.all()
    serializer_class = CurrencyExchangeRateSerializer
