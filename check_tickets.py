import urllib2
import os
from BeautifulSoup import BeautifulSoup

def check_tickets(url):
    #url = 'http://www.chncpa.org/ycgp/jmxx/2011-03-30/87483.shtml'
    tmp = url.split('/')
    tmp = tmp[-1:][0]
    id = tmp.split('.')[0]
    ticket_url = 'http://ticket.chncpa.org/unit.jsp?productId=' + id
    print ticket_url
    data = urllib2.urlopen(ticket_url)
    soup = BeautifulSoup(data)
    img = soup.findAll('img')
    if len(img)>0:
        print 'tickets!!!'
        os.system('echo | mutt jollychang@gmail.com -s "you can buy tickets now %s"' % url)
    else:
        print 'please wait'

if __name__=='__main__':
    file = open('tickets.txt')
    for url in file.readlines():
        check_tickets(url)
    file.close()