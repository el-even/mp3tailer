import sqlite3

from config import *


con = sqlite3.connect(database)
cur = con.cursor()


def sql(query):
    cur.execute(query)
    con.commit()


def select(query):
    cur.execute(query)
    return cur.fetchone()


def db_init():
    sql("CREATE TABLE IF NOT EXISTS status (id INTEGER PRIMARY KEY, \
        isParsed BOOLEAN,\
        isAudioDownloaded BOOLEAN,\
        isCoverDownloaded BOOLEAN,\
        isTagged BOOLEAN)")
        # TODO: remove isParsed?

    sql("CREATE TABLE IF NOT EXISTS tags (id INTEGER PRIMARY KEY,\
        title TEXT,\
        year INTEGER,\
        description TEXT)")

    sql("CREATE TABLE IF NOT EXISTS files (id INTEGER PRIMARY KEY,\
        audioRemote TEXT,\
        audioLocal TEXT,\
        audioLength INTEGER,\
        coverRemote TEXT,\
        coverLocal TEXT)")
