import urllib
import urllib2
import os
#import re


rooturl = "http://mp3tales.info/tales/"
first = 3
last = 4
fetched_path = "../fetched"

# def formattedpath(divider):
#     return size + divider + background + divider + textcolor

if not os.path.exists(fetched_path):
    os.makedirs(fetched_path)


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


def download(url):
    remote_file = urllib2.urlopen(url)
    file_name = url.split('/')[-1]
    local_file = open(file_name, 'wb')
    local_file.write(remote_file.read())
    local_file.close()



download("https://www.google.ru/logos/doodles/2015/evidence-of-water-found-on-mars-5652760466817024.2-hp.gif")

