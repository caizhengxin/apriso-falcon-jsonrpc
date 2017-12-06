# -*- coding: utf-8 -*-
# @Author: caixin
# @Date:   2017-11-01 10:38:54
# @Last Modified by:   1249614072@qq.com
# @Last Modified time: 2017-12-06 10:41:38
import falcon

from jsonrpc import JSONRPCResponseManager, dispatcher
from utils.apriso import JEClient
import constants

opr = JEClient(constants.CONF)


@dispatcher.add_method
def employee():
    return opr.exec_operation()


class Test(object):
    def on_post(self, req, resp):
        resp.content_type = 'application/json'
        datas = req.stream.read()
        response = JSONRPCResponseManager.handle(datas, dispatcher)
        resp.body = response.json
        resp.status = falcon.HTTP_200


api = falcon.API()
api.add_route('/test', Test())


if __name__ == '__main__':
    pass
