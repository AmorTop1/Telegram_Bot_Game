import requests
from bs4 import BeautifulSoup

url = "https://play.google.com/store/apps/details?id=com.blizzard.diablo.immortal"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
liri = soup.find('h1', class_="Fd93Bb ynrBgc xwcR9d").text
url = "https://play.google.com/store/apps/details?id=com.blizzard.diablo.immortal"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
liri1 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.blizzard.diablo.immortal"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
liri2 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.blizzard.diablo.immortal"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
liri3 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.plarium.raidlegends"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
liri4 = soup.find('h1', class_="Fd93Bb F5UCq xwcR9d").text
url = "https://play.google.com/store/apps/details?id=com.plarium.raidlegends"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
liri5 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.plarium.raidlegends"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
liri6 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.plarium.raidlegends"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
liri7 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.nexters.herowars"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
liri8 = soup.find('h1', class_="Fd93Bb F5UCq p5VxAd").text
url = "https://play.google.com/store/apps/details?id=com.nexters.herowars"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
liri9 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.nexters.herowars"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
liri10 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.nexters.herowars"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
liri11 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.ncsoft.lineage2mru"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
liri12 = soup.find('h1', class_="Fd93Bb ynrBgc xwcR9d").text
url = "https://play.google.com/store/apps/details?id=com.ncsoft.lineage2mru"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
liri13 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.ncsoft.lineage2mru"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
liri14 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.ncsoft.lineage2mru"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
liri15 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.whaleapp.blitz.rise.heroes.idle.rpg.battle"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
liri16 = soup.find('h1', class_="Fd93Bb F5UCq xwcR9d").text
url = "https://play.google.com/store/apps/details?id=com.whaleapp.blitz.rise.heroes.idle.rpg.battle"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
liri17 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.whaleapp.blitz.rise.heroes.idle.rpg.battle"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
liri18 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.whaleapp.blitz.rise.heroes.idle.rpg.battle"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
liri19 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.karma.mythwarspuzzles"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
liri20 = soup.find('h1', class_="Fd93Bb F5UCq p5VxAd").text
url = "https://play.google.com/store/apps/details?id=com.karma.mythwarspuzzles"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
liri21 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.karma.mythwarspuzzles"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
liri22 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.karma.mythwarspuzzles"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
liri23 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.dena.a12026418"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
liri24 = soup.find('h1', class_="Fd93Bb F5UCq xwcR9d").text
url = "https://play.google.com/store/apps/details?id=com.dena.a12026418"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
liri25 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.dena.a12026418"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
liri26 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.dena.a12026418"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
liri27 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=valhalla.survival.craft.z"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
liri28 = soup.find('h1', class_="Fd93Bb F5UCq xwcR9d").text
url = "https://play.google.com/store/apps/details?id=valhalla.survival.craft.z"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
liri29 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=valhalla.survival.craft.z"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
liri30 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=valhalla.survival.craft.z"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
liri31 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.lilithgame.hgame.gp"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
liri32 = soup.find('h1', class_="Fd93Bb ynrBgc xwcR9d").text
url = "https://play.google.com/store/apps/details?id=com.lilithgame.hgame.gp"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
liri33 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.lilithgame.hgame.gp"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
liri34 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.lilithgame.hgame.gp"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
liri35 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.pwrd.pwmru"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
liri36 = soup.find('h1', class_="Fd93Bb F5UCq p5VxAd").text
url = "https://play.google.com/store/apps/details?id=com.pwrd.pwmru"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
liri37 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.pwrd.pwmru"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
liri38 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.pwrd.pwmru"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
liri39 = soup.find('span', itemprop="contentRating").text
