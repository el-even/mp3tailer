# from download import *
from db import *
from fetch import *
from parse import *


def body():
    errors_counter = 0
    for id in xrange(first_tale, last_tale+1):
        url = "%s?id=%s" %(talesurl, id)
        try:
            html = fetcher(url)
            parser(id, html)
        except:
            errors_counter += 1
            print "\n[ ! ] Looks like something is wrong with tale #%s. %s error(s) so far" %(id, errors_counter)
        if errors_counter >= max_errors_allowed:
            print "Too many errors, aborting."
            break


db_init()
body()
