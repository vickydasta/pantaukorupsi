#!/usr/bin/python

__author__ = 'vickydasta'
__author__ = 'andrechristoga'

from urllib2 import urlopen
import lxml.html

host = 'http://www.pekanbaruexpress.com/korupsi.html'
host2 = 'http://pekanbaru.tribunnews.com/tag/korupsi'

def geturl():
    '''
    Parser url bersentimen korupsi
    '''

    try:
        html_data = urlopen(host).read()
    except:
        raise Exception('Something went wrong...')

    parser = lxml.html.fromstring(html_data)

    urls = []

    for url in parser.xpath('//a/@href'):
        if 'korupsi' in url:
            urls.append(url.split('/'))

    clean = []

    for item in urls:
        clean.append(item[-1])

    url_ = []
    for i in range(len(clean)):
        if i > 2:
            url_.append(clean[i])

    return url_

def newtitle(url):
    form = url.split('-') # deform url form
    id = int(form[0]) # get news id
    form.pop(0) # remove id
    # rm html
    title = ' '.join(form) # join all words
    return {id:title}

def getdata():
    data = {}
    for url in geturl():
        f = newtitle(url)
        data[f.keys()[0]] = f.values()
    return data


def getraw(data):
    # get raw of links (link-append-title-whatever) into (link append title whatever)
    raw = []
    for item in data:
        raw.append(item[0])

    return ' '.join(raw)

def tf(raw):
    # term frequency function added
    n = {}
    for k in raw.split():
        n[k] = raw.split().count(k) # count how many frequency of k in raw

    return n



if __name__ == '__main__':
    data = getdata()
    print getdata()
    print getraw(data.values())
    print tf(getraw(data.values()))
