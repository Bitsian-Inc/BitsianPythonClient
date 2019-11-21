import json

from BitsianPythonClient.Common.PageRequest import PageRequest
from BitsianPythonClient.Common.constant import REST_END_POINT, ORDER, METHOD, CANCEL, responsedata, page
from BitsianPythonClient.GetResponse import getResponse as s
from BitsianPythonClient.Order.OrderResponse import OrderResponse
from BitsianPythonClient.Order.createOrderDto import CreateOrderDto


def getAllOrders(resolution):
    """
    get all orders details
          :param resolution:resolution param for rest call
          :return: list of all orders
    """
    params = "resolution="+str(resolution)
    data = s.get_response(REST_END_POINT, ORDER + "?" + params, METHOD, "")
    my_objects = []
    datalength = len(data['data'])
    i = 0
    while (i < datalength):
        my_objects.append(((OrderResponse((data[responsedata][i])).__dict__)))
        i = i + 1
    my_objects.append(((PageRequest(data[page]).__dict__)))
    return json.dumps(my_objects)


def createOrder(order: CreateOrderDto):
    """
    create a order with given inputs
          :param order: order as body for rest call
          :return:get created order
    """
    data = s.get_response(REST_END_POINT, ORDER, 'POST', order)
    data = OrderResponse(data[responsedata])
    return json.dumps(data.__dict__)


def getOrder(orderId):
    """
    get order details for given order id
          :param orderId: orderid for get particular order
          :return: order details of given orderId
    """
    data = s.get_response(REST_END_POINT, ORDER + "/" + str(orderId), METHOD, None)
    data = OrderResponse(data[responsedata])
    return json.dumps(data.__dict__)


def cancelOrder(orderId):
    """
    cancel the order for given id
          :param orderId: orderId for cancel particular order
          :return:cancelled order of given orderId
    """
    data = s.get_response(REST_END_POINT,
                          ORDER + "/" + str(orderId) + CANCEL
                          , 'POST', None)
    data = OrderResponse(data[responsedata])
    return json.dumps(data.__dict__)
