import urllib
import urllib2
import os
import re


rooturl = "http://mp3tales.info/tales/"
first = 3
last = 4
fetched_path = "../fetched/"
downloads_path = "../files/"


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


def getName(remote_file):
    try:
        result = re.search('filename="(.*)"', remote_file.info().getheaders("Content-Disposition")[0]).group(1)
    except:
        result = ""
    return result
    

def download(url):
    remote_file = urllib2.urlopen(url)
    if getName(remote_file) != "":
        file_name = getName(remote_file)
    else:
        file_name = url.split('/')[-1]
    print file_name

    local_file = open(downloads_path+file_name, 'wb')
    meta = remote_file.info()

    file_size = int(meta.getheaders("Content-Length")[0])
    print "Downloading %s" % (file_name.split('/')[-1])

    print meta.getheaders("Content-Disposition")[0]

    file_size_dl = 0
    block_sz = 8*1024
    while True:
        buffer = remote_file.read(block_sz)
        if not buffer:
            break

        file_size_dl += len(buffer)
        local_file.write(buffer)
        status = r"%d of %d KB  [%3.2f%%]" % (file_size_dl/1024, file_size/1024, file_size_dl * 100. / file_size)
        status = status + chr(8)*(len(status)+1)
        print status,

    local_file.close()


download("http://download.linnrecords.com/test/m4a/tone24bit.aspx")
# download("http://mp3tales.info/audio/prikljuchenija_buratino.mp3")

