import os
import urllib2

from config import *


def fetcher(url):
    print "\nRetrieving %s" %url,
    remote_html = urllib2.urlopen(url).read()
    print ok_mark
    print "Decoding %s" %url,
    # reencode source html from cp1251 to utf8 for parsing sake
    html = remote_html.decode('cp1251').encode('utf8')
    print ok_mark
    return html


def htmlsave(id, html):
    # check if fetched files directory exists and create it
    if not os.path.exists(fetched_path):
        os.makedirs(fetched_path)
    filename = ("%s%s.html") %(fetched_path, id)
    with open(filename, 'w') as htmlfile:
        htmlfile.write(html)
