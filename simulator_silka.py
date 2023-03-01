import requests
from bs4 import BeautifulSoup

url = "https://play.google.com/store/apps/details?id=com.vizorapps.klondike"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
limi = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.vizorapps.klondike"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
limi1 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.vizorapps.klondike"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
limi2 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.tensquaregames.letsfish2"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
limi3 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.tensquaregames.letsfish2"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
limi4 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.tensquaregames.letsfish2"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
limi5 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=progameslab.com.magic.seasons2023.farm.build"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
limi6 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=progameslab.com.magic.seasons2023.farm.build"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
limi7 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=progameslab.com.magic.seasons2023.farm.build"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
limi8 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.yourstoryinteractive.sails.pirate.adventure"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
limi9 = soup.find('h1', class_="Fd93Bb F5UCq p5VxAd").text
url = "https://play.google.com/store/apps/details?id=com.yourstoryinteractive.sails.pirate.adventure"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
limi10 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.yourstoryinteractive.sails.pirate.adventure"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
limi11 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.yourstoryinteractive.sails.pirate.adventure"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
limi12 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.farmadventure.global"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
limi13 = soup.find('h1', class_="Fd93Bb F5UCq xwcR9d").text
url = "https://play.google.com/store/apps/details?id=com.farmadventure.global"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
limi14 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.farmadventure.global"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
limi15 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.farmadventure.global"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
limi16 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.mytona.cookingdiary.android"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
limi17 = soup.find('h1', class_="Fd93Bb F5UCq p5VxAd").text
url = "https://play.google.com/store/apps/details?id=com.mytona.cookingdiary.android"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
limi18 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.mytona.cookingdiary.android"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
limi19 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.mytona.cookingdiary.android"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
limi20 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.redcell.goldandgoblins"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
limi21 = soup.find('h1', class_="Fd93Bb F5UCq p5VxAd").text
url = "https://play.google.com/store/apps/details?id=com.redcell.goldandgoblins"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
limi22 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.redcell.goldandgoblins"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
limi23 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.redcell.goldandgoblins"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
limi24 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.phoenix.game.and.ddj"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
limi25 = soup.find('h1', class_="Fd93Bb ynrBgc xwcR9d").text
url = "https://play.google.com/store/apps/details?id=com.phoenix.game.and.ddj"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
limi26 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.phoenix.game.and.ddj"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
limi27 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.phoenix.game.and.ddj"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
limi28 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.xp101.ava_rus"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
limi29 = soup.find('h1', class_="Fd93Bb F5UCq p5VxAd").text
url = "https://play.google.com/store/apps/details?id=com.xp101.ava_rus"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
limi30 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.xp101.ava_rus"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
limi31 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.xp101.ava_rus"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
limi32 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.olzhas.carparking.multyplayer"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
limi33 = soup.find('h1', class_="Fd93Bb F5UCq xwcR9d").text
url = "https://play.google.com/store/apps/details?id=com.olzhas.carparking.multyplayer"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
limi34 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.olzhas.carparking.multyplayer"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
limi35 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.olzhas.carparking.multyplayer"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
limi36 = soup.find('span', itemprop="contentRating").text
