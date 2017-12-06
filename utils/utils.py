# -*- coding: utf-8 -*-
# @Author: caixin
# @Date:   2017-12-05 17:27:51
# @Last Modified by:   1249614072@qq.com
# @Last Modified time: 2017-12-06 10:28:46
import toml

from ._compat import PY3


def get_conf(conf_file_path):
    """read toml conf file for latter use.


    :param conf_file_path: absolute path of conf file.
    :return:a dict contains configured infomation.
    """
    if PY3:
        with open(conf_file_path, encoding='utf-8') as conf_file:
            config = toml.loads(conf_file.read())
    else:
        with open(conf_file_path) as conf_file:
            config = toml.loads(conf_file.read())

    return config
