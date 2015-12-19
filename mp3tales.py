# The main runner. Place desired operations sequence here
from Tkinter import *
import ttk

from download import *
from db import *
from fetch import *
from parse import *
from podcast import *


# gets items to fetch from UI and fetches them
def get_fetch():
    try:
        fetch_from =  int(first_item.get())
        fetch_to = int(last_item.get()) + 1
        populate(xrange(fetch_from,fetch_to))
    except:
        print "illegal FETCH numbers"


# gets items to download from UI and downloads them
def get_download():
    try:
        dl_from =  int(first_item.get())
        dl_to = int(last_item.get()) + 1
        for item in xrange(dl_from, dl_to):
            print item
            download(item)
    except:
        print "illegal DL numbers"


root = Tk()

ttk.Button(root, text="Initailize database", command=lambda: db_init()).grid(row=0, column=0, columnspan=2, padx=5, pady=10)

ttk.Label(root, text="First").grid(row=1, column=0, sticky=W, padx=5)
ttk.Label(root, text="Last").grid(row=1, column=1, sticky=W, padx=5)
first_item = ttk.Entry(root, width=8, cursor="ibeam")
last_item = ttk.Entry(root, width=8, cursor="ibeam")
first_item.grid(row=2, column=0, sticky=W, padx=5)
last_item.grid(row=2, column=1, sticky=W, padx=5)
ttk.Button(root, text="Fetch", command=lambda: get_fetch()).grid(row=3, column=0, columnspan=2, padx=5, pady=10)

ttk.Button(root, text="Download", command=lambda: get_download()).grid(row=4, column=0, columnspan=2, padx=5)

ttk.Button(root, text="Generate podcast file", command=lambda: create_podcast()).grid(row=5, column=0, columnspan=2, padx=5, pady=10)

root.iconbitmap("icon.ico")
root.title("mp3tailer")
root.mainloop()


# db_init()
# populate(xrange(first_tale,last_tale))
# download(43)
# create_podcast()
