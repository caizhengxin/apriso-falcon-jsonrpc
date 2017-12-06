# -*- coding: utf-8 -*-
# @Author: caixin
# @Date:   2017-11-01 10:39:05
# @Last Modified by:   1249614072@qq.com
# @Last Modified time: 2017-12-05 16:38:03
import requests
import json


def test():
    url = "http://localhost:9000/test"
    headers = {'content-type': 'application/json'}

    payload = {
        "method": "employee",
        "params": {},
        "jsonrpc": "2.0",
        "id": '0'
    }
    response = requests.post(
        url, data=json.dumps(payload), headers=headers)
    print(response.json())


if __name__ == "__main__":
    test()
