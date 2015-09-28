import urllib
import os
import sqlite3


#import re

rooturl = "http://mp3tales.info/tales/"
database = "../tales.db"
first = 1
last = 2
fetched_path = "../fetched"

con = sqlite3.connect(database)
cur = con.cursor()


if not os.path.exists(fetched_path):
    os.makedirs(fetched_path)


def sql(query):
    cur.execute(query)
    con.commit()


def db_init():
    sql("CREATE TABLE IF NOT EXISTS status (id INTEGER PRIMARY KEY, \
        isFetched BOOLEAN,\
        isDownloaded BOOLEAN,\
        isTagged BOOLEAN)")

    sql("CREATE TABLE IF NOT EXISTS tags (id INTEGER PRIMARY KEY,\
        title TEXT,\
        author TEXT,\
        year INTEGER,\
        description TEXT)")

    sql("CREATE TABLE IF NOT EXISTS remote_files (id INTEGER PRIMARY KEY,\
        mp3URL TEXT,\
        coverURL TEXT)")


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

        
        filename = ("%s/%s.txt") %(fetched_path, str(label))
        out_file = ("%s/%s_u.txt") %(fetched_path, str(label))
        print url, ">", filename,

        fetcher(url, filename)
        encoder(filename, out_file)

        # output=open(filename, 'rb')
        # print output.read()

db_init()

con.close()
