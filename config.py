rooturl = "http://mp3tales.info/"
talesurl = rooturl + "tales/"
fetched_path = "../fetched/"
downloads_path = "../files/"
database = "../tales.db"

first_tale = 265
last_tale = 267
max_errors_allowed = 50

ok_mark = "-- ok"

re_img_url = '(?s)<div class="row">.*?<img.*?src="/(.*?)"'
re_mp3_url = '<source src="/(.*)" type="audio/mpeg">'
re_title = '<h1 itemprop="name">(.*?)</h1>'
re_year = "<meta itemprop='dateCreated' content='(.*?)'>"
re_annotation = "(?s)<p>.*?<small>(.*?)</small>"
re_description = '(?s)<p id="description".*?>(.*?)</p>'


failed = [50, 99, 133, 148,\
    257, 325, 326,\
    404, 450, 493, 580, 582, 598,\
    669, 699, 713, 798,\
    899, 929]
