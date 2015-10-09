import os
import urllib2

from config import *


if not os.path.exists(fetched_path):
    os.makedirs(fetched_path)

if not os.path.exists(downloads_path):
    os.makedirs(downloads_path)


def fetcher(url):
    print "Retrieving %s" %url,
    remote_html = urllib2.urlopen(url).read()
    print ok_mark
    print "Decoding %s" %url,
    # reencode source html from cp1251 to utf8 for parsing sake
    html = remote_html.decode('cp1251').encode('utf8')
    print ok_mark
    return html
