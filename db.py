import sqlite3

from config import *


con = sqlite3.connect(database)
cur = con.cursor()


def sql(query):
    cur.execute(query)
    con.commit()


def select(query):
    cur.execute(query)
    return cur.fetchone()[0]


def db_init():
    sql("CREATE TABLE IF NOT EXISTS status (id INTEGER PRIMARY KEY, \
        isParsed BOOLEAN,\
        isDownloaded BOOLEAN,\
        isTagged BOOLEAN)")

    sql("CREATE TABLE IF NOT EXISTS tags (id INTEGER PRIMARY KEY,\
        title TEXT,\
        year INTEGER,\
        description TEXT)")

    sql("CREATE TABLE IF NOT EXISTS files (id INTEGER PRIMARY KEY,\
        taleName TEXT,\
        mp3URL TEXT,\
        coverURL TEXT)")
