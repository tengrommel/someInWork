#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'teng'

import os, sys
from getpass import getpass
from ftplib import FTP

nonpassive = False
filename = 'remote.jpg'
dirname = '.'
sitename = 'ftp.ziji.ff'
userinfo = ('teng', getpass('Passwd?'))
if len(sys.argv) > 1: filename = sys.argv[1]
print('Connecting...')
connection = FTP(sitename)
connection.login(*userinfo)
connection.cwd(dirname)
if nonpassive:
    connection.set_pasv(False)

print('Downloading...')
localfile = open(filename, 'wb')
connection.retrbinary('RETR '+ filename, localfile.write, 1024)
connection.quit()
localfile.close()


