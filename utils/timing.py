# -*- coding: utf-8 -*-
# @Author: caixin
# @Date:   2017-03-24 16:39:22
# @Last Modified by:   caixin
# @Last Modified time: 2017-04-09 23:30:40
from apscheduler.schedulers.background import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler


def timing(func, timing_type='interval', seconds=2):
    scheduler = BlockingScheduler()
    scheduler.daemonic = False
    scheduler.add_job(func, timing_type, seconds=seconds)
    scheduler.start()


def timing_background(func, timing_type='interval', seconds=2):
    scheduler = BackgroundScheduler()
    scheduler.daemonic = False
    scheduler.add_job(func, timing_type, seconds=seconds)
    scheduler.start()
