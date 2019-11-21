class BalanceResponse(object):
    def __init__(self, data):
        self.exchangeId = data['exchangeId']
        self.currencyId = data['currencyId']
        self.availableBalance = data['availableBalance']
        self.realizedBalance = data['realizedBalance']
        self.currencySymbol = data['currencySymbol']
        self.exchangeName = data['exchangeName']
