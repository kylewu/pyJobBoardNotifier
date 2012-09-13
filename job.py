#!/usr/bin/env python
# -*- coding: utf-8 -*-


from pyquery import PyQuery as pq

from mail import mail
from settings import gmail_user

AWARENESS_LIST = ['copenhagen', 'denmark',
                  'sweden', 'stockholm']

PYJOBBOARD_URL = 'http://www.python.org/community/jobs/'

#with open('./pjb.html', 'r') as f:
    #html = f.read()


secs = pq(url=PYJOBBOARD_URL)('div.section')

for sec in secs:
    sec = pq(sec)
    id = sec.attr('id').lower()
    for w in id.split('-'):
        if w in AWARENESS_LIST:
            mail(gmail_user, id, sec.html().encode('utf-8'))
            break
