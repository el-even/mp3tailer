# from download import *
from db import *
from fetch import *
from parse import *


def body():
    errors_counter = 0
    failed_tales = []
    for id in [293]:
        url = "%s?id=%s" %(talesurl, id)
        try:
            html = fetcher(url)
            parser(id, html)
        except:
            errors_counter += 1
            failed_tales.append(id)
            print "\n[ ! ] Looks like something is wrong with tale #%s. %s error(s) so far" %(id, errors_counter)
        if errors_counter >= max_errors_allowed:
            print "Too many errors, aborting."
            break
    if errors_counter > 0:
        print "Failed tales: %s" %failed_tales

db_init()
body()
