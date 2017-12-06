# -*- coding: utf-8 -*-
# @Author: caixin
# @Date:   2017-11-28 13:51:44
# @Last Modified by:   1249614072@qq.com
# @Last Modified time: 2017-12-06 10:27:57
"""
create Apriso Job and get execution result

"""
import json
from zeep import Client

import constants
from .xmls import parse_xml

"""
xsd\\valueobjects.py
line 173:index = 1

"""


class JEClient(object):
    """ Apriso Job Executor Client """

    def __init__(self, conf):
        conf = conf['apriso']
        self.host = conf.get('host', '127.0.0.1')
        self.operation = conf.get('operation', '')

    def connect_apriso(self):
        try:
            client = Client(constants.APRISO_URL % (self.host))
            self.service = client.bind('JobExecutor', 'JobExecutorSoap12')
        except Exception as e:
            raise

    def exec_operation(self, json_data=''):
        json_str = json.dumps(json)
        params = constants.DATAXMLS % (self.operation, json_str)
        try:
            self.connect_apriso()
            result = self.service.ExecuteJobSynchronously(
                actionParameters=params,
                actionType=1,
                attemptSleepDuration=0,
                description='ws client',
                name=self.operation,
                numberOfExecutionAttempts=1,
                pool='DEFAULT',
                synchronizationQueue='SQ', timeout=0, transactionDataQueueId=0
            )
            return self._parse(result)
        except Exception as e:
            raise

    def _parse(self, result):
        val = result['results']
        try:
            if val:
                return parse_xml(val)
            return False
        except Exception as e:
            raise


if __name__ == '__main__':
    try:
        opr = JEClient()
        opr.exec_operation()
    except Exception as e:
        print(str(e))
