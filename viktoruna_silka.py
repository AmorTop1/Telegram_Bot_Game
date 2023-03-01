import requests
from bs4 import BeautifulSoup

url = "https://play.google.com/store/apps/details?id=com.xmonetize.quizzland"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lins = soup.find('h1', class_="Fd93Bb F5UCq p5VxAd").text
url = "https://play.google.com/store/apps/details?id=com.xmonetize.quizzland"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lins1 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.xmonetize.quizzland"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lins2 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.xmonetize.quizzland"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lins3 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.unicostudio.braintest"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lins4 = soup.find('h1', class_="Fd93Bb F5UCq p5VxAd").text
url = "https://play.google.com/store/apps/details?id=com.unicostudio.braintest"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lins5 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.unicostudio.braintest"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lins6 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.unicostudio.braintest"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lins7 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.asmolgam.flags"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lins8 = soup.find('h1', class_="Fd93Bb F5UCq p5VxAd").text
url = "https://play.google.com/store/apps/details?id=com.asmolgam.flags"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lins9 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.asmolgam.flags"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lins10 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.asmolgam.flags"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lins11 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=fun.arts.studio.rotate.baraban"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lins12 = soup.find('h1', class_="Fd93Bb ynrBgc xwcR9d").text
url = "https://play.google.com/store/apps/details?id=fun.arts.studio.rotate.baraban"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lins13 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=fun.arts.studio.rotate.baraban"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lins14 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=fun.arts.studio.rotate.baraban"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lins15 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.nuomondo.millionaire.quiz"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lins16 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.nuomondo.millionaire.quiz"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lins17 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.nuomondo.millionaire.quiz"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lins18 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.whotir.uquiz"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lins19 = soup.find('h1', class_="Fd93Bb F5UCq xwcR9d").text
url = "https://play.google.com/store/apps/details?id=com.whotir.uquiz"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lins20 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.whotir.uquiz"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lins21 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.whotir.uquiz"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lins22 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.submarineapps.mill"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lins23 = soup.find('h1', class_="Fd93Bb F5UCq p5VxAd").text
url = "https://play.google.com/store/apps/details?id=com.submarineapps.mill"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lins24 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.submarineapps.mill"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lins25 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.submarineapps.mill"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lins26 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.RedTower.AFourRoulette"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lins27 = soup.find('h1', class_="Fd93Bb F5UCq xwcR9d").text
url = "https://play.google.com/store/apps/details?id=com.RedTower.AFourRoulette"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lins28 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.RedTower.AFourRoulette"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lins29 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.RedTower.AFourRoulette"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lins30 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=by.panko.wherelogic"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lins31 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=by.panko.wherelogic"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lins32 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=by.panko.wherelogic"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lins33 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.openmygame.games.android.pics"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lins34 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.openmygame.games.android.pics"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lins35 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.openmygame.games.android.pics"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lins36 = soup.find('span', itemprop="contentRating").text
