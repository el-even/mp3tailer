import os
import urllib

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


# TODO: decomiss fetcher or add more actions to it
def fetcher(url, filename):
    urllib.urlretrieve(url, filename)


def crawler(label):
    url = "%s?id=%s" %(rooturl, str(label))
    filename = ("%s%s.txt") %(fetched_path, str(label))
    out_file = ("%s%s_u.txt") %(fetched_path, str(label))
    fetcher(url, filename)
    encoder(filename, out_file)
    print "%s > %s: %d bytes" %(url, filename, os.path.getsize(filename))
    return filename, out_file


def body():
    for label in xrange(first, last+1):
        url = "%s?id=%s" %(rooturl, str(label))
        crawler(label)
