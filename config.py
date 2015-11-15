rooturl = "http://mp3tales.info/"
talesurl = rooturl + "tales/"
fetched_path = "../fetched/"
downloads_path = "../files/"
database = "../tales.db"

first_tale = 1
last_tale = 999
max_errors_allowed = 50

ok_mark = "-- Done"
nok_mark = "-- Failed"

re_img_url = '(?s)<div class="row">.*?<img.*?src="/(.*?)"'
re_mp3_url = '<a.*?href="/(.*?)".*?onclick="return clickaudio\(\)".*?>'
re_title = '<h1.*?>(.*?)</h1>'
re_year = "<meta itemprop='dateCreated' content='(.*?)'>"
re_annotation = "(?s)<p>.*?<small>(.*?)</small>"
re_description = '(?s)<p id="description".*?>(.*?)</p>'


failed = []
