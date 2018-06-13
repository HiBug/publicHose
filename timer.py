# -*- coding:utf-8 -*-
from datetime import datetime, timedelta


def runTask(func, period):
    runCnt = 1
    now = datetime.now()

    next_time = now+timedelta(seconds=period)
    while True:
        now = datetime.now()
        if next_time <= now:
            next_time = now+timedelta(seconds=period)
            print '第%4d次执行  %s  下次执行时间:%s' % (runCnt, now.strftime('%Y-%m-%d %H:%M:%S'), next_time.strftime('%Y-%m-%d %H:%M:%S'))
            func()
            runCnt += 1
