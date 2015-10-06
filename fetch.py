import os
import urllib
# TODO: evolve from urllib to urllib2 for consistency

from config import *


if not os.path.exists(fetched_path):
    os.makedirs(fetched_path)

if not os.path.exists(downloads_path):
    os.makedirs(downloads_path)


def encoder(cp1251_file, utf8_file):
    text_in_cp1251 = open(cp1251_file, 'r').read()
    text_in_unicode = text_in_cp1251.decode('cp1251')
    text_in_utf8 = text_in_unicode.encode('utf8')
    open(utf8_file, 'wb').write(text_in_utf8)


# TODO: decomiss fetcher or add more actions to it; change urllib to urllib2
def fetcher(url, filename):
    urllib.urlretrieve(url, filename)


def crawler(tale_id):
    url = "%s?id=%s" %(talesurl, str(tale_id))
    filename = ("%s%s.txt") %(fetched_path, str(tale_id))
    out_file = ("%s%s_u.txt") %(fetched_path, str(tale_id))
    fetcher(url, filename)
    encoder(filename, out_file)
    print "%s > %s: %d bytes" %(url, filename, os.path.getsize(filename))
    return filename, out_file


# TODO: move this to mp3tales.py
def body():
    for tale_id in xrange(first, last+1):
        url = "%s?id=%s" %(talesurl, str(tale_id))
        crawler(tale_id)
