import os
import urllib2

from config import *
from db import *


if not os.path.exists(downloads_path):
    os.makedirs(downloads_path)


def download_mp3(id, remote_mp3, local_mp3):
    try:
        print "Downloading %s" %(local_mp3),  # comma left for nok_mark to be printed on the very same line
        remote_file = urllib2.urlopen(remote_mp3)
        meta = remote_file.info()
        file_size = int(meta.getheaders("Content-Length")[0])

        with open(downloads_path+local_mp3, 'wb') as local_file:
            file_size_dl = 0
            block_size = 8*1024
            status = ""
            while True:
                buffer = remote_file.read(block_size)
                if not buffer:
                    break
                file_size_dl += len(buffer)
                local_file.write(buffer)
                status = r"%d of %d KB  [%3.2f%%]" % (file_size_dl/1024, file_size/1024, file_size_dl * 100. / file_size)
                status = status + chr(8)*(len(status)+1)
                print status,

        if os.path.getsize("%s" %(downloads_path+local_mp3)) == file_size:
            query = ("UPDATE status SET isDownloaded=1 WHERE id='%s'") %id
            sql(query)
        else:
            query = ("UPDATE status SET isDownloaded=0 WHERE id='%s'") %id
            sql(query)
            print "\nSomething went wrong, downloaded mp3 is corrupted"
    except:
        print nok_mark


def download_cover(remote_cover, local_cover):
    try:
        print "Downloading %s" %(local_cover),
        file_name = "%s%s" %(downloads_path, local_cover)
        remote_cover = urllib2.urlopen(remote_cover).read()
        with open(file_name, 'wb') as local_file:
            local_file.write(remote_cover)
        print ok_mark
    except:
        print nok_mark


def download(id):
    try:
        data = select("SELECT taleName, mp3URL, coverURL FROM files WHERE id=%s" %id)
        tale_name, mp3_url, cover_url = data[0], data[1], data[2]
        mp3_name = "%s.%s" %(tale_name, mp3_url.split('.')[-1])
        cover_name = "%s.%s" %(tale_name, cover_url.split('.')[-1])
        download_mp3(id, mp3_url, mp3_name)
        print  # add new line
        download_cover(cover_url, cover_name)
    except:
        print "No URL found for tale #%s" %id
