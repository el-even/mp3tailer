import re

from config import *


filename = fetched_path+"49_u.txt"
html = open(filename, 'r').read()

def parser(html):
    img_url = rooturl + re.search('img class="saturate" src="/(.*?)" alt', html).group(1)
    mp3_url = rooturl + re.search('<source src="/(.*)" type="audio/mpeg">', html).group(1)
    title = re.search('<h1 itemprop="name">(.*?)</h1>', html).group(1)
    year = re.search("<meta itemprop='dateCreated' content='(.*?)'>", html).group(1)
    description = re.search('<p id="description"(.|\n)*?>(.*)</p>', html).group(0)

    print img_url
    print mp3_url
    print title
    print year
    print description

parser(html)
