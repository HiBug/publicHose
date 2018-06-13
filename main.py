# -*- coding:utf-8 -*-
from showMessage import showMessage
from parseHtml import getHouseName
from timer import runTask


cookie = 'ASP.NET_SessionId=dh01g2nv0rdya2ctgdklhmwc'
# 刷新时间
period = 2


def work():
    name = getHouseName(1, cookie)
    if name is not None:
        showMessage(name)

runTask(work, period)
