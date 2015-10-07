import urllib2
import re

from config import *
from db import *


def download(id, url):
    remote_file = urllib2.urlopen(url)
    meta = remote_file.info()

    try:
        file_name = re.search('filename="(.*)"', meta.getheaders("Content-Disposition")[0]).group(1)
    except:
        file_name = url.split('/')[-1]

    file_extention= file_name.split('.')[-1]
    file_name = ("%s.%s") %(file_name.split('.')[-2], file_name.split('.')[-1])

    local_file = open(downloads_path+file_name, 'wb')

    file_size = int(meta.getheaders("Content-Length")[0])
    print "Downloading %s" % file_name

    # file_size_dl = 0
    # block_sz = 8*1024
    # while True:
    #     buffer = remote_file.read(block_sz)
    #     if not buffer:
    #         break

    #     file_size_dl += len(buffer)
    #     local_file.write(buffer)
    #     status = r"%d of %d KB  [%3.2f%%]" % (file_size_dl/1024, file_size/1024, file_size_dl * 100. / file_size)
    #     status = status + chr(8)*(len(status)+1)
    #     print status,

    local_file.close()

    # query = ("INSERT OR REPLACE INTO files (id, fileName) VALUES (%s, 'ABC')") %(id)
    # sql(query)

download(10, "http://mp3tales.info/audio/prikljuchenija_buratino.mp3")
# download("http://mp3tales.info/screen/pre/280x280xprikljuchenija_buratino.jpg.pagespeed.ic.ViQl-ABr1T.jpg")
# download("http://download.linnrecords.com/test/m4a/tone24bit.aspx")
