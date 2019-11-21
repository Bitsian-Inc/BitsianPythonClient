import base64
import hashlib
import hmac

from BitsianPythonClient.Common.constant import secretKey


def generate_signature(path, method, body, timestamp):
    """
    get created signature
       :param path:destination path for rest call
       :param method:rest call method
       :param body: body for create signature
       :param timestamp: current date and time in utc
       :return:response data of rest call
    """
    shared_secret = secretKey
    path = str(timestamp) + method + path + {True: str(body), False: ""}[body != None]
    digest = hmac.new(shared_secret.encode('utf-8'), path.encode(), digestmod=hashlib.sha256).digest()
    signature = base64.b64encode(digest).decode()
    return signature
