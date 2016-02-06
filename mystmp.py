#!/usr/bin/env python
# -*- coding:utf-8 -*-


import smtplib, sys, email.utils
mailserver="smtp.126.com"

host_name="XXXXX"
host_pass="XXXX"
From = input('From? ').strip()                 # or import from mailconfig
To   = input('To?   ').strip()                 # ex: python-list@python.org
Tos  = To.split(';')                           # allow a list of recipients
Subj = input('Subj? ').strip()
Date = email.utils.formatdate()                # curr datetime, rfc2822


text = ('From: %s\nTo: %s\nDate: %s\nSubject: %s\n\n' % (From, To, Date, Subj))

print('Type message text, end with line=[Ctrl+d (Unix), Ctrl+z (Windows)]')
while True:
    line = sys.stdin.readline()
    if not line:
        break

    text += line

print('Connecting...')
server = smtplib.SMTP(mailserver)              # connect, no log-in step
server.login(host_name, host_pass)
server.data()
failed = server.sendmail(From, Tos, text)
server.quit()
if failed:                                     # smtplib may raise exceptions
    print('Failed recipients:', failed)        # too, but let them pass here
else:
    print('No errors.')
print('Bye.')
