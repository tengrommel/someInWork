#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'teng'
import sys,os,multiprocessing
from Internet.Sockets.socket_stream_redirect import initListenerSocket, redirectOut
"""简单测试下"""

# redirected client output
def server():
    mypid = os.getpid()
    conn = initListenerSocket()
    file = conn.makefile('r')
    for i in range(3):
        data = file.readline().rstrip()
        print('server %s got [%s]' % (mypid, data))

def client():
    mypid = os.getpid()
    redirectOut()
    for i in range(3):
        print('client %s: %s' % (mypid, i))
        sys.stdout.flush()

if __name__=='__main__':
    multiprocessing.Process(target=server).start()
    client()
# 结果为 
# server 10737 got [client 10736: 0]
# server 10737 got [client 10736: 1]
# server 10737 got [client 10736: 2]
