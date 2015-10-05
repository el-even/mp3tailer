import re

from config import *


filename = fetched_path+"48_u.txt"
html = open(filename, 'r').read()


def strip(text):
    return re.sub("^\s*|\s*$|\s*?<br/>", "", text)

def parser(html):
    img_url = rooturl + re.search(re_img_url, html).group(1)
    mp3_url = rooturl + re.search(re_mp3_url, html).group(1)
    title = re.search(re_title, html).group(1)
    year = re.search(re_year, html).group(1)
    annotation = strip(re.search(re_annotation, html).group(1))
    description = strip(re.search(re_description, html).group(1))


    print img_url
    print mp3_url
    print title
    print year
    print annotation
    print description

parser(html)
