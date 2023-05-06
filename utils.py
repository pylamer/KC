import json
import requests
import time

URL_SEC_NUMBER = 'https://lab.karpov.courses/hardml-api/module-5/get_secret_number'

def get_secret_number(url):
    flag = True
    count = 1
    secret_number = None
    while flag and count < 100:
        time.sleep(0.5)
        # print(count)
        try:
            response = requests.get(URL_SEC_NUMBER).text.replace("'", '"')
            res = json.loads(response)
            secret_number = res['secret_number']
            flag = False
        except:
            count += 1

    if secret_number is None:
        return -1
    else:
        return secret_number

