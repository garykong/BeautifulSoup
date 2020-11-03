	from bs4 import BeautifulSoup
	import requests
	import re
	import math
	
	key = input("검색 키워드를 입력하세요 : ")
	key_search = "http://databasekorea.com/?q=" + key
	temp_r = requests.get(key_search)
	temp_soup = BeautifulSoup(temp_r.text, "html.parser")
	temp = temp_soup.find(class_="page-header")
	item = re.findall("\d+", temp.get_text())
	total_item = (''.join(item))
	page = int(total_item) / 20
	url = []
	r = []
	no = 0
	
	print("업체수 : ",total_item,"/ 페이지 : ", math.ceil(page))
	print("no|업체|전화번호|업종|구주소|신주소|")
	
	for i in range(0,math.ceil(page)):
			url_list = i + 1 
			url.append("http://databasekorea.com/?q=" + key + "&p=" + str(url_list))
			r.append(requests.get(url[i]))
			soup = BeautifulSoup(r[i].text, "html.parser")
			for j in range(0, 20):
				no = no + 1
				add = soup.find_all("address")
				if no > int(total_item) : continue 
				print(int(no),"|",add[j].get_text("|", strip=True))
