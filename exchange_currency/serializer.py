from rest_framework import serializers
from .models import CurrencyExchangeRate
from datetime import datetime

class CurrencyExchangeRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyExchangeRate
        fields = '__all__'

class CurrencyFilterSerializer(serializers.Serializer):
    currency = serializers.CharField(max_length=3, required=True)
    from_date = serializers.DateField(required=True)
    to_date = serializers.DateField(required=True)

    def validate_currency(self, value):
        """
        Validate that the currency code is a valid 3-letter code.
        """
        if len(value) != 3 or not value.isalpha():
            raise serializers.ValidationError("Currency must be a valid 3-letter code.")
        return value.upper()

    def validate(self, data):
        """
        Check that from_date is before to_date.
        """
        from_date = data.get('from_date')
        to_date = data.get('to_date')

        if from_date > to_date:
            raise serializers.ValidationError("from_date must be earlier than to_date.")
        return data

class CurrencyConversionSerializer(serializers.Serializer):
    source_currency = serializers.CharField(max_length=3)
    exchanged_currency = serializers.CharField(max_length=3)
    amount = serializers.DecimalField(max_digits=12, decimal_places=2)

    def validate_source_currency(self, value):
        """
        Custom validation to ensure the source currency is a valid 3-letter currency code.
        """
        if len(value) != 3 or not value.isalpha():
            raise serializers.ValidationError("Source currency must be a valid 3-letter currency code.")
        return value.upper()

    def validate_exchanged_currency(self, value):
        """
        Custom validation to ensure the exchanged currency is a valid 3-letter currency code.
        """
        if len(value) != 3 or not value.isalpha():
            raise serializers.ValidationError("Exchanged currency must be a valid 3-letter currency code.")
        return value.upper()

    def validate_amount(self, value):
        """
        Validate that the amount is positive.
        """
        if value <= 0:
            raise serializers.ValidationError("Amount must be a positive number.")
        return value

