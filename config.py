rooturl = "http://mp3tales.info/"
talesurl = rooturl + "tales/"
fetched_path = "../fetched/"
downloads_path = "../files/"
database = "../tales.db"
first = 48
last = 49

re_img_url = 'img class="saturate" src="/(.*?)" alt'
re_mp3_url = '<source src="/(.*)" type="audio/mpeg">'
re_title = '<h1 itemprop="name">(.*?)</h1>'
re_year = "<meta itemprop='dateCreated' content='(.*?)'>"
re_annotation = "(?s)<p>.*?<small>(.*?)</small>"
re_description = '(?s)<p id="description".*?>(.*?)</p>'
