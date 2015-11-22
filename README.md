# mp3tailer
The script to download and process ye olde soviet mp3 audio tales
For education sake only :)


How to use:
* uncomment all imports in mp3tales.py
* add desired action in it:
* db_init -- create database file
* populate([area]) -- fill database by fetching data; use _xrange(first_tale,last_tale)_ instead of _[area]_ to fetch area
* download(story_id) -- download desired file
* create_podcast() to create xml file
