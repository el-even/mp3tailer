from config import *
from db import *


head = """<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd">
\t<channel>
\t\t<title>Audio Tales</title>
\t\t<description>Good old audiotales in shiny new cover. Enjoy, my little friend :)</description>
\t\t<link>http://mp3tales.info</link>
\t\t<language>ru-ru</language>
\t\t<docs>http://blogs.law.harvard.edu/tech/rss</docs>
\t\t<itunes:author>Powered by mp3tales.info</itunes:author>
\t\t<itunes:image href="http://mp3tales.info/img/sky.png.pagespeed.ce.ppKAjK8Sec.png"/>
"""

bottom = """\t</channel>
</rss>"""

with open("../audiotales_002.xml", 'wb') as test_file:
    test_file.write(head)
    for tale in xrange(0, 999):
        print "Processing tale #%s" %tale,
        query = "SELECT * FROM files WHERE id=%s" %tale
        result = type(select(query))
        # print result

        # replace with try-except later
        if result == tuple:
            test_file.write("\t\t<item>\n")
            title = "\t\t\t<title>%s</title>\n" %select("SELECT title FROM tags WHERE id=%s" %tale)[0]
            description = "\t\t\t<description>%s</description>\n" %select("SELECT description FROM tags WHERE id=%s" %tale)[0]
            # url = "%s?id=%s" %(talesurl, tale)
            link = "\t\t\t<link>%s?id=%s</link>\n" %(talesurl, tale)
            guid = "\t\t\t<guid>%s</guid>\n" %select("SELECT audioRemote FROM files WHERE id=%s" %tale)[0]
            audio = select("SELECT audioRemote, audioLength FROM files WHERE id=%s" %tale)
            enclosure = '\t\t\t<enclosure length="%s" type="audio/mpeg" url="%s" />\n' %(audio[1], audio[0])
            image = '\t\t\t<itunes:image href="%s"/>\n' %select("SELECT coverRemote FROM files WHERE id=%s" %tale)[0]

            test_file.write(title.encode('utf8'))
            test_file.write(description.encode('utf8'))
            test_file.write(link)
            test_file.write(guid)
            test_file.write(enclosure)
            test_file.write(image)

            test_file.write("\t\t\t</item>\n")
            print ok_mark
        else:
            print "-- No data found, skipping"
    test_file.write(bottom)
