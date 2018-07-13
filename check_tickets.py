# -*- coding: utf-8 -*-
#! /usr/bin/python
import urllib2
import requests
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
    keyword = "【开票】"
    headers = {}
    headers['Cookie'] = 'coBUDrHx6D=MDAwM2IyNzNhNDQwMDAwMDAwMDQwZi1MIlYxMzkxNDYzOTYx; Hm_lvt_c0f83d11c5318938a003c0a00dcded64=1391681917; Hm_lpvt_c0f83d11c5318938a003c0a00dcded64=1391681917; _gscu_1063692112=91681917r202yo21; _gscs_1063692112=91681917yri46l21|pv:1; _gscbrs_1063692112=1; JSESSIONID=84yvSzhLyG52DK8JTDdr7hhJrX5nn3L18qp638t916FLmxBTYWs1!-194699159'
    r = requests.get(url, headers = headers)
    if keyword in r.text:
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


if __name__=='__main__':
    ticket_list_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'tickets.txt')
    file = open(ticket_list_file)
    for url in file.readlines():
        check_tickets(url)
    file.close()
