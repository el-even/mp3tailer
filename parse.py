import re

from config import *
from db import *


def retrieve(pattern, string):
    try:
        result = re.search(pattern, string).group(1)
    except:
        result = ""
    return result


# def typographer2(pattern, substitute, string):
#     result = string.decode("utf-8").replace(pattern, substitute).encode("utf-8")
#     return result


def typographer(pattern, substitute, string):
    string = string.decode("utf-8")
    result = re.sub(pattern, substitute, string).encode("utf-8")
    return result


def strip(text):
    result = re.sub("<span.*?>.*?</span>", "", text) # remove surplus spans
    result = typographer("- ", u"\u2014 ", result) # replace hyphens with emdash
    result = typographer(" -", u" \u2014", result)
    result = typographer(" {4,}", "\n", result)
    result = typographer(" {2,}", " ", result)
    result = re.sub("^\s*|^\n*|\s*$|\n*$|\s*?<br/>", "", result)
    result = typographer(" (\"|\')", u" \xab", result)
    result = typographer("(\"|\') ", u"\xbb ", result) # don't like these similar lines
    result = typographer("(\"|\')\.", u"\xbb.", result)
    
    return result


def parser(id, html):
    print "Parsing tale #%s" %id,
    img_url = rooturl + re.search(re_img_url, html).group(1)
    mp3_url = rooturl + re.search(re_mp3_url, html).group(1)
    tale_name = (mp3_url.split('/')[-1]).split('.')[0]
    title = retrieve(re_title, html)
    year = retrieve(re_year, html)
    # not sure if it is a best way to populate description
    # TODO: investigate further
    description = "%s\n\n%s"\
        %(strip(retrieve(re_annotation, html)),\
            strip(retrieve(re_description, html)))
    # print description
    description = strip(description)
    print ok_mark

    print "Updating database",
    query = ("INSERT OR REPLACE INTO files (id, taleName, mp3URL, coverURL)\
        VALUES ('%s', '%s', '%s', '%s')") %(id, tale_name, mp3_url, img_url)
    sql(query)

    query = ("INSERT OR REPLACE INTO tags (id, title, year, description)\
        VALUES ('%s', '%s', '%s', '%s')") %(id, title, year, description)
    sql(query)

    query = ("INSERT OR REPLACE INTO status (id, isParsed)\
        VALUES ('%s', 1)") %id
    sql(query)
    print ok_mark
