import base64
import datetime
import hashlib
import hmac

from BitsianPythonClient.Common.constant import apiKey, passphrase, METHOD, PATH, BODY, secretKey



def generate_signature(message):
    """
    create a signature
          :param message: message like a path and method and timestamp
          :return:created signature
    """
    hmac_key = secretKey
    digest = hmac.new(hmac_key.encode('utf-8'), message.encode("utf-8"), digestmod=hashlib.sha256).digest()
    signature = base64.b64encode(digest).decode()
    return signature


def subscribe_auth(dest, headers):
    """
    Generate subscription payload for authentication
          :param dest: destination path
          :param headers: apikey,signature,timestamp,secretKey
          :return:string of given data
    """
    return "SUBSCRIBE\nid:%s\nBITSIAN-API-SIGN:%s\nBITSIAN-API-KEY:%s\nBITSIAN-PASSPHRASE:%s\nBITSIAN-TIMESTAMP:%s\ndestination:%s\n\n\x00\n" \
           % (headers.get('id'), headers.get('BITSIAN-API-SIGN'), apiKey, passphrase, headers.get('BITSIAN-TIMESTAMP'),
              dest)


def subscribe_data(dest, headers_data):
    """
    Generate subscription payload for market data subscription
           :param dest: destination path
           :param headers: id
           :return:string of given data
    """
    return "SUBSCRIBE\nid:%s\ndestination:%s\n\n\x00\n" % (
        headers_data.get('id'), dest)


def get_auth_header():
    """
    get authentication headers
              :return: return the assigned headers
    """
    timestamp = str(datetime.datetime.utcnow())
    message = timestamp + METHOD + PATH + BODY
    headers = {}
    signature = generate_signature(message)
    headers['BITSIAN-API-SIGN'] = signature
    headers['BITSIAN-TIMESTAMP'] = timestamp
    headers['id'] = "1"
    return headers


def get_subscribe_header(id):
    """
    get a headers
           :param id: id for assign as header
           :return:header
    """
    headers_data = {}
    headers_data['id'] = id
    return headers_data
