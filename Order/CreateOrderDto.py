class CreateOrderDto(object):
    def __init__(self, data):
        self.currencyPair = data['currencyPair']
        self.orderSide = data['orderSide']
        self.quantity = data['quantity']
        self.price = data['price']
        self.orderType = data['orderType']
        self.exchangeId = data['exchangeId']
        self.tifType = data['tifType']
