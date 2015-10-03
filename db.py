import sqlite3

from config import *


con = sqlite3.connect(database)
cur = con.cursor()


def sql(query):
    cur.execute(query)
    con.commit()


def db_init():
    sql("CREATE TABLE IF NOT EXISTS status (id INTEGER PRIMARY KEY, \
        isFetched BOOLEAN,\
        isDownloaded BOOLEAN,\
        isTagged BOOLEAN)")

    sql("CREATE TABLE IF NOT EXISTS tags (id INTEGER PRIMARY KEY,\
        title TEXT,\
        author TEXT,\
        year INTEGER,\
        description TEXT)")

    sql("CREATE TABLE IF NOT EXISTS remote_files (id INTEGER PRIMARY KEY,\
        mp3URL TEXT,\
        coverURL TEXT)")
