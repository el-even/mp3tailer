import os
import re
import urllib2

from config import *
from db import *


if not os.path.exists(downloads_path):
    os.makedirs(downloads_path)


def download(id):
    try:
        # TODO: use single request to DB -- rewrite select(query) to return list
        mp3_url = select("SELECT mp3URL FROM files WHERE id=%s" %id)
        cover_url = select("SELECT coverURL FROM files WHERE id=%s" %id)
        tale_name = select("SELECT taleName FROM files WHERE id=%s" %id)
        mp3_name = "%s.mp3" %tale_name
        cover_name = "%s.jpg" %tale_name

        remote_mp3 = urllib2.urlopen(mp3_url)
        meta = remote_mp3.info()
        file_size = int(meta.getheaders("Content-Length")[0])

        local_file = open(downloads_path+mp3_name, 'wb')
        print "Downloading audio file for tale #%s: %s" %(id, mp3_name)
        file_size_dl = 0
        block_size = 8*1024
        while True:
            buffer = remote_mp3.read(block_size)
            if not buffer:
                break
            file_size_dl += len(buffer)
            local_file.write(buffer)
            status = r"%d of %d KB  [%3.2f%%]" % (file_size_dl/1024, file_size/1024, file_size_dl * 100. / file_size)
            status = status + chr(8)*(len(status)+1)
            print status,
        local_file.close()

        if os.path.getsize("%s" %(downloads_path+mp3_name)) == file_size:
            print "\n%s is successfully downloaded" %mp3_name
            query = ("UPDATE status SET isDownloaded=1 WHERE id='%s'") %id
            sql(query)
        else:
            print "\nSomething went wrong, downloaded mp3 is corrupted"
            query = ("UPDATE status SET isDownloaded=0 WHERE id='%s'") %id
            sql(query)

        print "Downloading cover art for tale #%s: %s" %(id, cover_name),
        file_name = "%s%s" %(downloads_path, cover_name)
        remote_cover = urllib2.urlopen(cover_url).read()
        with open(file_name, 'wb') as local_cover:
            local_cover.write(remote_cover)
        print ok_mark

    except:
        print "No URL found for tale #%s" %id
