import re

from config import *
from db import *


def strip(text):
    return re.sub("^\s*|^\n*|\s*$|\n*$|\s*?<br/>", "", text)

def parser(id, html):
    img_url = rooturl + re.search(re_img_url, html).group(1)
    mp3_url = rooturl + re.search(re_mp3_url, html).group(1)
    tale_name = (mp3_url.split('/')[-1]).split('.')[0]
    title = re.search(re_title, html).group(1)
    year = re.search(re_year, html).group(1)
    description = strip(re.search(re_annotation, html).group(1))
    if len(description) !=0:
        description += "\n\n"
    description += strip(re.search(re_description, html).group(1))
    description = strip(description)

    query = ("INSERT OR REPLACE INTO files (id, taleName, mp3URL, coverURL)\
        VALUES ('%s', '%s', '%s', '%s')") %(id, tale_name, mp3_url, img_url)
    sql(query)

    query = ("INSERT OR REPLACE INTO tags (id, title, year, description)\
        VALUES ('%s', '%s', '%s', '%s')") %(id, title, year, description)
    sql(query)

    query = ("INSERT OR REPLACE INTO status (id, isParsed)\
        VALUES ('%s', 1)") %id
    sql(query)


filename = fetched_path+"1_u.txt"
html = open(filename, 'r').read()
parser(1, html)
