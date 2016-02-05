#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'teng'
import os, getpass
from urllib.request import urlopen
filename = 'remote.jpg'
password = getpass.getpass('Pswd?')

remoteaddr = 'ftp://lutz:%s@ftp.rmi.net/%s;type=i' % (password, filename)
print('Downloading', remoteaddr)

remotefile = urlopen(remoteaddr)
localfile = open(filename, 'wb')
localfile.write(remotefile.read())
localfile.close()
remotefile.close()