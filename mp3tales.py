import urllib
import urllib2
import os
# import re

from download import *
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


def fetcher(url, filename):
    urllib.urlretrieve(url, filename)
    print ": %s bytes" %os.path.getsize(filename)


# does nothing yet
def crawler(label):
    url = "%s?id=%s" %(rooturl, str(label))
    filename = str(label) + ".txt"
    out_file = str(label) + "_u.txt"
    print url, ">", filename,
    return filename, out_file


def body():
    for label in xrange(first, last+1):
        url = "%s?id=%s" %(rooturl, str(label))

        
        filename = ("%s%s.txt") %(fetched_path, str(label))
        out_file = ("%s%s_u.txt") %(fetched_path, str(label))
        print url, ">", filename,

        fetcher(url, filename)
        encoder(filename, out_file)


download("http://download.linnrecords.com/test/m4a/tone24bit.aspx")
# download("http://mp3tales.info/audio/prikljuchenija_buratino.mp3")


