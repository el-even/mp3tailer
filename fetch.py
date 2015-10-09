# import os
import urllib2

from config import *

# left for debug sake
# TODO: get rid of it on release
# if not os.path.exists(fetched_path):
#     os.makedirs(fetched_path)


def fetcher(url):
    print "Retrieving %s" %url,
    remote_html = urllib2.urlopen(url).read()
    print ok_mark
    print "Decoding %s" %url,
    # reencode source html from cp1251 to utf8 for parsing sake
    html = remote_html.decode('cp1251').encode('utf8')
    print ok_mark
    return html
