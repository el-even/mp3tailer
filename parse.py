import re
import urllib2

from config import *
from db import *


# wrapper for regexp search
def retrieve(pattern, string):
    try:
        result = re.search(pattern, string).group(1)
    except:
        result = ""
    return result


# wrapper for regexp replace
def typographer(pattern, substitute, string):
    string = string.decode("utf-8")
    result = re.sub(pattern, substitute, string).encode("utf-8")
    return result


# remove obsolete chars or replace them with more typographically-friendly
def strip(text):
    result = re.sub("<span.*?>.*?</span>", "", text) # remove surplus spans
    result = typographer("- ", u"\u2014 ", result) # replace hyphens with emdash
    result = typographer(" -", u" \u2014", result) # replace hyphens with emdash
    result = typographer(" {4,}", "\n", result) # replace 4+ spaces with line break
    result = typographer(" {2,}", " ", result) # replace 2+ spaces with single space

    result = re.sub("^\s*|^\n*|\s*$|\n*$|\s*?<br/>", "", result) # remove obsolete spaces and line breaks

    result = typographer(" (\"|\')", u" \xab", result) # beautify quotes
    result = typographer("(\"|\') ", u"\xbb ", result) # don't like these similar lines
    
    result = typographer("(\"|\')\.", u"\xbb.", result)
    result = typographer("\!(\"|\')", u"!\xbb", result) # I know it looks stupid :(
    result = typographer("(\"|\')\,", u"\xbb,", result)
    result = typographer("\((\"|\')", u"(\xab", result)
    result = typographer("(\"|\')\)", u"\xbb)", result)
    result = typographer("\n(\"|\')", u"\n\xab", result)  # first quote in line
    result = typographer("(\"|\')\n", u"\xbb\n", result)  # final quote in line
    result = typographer("(\"|\')$", u"\xbb", result)  # final quote in line
    
    result = typographer("\'", "''", result)  # if nothing helped, just escape it by doubling
    return result


# mine data -- extract info from html
def parser(id, html):
    print "Parsing tale #%s" %id,
    title = retrieve(re_title, html)
    if title[0:4] != "404.":
        year = retrieve(re_year, html)
        # not sure if it is a best way to populate description
        # TODO: investigate further
        description = "%s\n\n%s"\
            %(strip(retrieve(re_annotation, html)),\
                strip(retrieve(re_description, html)))
        description = strip(description)
        cover_url = rooturl + re.search(re_cover_url, html).group(1)
        mp3_url = rooturl + re.search(re_mp3_url, html).group(1)
        tale_name = (mp3_url.split('/')[-1]).split('.')[0]

        remote_file = urllib2.urlopen(mp3_url)
        meta = remote_file.info()
        mp3_length = int(meta.getheaders("Content-Length")[0])
        cover_name = "%s.%s" %(tale_name, cover_url.split('.')[-1])
        mp3_name = "%s.%s" %(tale_name, mp3_url.split('.')[-1])

        print ok_mark

        # NOT SECURE!
        # TODO: use ? istead of %s
        print "Updating database",
        query = ("INSERT OR REPLACE INTO files (id, audioRemote, audioLocal, audioLength, coverRemote, coverLocal)\
            VALUES ('%s', '%s', '%s', '%s', '%s', '%s')") %(id, mp3_url, mp3_name, mp3_length, cover_url, cover_name)
        sql(query)

        query = ("INSERT OR REPLACE INTO tags (id, title, year, description)\
            VALUES ('%s', '%s', '%s', '%s')") %(id, title, year, description)
        sql(query)

        query = ("INSERT OR REPLACE INTO status (id, isParsed)\
            VALUES ('%s', 1)") %id
        sql(query)
        print ok_mark

    else:
        print "-- Error 404: nothing here, skipping"
