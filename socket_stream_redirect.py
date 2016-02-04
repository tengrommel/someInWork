#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'teng'

import sys
from socket import *
port = 9090
host = 'localhost'
# 以前一个国外的blog 写了写关于重定向的东西 
# 自己改改拿来用 挺好的 感觉挺快的 
# 这是基本的脚本 之后就随便插就好

def initListenerSocket(port=port):
    sock=socket(AF_INET, SOCK_STREAM)
    sock.bind(('', port))
    sock.listen(5)
    conn, addr = sock.accept()
    return conn

def redirectOut(port=port, host=host):
    sock=socket(AF_INET, SOCK_STREAM)
    sock.connect((host, port))
    file=sock.makefile('w')
    sys.stdout=file
    return sock

def redirectIn(port=port, host=host):
    sock=socket(AF_INET, SOCK_STREAM)
    sock.connect((host, port))
    file=sock.makefile('r')
    sys.stdin=file
    return sock

def redirectBothAsClient(port=port,host=host):
    sock=socket(AF_INET, SOCK_STREAM)
    sock.connect((host, port))
    ofile=sock.makefile('w')
    ifile=sock.makefile('r')
    sys.stdout=ofile
    sys.stdin=ifile
    return sock

def redirectBothAsServer(port=port, host=host):
    sock=socket(AF_INET, SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(5)
    conn, addr = sock.accept()
    ofile = conn.makefile('w')
    ifile = conn.makefile('r')
    sys.stdout = ofile
    sys.stdin = ifile
    return conn