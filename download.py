import os
import urllib2

from config import *
from db import *


if not os.path.exists(downloads_path):
    os.makedirs(downloads_path)


def download_mp3(id):
    try:
        print "Downloading tale #%s" %id,  # comma left for nok_mark to be printed on the very same line

        data = select("SELECT audioRemote, audioLocal, audioLength FROM files WHERE id=%s" %id)
        local_mp3 = downloads_path+data[1]
        file_size = data[2]
        remote_mp3 = urllib2.urlopen(data[0])

        is_downloaded = 0  # dropping download flag
        with open(local_mp3, 'wb') as local_file:
            file_size_dl = 0
            block_size = 8*1024
            status = ""
            while True:
                buffer = remote_mp3.read(block_size)
                if not buffer:
                    break
                file_size_dl += len(buffer)
                local_file.write(buffer)
                status = r"%d of %d KB  [%3.2f%%]" % (file_size_dl/1024, file_size/1024, file_size_dl * 100. / file_size)
                status = status + chr(8)*(len(status)+1)
                print status,

        if os.path.getsize("%s" %local_mp3) == file_size:
            is_downloaded = 1
        else:
            print "\nSomething went wrong, downloaded mp3 is corrupted"

    except:
        print nok_mark
    finally:
        query = ("UPDATE status SET isAudioDownloaded=%s WHERE id='%s'") %(is_downloaded, id)
        sql(query)


def download_cover(id):
    try:
        is_downloaded = 0
        print "Downloading cover #%s" %id,
        data = select("SELECT coverRemote, coverLocal FROM files WHERE id=%s" %id)
        local_cover = downloads_path+data[1]
        remote_cover = urllib2.urlopen(data[0]).read()
        with open(local_cover, 'wb') as local_file:
            local_file.write(remote_cover)
        print ok_mark
        is_downloaded = 1
    except:
        print nok_mark
    finally:
        query = ("UPDATE status SET isCoverDownloaded=%s WHERE id='%s'") %(is_downloaded, id)
        sql(query)


def download(id):
    try:
        # TODO: not good for broken links, need to improve try-except
        download_mp3(id)
        print  # add new line
        download_cover(id)
    except:
        print "No URL found for tale #%s" %id
