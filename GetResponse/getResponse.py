import datetime
import requests
from BitsianPythonClient.Common import getSignature as ev
from BitsianPythonClient.Common.constant import apiKey, secretKey, passphrase
from BitsianPythonClient.Order.createOrderDto import CreateOrderDto


def get_response(url, path, method, order : CreateOrderDto):
        """
        get rest call response
        :param url:base path of rest call
        :param path:destination path for rest call
        :param method:rest call method
        :param order: body for rest call
        :return:response data of rest call
        """
        timestamp = datetime.datetime.now(datetime.timezone.utc)
        # Timestamp should be in milliseconds
        time = int(round(timestamp.timestamp() * 1000))
        signature= ev.generate_signature(path,method,order,time)
        response = requests.request(method, (url + path), data = order,
                                    headers = {"BITSIAN-API-KEY":apiKey,
                                                'BITSIAN-TIMESTAMP': time,
                                                "SECRET_KEY":secretKey,"BITSIAN-PASSPHRASE":passphrase,
                                                "BITSIAN-API-SIGN":signature,"Content-Type":"application/json"}
)
        return response.json()
