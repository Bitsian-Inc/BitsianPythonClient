import json
import os

from BitsianPythonClient.Common.constant import REST_END_POINT, EXCHANGE, CURRENCY, PRODUCT, METHOD
from BitsianPythonClient.ErdPrd.ErdPrdResponse import CurrencyResponse, ProductResponse, ExchangeResponse
from BitsianPythonClient.GetResponse import getResponse as s


def getExchanges():
    """
    get exchange list
           :return:list of exchanges
    """
    data = s.get_response(REST_END_POINT, EXCHANGE, METHOD, "")
    my_objects = []
    for item in data:
        my_objects.append(((ExchangeResponse((item)).__dict__)))
    return json.dumps(my_objects)


def getCurrencies():
    """
    get currency list
          :return:list of currencies
    """
    data = s.get_response(REST_END_POINT, CURRENCY, METHOD, "")
    my_objects = []
    for item in data:
        my_objects.append(((CurrencyResponse((item)).__dict__)))
    return json.dumps(my_objects)

def getProducts(exchangeId):
    """
    get products list
        :param exchangeId: Exchange Id
        :return:list of products
    """
    params = 'exchangeId=' + str(exchangeId)
    data = s.get_response(REST_END_POINT, PRODUCT + "?" + params, METHOD,
                      "")
    my_objects = []
    for item in data:
        my_objects.append(((ProductResponse((item)).__dict__)))
    return json.dumps(my_objects)
