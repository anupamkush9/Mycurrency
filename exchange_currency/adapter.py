
from abc import ABC, abstractmethod

#  Target Interface
class CurrencyProviderAdapter(ABC):
    """Abstract base class (adapter) for currency exchange providers."""

    @abstractmethod
    def get_exchange_rate(self, source_currency, target_currency, valuation_date):
        pass

# Adaptee 1 (CurrencyBeaconAPI)
class CurrencyBeaconAPI:
    """A mock class simulating CurrencyBeacon API."""
    
    def fetch_rate(self, base: str, target: str, date: str):
        print(f"CurrencyBeaconAPI fetching rate for {base} to {target} on {date}")
        return 1.12

# Adaptee 2 (MockCurrencyAPI)
class MockCurrencyAPI:
    """A mock class simulating another API with different method signature."""
    
    def get_rate(self, base_currency: str, target_currency: str, date: str):
        print(f"MockCurrencyAPI fetching rate for {base_currency} to {target_currency} on {date}")
        return 0.85

class CurrencyBeaconAdapter(CurrencyProviderAdapter):
    """Adapter for CurrencyBeaconAPI."""
    
    def __init__(self, api: CurrencyBeaconAPI):
        self.api = api
    
    def get_exchange_rate(self, source_currency, target_currency, valuation_date) :
        return self.api.fetch_rate(source_currency, target_currency, valuation_date)

class MockCurrencyAdapter(CurrencyProviderAdapter):
    """Adapter for MockCurrencyAPI."""
    
    def __init__(self, api: MockCurrencyAPI):
        self.api = api
    
    def get_exchange_rate(self, source_currency, target_currency, valuation_date):
        return self.api.get_rate(source_currency, target_currency, valuation_date)

def get_exchange_rate_data(source_currency, exchanged_currency, valuation_date, provider):
    """Retrieve exchange rate data using the appropriate adapter based on the provider."""
    
    if provider == "currency_beacon":
        api = CurrencyBeaconAPI()
        adapter = CurrencyBeaconAdapter(api)
    elif provider == "mock_currency":
        api = MockCurrencyAPI()
        adapter = MockCurrencyAdapter(api)
    else:
        raise ValueError(f"Unsupported provider: {provider}")    
    return adapter.get_exchange_rate(source_currency, exchanged_currency, valuation_date)

if __name__ == "__main__":
    source_currency = "USD"
    exchanged_currency = "EUR"
    valuation_date = "2023-10-10"
    
    rate_currency_beacon = get_exchange_rate_data(source_currency, exchanged_currency, valuation_date, "currency_beacon")
    print(f"CurrencyBeacon rate: {rate_currency_beacon}")
    
    rate_mock_currency = get_exchange_rate_data(source_currency, exchanged_currency, valuation_date, "mock_currency")
    print(f"MockCurrency rate: {rate_mock_currency}")
