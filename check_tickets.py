# -*- coding: utf-8 -*-
#! /usr/bin/python
import urllib2
import os
import time
from BeautifulSoup import BeautifulSoup
from pync import Notifier
import sys 
reload(sys) 
sys.setdefaultencoding('utf8') 


def check_tickets(url):
    #url = 'http://www.chncpa.org/ycgp/jmxx/2011-03-30/87483.shtml'
    print url
    id = get_id_by_ticket_url(url)
    unit_url = 'http://ticket.chncpa.org/unit.jsp?productId=' + id
    data = urllib2.urlopen(unit_url)
    soup = BeautifulSoup(data)
    img = soup.findAll('img')
    if len(img)>0:
        concert_title = get_title_by_ticket_url(url)
        print concert_title
        print 'tickets!!!'
        Notifier.notify(concert_title, open=url.strip(), title='chncpa ticket is open')
        time.sleep(1)
        #os.system('echo %s | mutt jollychang@gmail.com -s "you can buy tickets now %s "' % (url, concert_title))
    else:
        print 'please wait'

def get_title_by_ticket_url(url):
    concert_detail_data = urllib2.urlopen(url)
    concert_detail_soup = BeautifulSoup(concert_detail_data)
    concert_title = concert_detail_soup.head.title.string
    return concert_title

def get_id_by_ticket_url(url):
    tmp = url.split('/')
    tmp = tmp[-1:][0]
    id = tmp.split('.')[0]
    return id


if __name__=='__main__':
    ticket_list_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'tickets.txt')
    file = open(ticket_list_file)
    for url in file.readlines():
        check_tickets(url)
    file.close()
