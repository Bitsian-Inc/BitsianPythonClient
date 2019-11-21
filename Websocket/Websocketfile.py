from websocket import create_connection
from BitsianPythonClient.Common.constant import WEBSOCKET_DESTINATION_PRIFEX, ORDER_BOOK, TRADE_TAP, WEBSOCKET_BASE_URL, \
    PATH, AUTH_FEED
from BitsianPythonClient.Websocket.GetAuthentication import subscribe_data, get_auth_header, subscribe_auth,get_sub_header
import uuid

def parse(result):
    """
    Extract the actual  from websocket messages
           :param result: result param as json data
           :return: return splitted string
    """
    data = result.split("\n\n", 1)[1]
    return data[:-1]


def subscribe(path, headers, ws):
    """
    get a response from subscribed channel
    :param path: path as destination for api
    :param headers: headers for api
    :param ws: connection created variable
    """
    sub = subscribe_data(path, headers)
    ws.send(sub)
    while True:
        result = ws.recv()
        data = parse(result)
        print(data)


def create():
    """
    create a connection for given url
    :return: response of given destination
    """
    headers = get_auth_header()
    destination = WEBSOCKET_DESTINATION_PRIFEX + AUTH_FEED
    ws = create_connection(WEBSOCKET_BASE_URL + PATH)
    sub = subscribe_auth(destination, headers)
    ws.send(sub)
    result = ws.recv()
    if (result):
        subscribe(WEBSOCKET_DESTINATION_PRIFEX + ORDER_BOOK + "/btc/usd", get_subscribe_header
        (str(uuid.uuid1()), ws)
        subscribe(WEBSOCKET_DESTINATION_PRIFEX + TRADE_TAP + "/ltc/usdt", get_subscribe_header
        (str(uuid.uuid1()), ws)
        subscribe(WEBSOCKET_DESTINATION_PRIFEX + TRADE_TAP + "/bitmart/ltc/usdt", get_subscribe_header
        (str(uuid.uuid1()), ws)
        subscribe(WEBSOCKET_DESTINATION_PRIFEX + ORDER_BOOK + "/coinbase/btc/usd", get_subscribe_header
        (str(uuid.uuid1()), ws)
