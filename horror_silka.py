import requests
from bs4 import BeautifulSoup

url = "https://play.google.com/store/apps/details?id=com.skytecgames.survival"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
horror1 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.skytecgames.survival"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
horror2 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.skytecgames.survival"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
horror3 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.eyesthegame.eyes"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
horror4 = soup.find('h1', class_="Fd93Bb F5UCq p5VxAd").text
url = "https://play.google.com/store/apps/details?id=com.eyesthegame.eyes"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
horror5 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.eyesthegame.eyes"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
horror6 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.eyesthegame.eyes"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
horror7 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.eg.deathpark"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
horror8 = soup.find('h1', class_="Fd93Bb F5UCq p5VxAd").text
url = "https://play.google.com/store/apps/details?id=com.eg.deathpark"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
horror9 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.eg.deathpark"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
horror10 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.eg.deathpark"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
horror11 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.bhvr.deadbydaylight"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
horror12 = soup.find('h1', class_="Fd93Bb F5UCq xwcR9d").text
url = "https://play.google.com/store/apps/details?id=com.bhvr.deadbydaylight"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
horror13 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.bhvr.deadbydaylight"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
horror14 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.bhvr.deadbydaylight"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
horror15 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.aleson.casefiveanimatronicsfnaf"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
horror16 = soup.find('h1', class_="Fd93Bb F5UCq p5VxAd").text
url = "https://play.google.com/store/apps/details?id=com.aleson.casefiveanimatronicsfnaf"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
horror17 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.aleson.casefiveanimatronicsfnaf"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
horror18 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.aleson.casefiveanimatronicsfnaf"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
horror19 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.freerange.goosebumps"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
horror20 = soup.find('h1', class_="Fd93Bb F5UCq p5VxAd").text
url = "https://play.google.com/store/apps/details?id=com.freerange.goosebumps"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
horror21 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.freerange.goosebumps"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
horror22 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.freerange.goosebumps"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
horror23 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.RaycasterGames.KadabraSurvivalHorror"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
horror24 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.RaycasterGames.KadabraSurvivalHorror"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
horror25 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.RaycasterGames.KadabraSurvivalHorror"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
horror26 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.horrogames.pipehead.scp.survival"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
horror27 = soup.find('h1', class_="Fd93Bb F5UCq p5VxAd").text
url = "https://play.google.com/store/apps/details?id=com.horrogames.pipehead.scp.survival"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
horror28 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.horrogames.pipehead.scp.survival"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
horror29 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.horrogames.pipehead.scp.survival"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
horror30 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.escapehorrorgames.houseoffear3d2"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
horror31 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.escapehorrorgames.houseoffear3d2"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
horror32 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.escapehorrorgames.houseoffear3d2"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
horror33 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=io.horror.show"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
horror34 = soup.find('h1', class_="Fd93Bb F5UCq p5VxAd").text
url = "https://play.google.com/store/apps/details?id=io.horror.show"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
horror35 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=io.horror.show"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
horror36 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=io.horror.show"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
horror37 = soup.find('span', itemprop="contentRating").text
