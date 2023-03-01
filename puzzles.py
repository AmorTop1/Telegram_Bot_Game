import requests
from bs4 import BeautifulSoup

url = "https://play.google.com/store/apps/details?id=com.smallgiantgames.empires"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lina = soup.find('h1', class_="Fd93Bb F5UCq p5VxAd").text
url = "https://play.google.com/store/apps/details?id=com.smallgiantgames.empires"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lina1 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.smallgiantgames.empires"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lina2 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.smallgiantgames.empires"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lina3 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.playrix.fishdomdd.gplay"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lina4 = soup.find('h1', class_="Fd93Bb ynrBgc xwcR9d").text
url = "https://play.google.com/store/apps/details?id=com.playrix.fishdomdd.gplay"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lina5 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.playrix.fishdomdd.gplay"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lina6 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.playrix.fishdomdd.gplay"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lina7 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.dreamgames.royalmatch"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lina8 = soup.find('h1', class_="Fd93Bb ynrBgc xwcR9d").text
url = "https://play.google.com/store/apps/details?id=com.dreamgames.royalmatch"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lina9 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.dreamgames.royalmatch"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lina10 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.dreamgames.royalmatch"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lina11 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.everywear.game5"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lina12 = soup.find('h1', class_="Fd93Bb ynrBgc xwcR9d").text
url = "https://play.google.com/store/apps/details?id=com.everywear.game5"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lina13 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.everywear.game5"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lina14 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.everywear.game5"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lina15 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.gramgames.mergedragons"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lina16 = soup.find('h1', class_="Fd93Bb ynrBgc xwcR9d").text
url = "https://play.google.com/store/apps/details?id=com.gramgames.mergedragons"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lina17 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.gramgames.mergedragons"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lina18 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.gramgames.mergedragons"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lina19 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.bigfishgames.mergetalesgoog"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lina20 = soup.find('h1', class_="Fd93Bb F5UCq p5VxAd").text
url = "https://play.google.com/store/apps/details?id=com.bigfishgames.mergetalesgoog"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lina21 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.bigfishgames.mergetalesgoog"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lina22 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.bigfishgames.mergetalesgoog"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lina23 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.belkatechnologies.clockmaker"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lina24 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.belkatechnologies.clockmaker"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lina25 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.belkatechnologies.clockmaker"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lina26 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.zynga.pottermatch"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lina27 = soup.find('h1', class_="Fd93Bb F5UCq p5VxAd").text
url = "https://play.google.com/store/apps/details?id=com.zynga.pottermatch"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lina28 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.zynga.pottermatch"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lina29 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.zynga.pottermatch"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lina30 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.rovio.dream"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lina31 = soup.find('h1', class_="Fd93Bb F5UCq xwcR9d").text
url = "https://play.google.com/store/apps/details?id=com.rovio.dream"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lina32 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.rovio.dream"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lina33 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.rovio.dream"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lina34 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.orangeapps.piratetreasure"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lina35 = soup.find('h1', class_="Fd93Bb F5UCq p5VxAd").text
url = "https://play.google.com/store/apps/details?id=com.orangeapps.piratetreasure"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lina36 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.orangeapps.piratetreasure"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lina37 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.orangeapps.piratetreasure"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lina38 = soup.find('span', itemprop="contentRating").text
