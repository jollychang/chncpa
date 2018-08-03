# -*- coding: utf-8 -*-
#! /usr/bin/python
import requests
import os
import time
import sys

from BeautifulSoup import BeautifulSoup
from pync import Notifier

reload(sys)
sys.setdefaultencoding('utf8')


def check_tickets(url):
    #url = 'http://www.chncpa.org/ycgp/jmxx/2011-03-30/87483.shtml'
    print url
    KEYWORD = "【开票】"
    headers = {}
    r = requests.get(url, headers = headers)
    if KEYWORD in r.text:
        concert_title = get_concert_title(r.text)
        print concert_title
        print 'tickets!!!'
        Notifier.notify(concert_title, open=url.strip(), title='chncpa ticket is open')
        time.sleep(1)
        #os.system('echo %s | mutt jollychang@gmail.com -s "you can buy tickets now %s "' % (url, concert_title))
    else:
        print 'please wait'

def get_concert_title(html):
    concert_detail_soup = BeautifulSoup(html)
    concert_title = concert_detail_soup.head.title.string
    return concert_title


if __name__=='__main__':
    ticket_list_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'tickets.txt')
    file = open(ticket_list_file)
    for url in file.readlines():
        check_tickets(url)
    file.close()
