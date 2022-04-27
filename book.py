from bs4 import BeautifulSoup
import requests
link_list = [
	'http://mpec.sc.mahidol.ac.th/forums/index.php/board,142.0.html',
	'http://mpec.sc.mahidol.ac.th/forums/index.php/board,142.20.html',
	'http://mpec.sc.mahidol.ac.th/forums/index.php/board,142.40.html'
]
for link_main in link_list:
	headers = {
	  'Cookie': 'PHPSESSID=94a230sa7k8htc12du05obct75hjivcg'
	}
	response = requests.request("GET", link_main, headers=headers)
	soup = BeautifulSoup(response.text, 'html.parser')
	i = 1
	for l in soup.find_all("td", {"class": "windowbg"}):
		cx = l.find('a')
		if cx:
			link_html = cx.attrs["href"]
			r = requests.get(link_html)
			ct = str(r.text).replace("src='/forums/Sources/latex/pictures/","src='img/")
			with open('books/' + str(cx.text)+'.html', 'w',encoding='utf-8') as w:
				w.write(ct)
			soupimg = BeautifulSoup(r.text, 'html.parser')
			for ig in soupimg.find_all("img"):
				li = ig.attrs["src"]
				if "/forums/Sources/latex/pictures/" in li:
					link_img = li.replace("http://mpec.sc.mahidol.ac.th","")
					img_name = link_img.replace("/forums/Sources/latex/pictures/","").replace("http://mpec.sc.mahidol.ac.th","")
					src = "http://mpec.sc.mahidol.ac.th"+str(link_img)
					ri = requests.get(src)
					with open('books/img/'+str(img_name), 'wb') as w1:
						w1.write(ri.content)
			i+=1