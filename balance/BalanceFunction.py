import json

from BitsianPythonClient.Balance.BalanceResponse import BalanceResponse
from BitsianPythonClient.Common.PageRequest import PageRequest
from BitsianPythonClient.Common.constant import BALANCE, REST_END_POINT, METHOD, page
from BitsianPythonClient.GetResponse import getResponse as s


def getBalance(exchangeId, currencyId):
    """
    get list of balance details
    :param exchangeId: exchangeId param for rest call
    :param currencyId: currencyId param for rest call
    :return: list of balance details
    """
    params ={True:"exchangeId="+str(exchangeId) + "&", False: ""}[exchangeId != None] + {True:"currencyId="+str(currencyId), False: ""}[currencyId != None]
    if params!="":
            params = "?" + params
    data = s.get_response(REST_END_POINT, BALANCE +  params, METHOD, "")
    my_objects = []
    datalength = len(data['data'])
    i = 0
    while (i < datalength):
        my_objects.append((json.dumps(BalanceResponse(data['data'][i]).__dict__)))
        i = i + 1
    my_objects.append((json.dumps(PageRequest(data[page]).__dict__)))
    return str(my_objects)
