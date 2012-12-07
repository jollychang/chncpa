# -*- coding: utf-8 -*-
#! /usr/bin/python
import urllib2
import os
from BeautifulSoup import BeautifulSoup
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
        concert_title = get_ticket_title(url)
        print concert_title
        print 'tickets!!!'
        os.system('echo %s | mutt jollychang@gmail.com -s "you can buy tickets now %s "' % (url, concert_title))
    else:
        print 'please wait'

def get_ticket_title(url):
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
    file = open('tickets.txt')
    for url in file.readlines():
        check_tickets(url)
    file.close()