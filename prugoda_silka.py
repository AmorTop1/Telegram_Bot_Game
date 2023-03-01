import requests
from bs4 import BeautifulSoup

url = "https://play.google.com/store/apps/details?id=com.roblox.client"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lifi1 = soup.find('h1', class_="Fd93Bb ynrBgc xwcR9d").text
url = "https://play.google.com/store/apps/details?id=com.roblox.client"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lifi2 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.roblox.client"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lifi3 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.roblox.client"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lifi4 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.miHoYo.GenshinImpact"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lifi5 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.miHoYo.GenshinImpact"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lifi6 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.miHoYo.GenshinImpact"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lifi7 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.xdg.and.eu.lifeafter"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lifi8 = soup.find('h1', class_="Fd93Bb F5UCq xwcR9d").text
url = "https://play.google.com/store/apps/details?id=com.xdg.and.eu.lifeafter"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lifi9 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.xdg.and.eu.lifeafter"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lifi10 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.xdg.and.eu.lifeafter"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lifi11 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=net.wooga.junes_journey_hidden_object_mystery_game"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lifi12 = soup.find('h1', class_="Fd93Bb F5UCq p5VxAd").text
url = "https://play.google.com/store/apps/details?id=net.wooga.junes_journey_hidden_object_mystery_game"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lifi13 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=net.wooga.junes_journey_hidden_object_mystery_game"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lifi14 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=net.wooga.junes_journey_hidden_object_mystery_game"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lifi15 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.dxx.firenow"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lifi16 = soup.find('h1', class_="Fd93Bb ynrBgc xwcR9d").text
url = "https://play.google.com/store/apps/details?id=com.dxx.firenow"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lifi17 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.dxx.firenow"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lifi18 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.dxx.firenow"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lifi19 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.playrix.manormatters"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lifi20 = soup.find('h1', class_="Fd93Bb ynrBgc xwcR9d").text
url = "https://play.google.com/store/apps/details?id=com.playrix.manormatters"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lifi21 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.playrix.manormatters"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lifi22 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.playrix.manormatters"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lifi23 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.gameloft.android.ANMP.GloftDOHM"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lifi24 = soup.find('h1', class_="Fd93Bb F5UCq xwcR9d").text
url = "https://play.google.com/store/apps/details?id=com.gameloft.android.ANMP.GloftDOHM"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lifi25 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.gameloft.android.ANMP.GloftDOHM"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lifi26 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.gameloft.android.ANMP.GloftDOHM"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lifi27 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=net.wapsmskey.mrush"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lifi28 = soup.find('h1', class_="Fd93Bb ynrBgc xwcR9d").text
url = "https://play.google.com/store/apps/details?id=net.wapsmskey.mrush"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lifi29 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=net.wapsmskey.mrush"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lifi30 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=net.wapsmskey.mrush"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lifi31 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.fivebn.ll8.f2p"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lifi32 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.fivebn.ll8.f2p"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lifi33 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.fivebn.ll8.f2p"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lifi34 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.heliogames.westland"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lifi35 = soup.find('h1', class_="Fd93Bb F5UCq p5VxAd").text
url = "https://play.google.com/store/apps/details?id=com.heliogames.westland"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lifi36 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.heliogames.westland"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lifi37 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.heliogames.westland"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lifi38 = soup.find('span', itemprop="contentRating").text
