class CurrencyResponse(object):
    def __init__(self, data):
        self.currencySymbol = data['currencySymbol']
        self.currencyName = data['currencyName']
        self.bitsianCurrencyId = data['currencyId']


class ProductResponse(object):
    def __init__(self, data):
        self.exchangeProductId = data['exchangeProductId']
        self.productName = data['productName']
        self.productSymbol = data['productSymbol']
        self.baseCurrencySymbol = data['baseCurrencySymbol']
        self.quoteCurrencySymbol = data['quoteCurrencySymbol']
        self.exchangeId = data['exchangeId']
        self.exchangeName = data['exchangeName']


class ExchangeResponse(object):
    def __init__(self, data):
        self.exchangeId = data['exchangeId']
        self.exchangeName = data['exchangeName']
        self.websiteLink = data['websiteLink']
        self.countryOfOrigin = data['countryOfOrigin']
