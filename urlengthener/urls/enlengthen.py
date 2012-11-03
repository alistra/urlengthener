import urllib2
import HTMLParser

from BeautifulSoup import BeautifulSoup

class HeadRequest(urllib2.Request):
    def get_method(self):
        return "HEAD"

def sanitizeword(word):
    h = HTMLParser.HTMLParser()
    w = h.unescape(word)

    w = w.strip('\'&=[]"$_:!;.,- ')
    w = w.replace('"','')
    w = w.replace('$','')
    w = w.replace('&','')
    w = w.replace(']','')
    w = w.replace('[','')
    w = w.replace("'",'')
    w = w.replace(' ','')
    w = w.replace('_','-')
    w = w.replace('!','-')
    w = w.replace('.','-')
    w = w.replace(';','-')
    w = w.replace('=','-')
    w = w.replace(',','-')
    w = w.replace(':','-')
    w = w.lower()
    return w

def wordgen(url):
    response = urllib2.urlopen(HeadRequest(url))
    html = response.read()
    soup = BeautifulSoup(html)
    for word in soup.html.head.title.string.split(' '):
        w = sanitizeword(word)
        if w != '':
            yield w.lower()

    for p in soup.findAll('p'):
        for elem in p.contents:
            if elem.string:
                for word in elem.string.split(' '):
                    w = sanitizeword(word)
                    if w != '':
                        yield w

def enlengthen(url, maxlength = 4096):

    longurl = 'url'
    gen = wordgen(url)

    try:
        while True:
            w = next(gen)

            if len(w) + len(longurl) > maxlength:
                break

            longurl = "".join([longurl, '-', w])

    except StopIteration:
        pass

    return longurl
