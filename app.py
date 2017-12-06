# -*- coding: utf-8 -*-
# @Author: caixin
# @Date:   2017-12-05 17:19:52
# @Last Modified by:   1249614072@qq.com
# @Last Modified time: 2017-12-06 10:41:12
import waitress

import constants
from web.server import api


def init(conf):
    pass


if __name__ == '__main__':
    conf = constants.CONF
    init(conf)
    sv = conf.get('server', {})
    host = sv.get('host', '0.0.0.0')
    port = sv.get('port', 8000)
    waitress.serve(api, host=host, port=port, _quiet=True)
