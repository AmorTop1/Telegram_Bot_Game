import requests
from bs4 import BeautifulSoup

url = "https://play.google.com/store/apps/details?id=com.naturalmotion.customstreetracer2"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lafa1 = soup.find('h1', class_="Fd93Bb F5UCq p5VxAd").text
url = "https://play.google.com/store/apps/details?id=com.naturalmotion.customstreetracer2"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lafa2 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.naturalmotion.customstreetracer2"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lafa3 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.naturalmotion.customstreetracer2"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lafa4 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.ea.game.nfs14_row"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lafa5 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.ea.game.nfs14_row"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lafa6 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.ea.game.nfs14_row"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lafa7 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.gameloft.android.ANMP.GloftA9HM"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lafa8 = soup.find('h1', class_="Fd93Bb F5UCq xwcR9d").text
url = "https://play.google.com/store/apps/details?id=com.gameloft.android.ANMP.GloftA9HM"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lafa9 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.gameloft.android.ANMP.GloftA9HM"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lafa10 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.gameloft.android.ANMP.GloftA9HM"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lafa11 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.fingersoft.hcr2"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lafa12 = soup.find('h1', class_="Fd93Bb F5UCq xwcR9d").text
url = "https://play.google.com/store/apps/details?id=com.fingersoft.hcr2"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lafa13 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.fingersoft.hcr2"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lafa14 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.fingersoft.hcr2"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lafa15 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.battlecreek.nolimit2"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lafa16 = soup.find('h1', class_="Fd93Bb F5UCq xwcR9d").text
url = "https://play.google.com/store/apps/details?id=com.battlecreek.nolimit2"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lafa17 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.battlecreek.nolimit2"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lafa18 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.battlecreek.nolimit2"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lafa19 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.hutchgames.cccg"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lafa20 = soup.find('h1', class_="Fd93Bb F5UCq p5VxAd").text
url = "https://play.google.com/store/apps/details?id=com.hutchgames.cccg"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lafa21 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.hutchgames.cccg"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lafa22 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.hutchgames.cccg"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lafa23 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.battlecreek.offroadoutlaws"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lafa24 = soup.find('h1', class_="Fd93Bb ynrBgc xwcR9d").text
url = "https://play.google.com/store/apps/details?id=com.battlecreek.offroadoutlaws"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lafa25 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.battlecreek.offroadoutlaws"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lafa26 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.battlecreek.offroadoutlaws"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lafa27 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.ea.games.r3_na"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lafa28 = soup.find('h1', class_="Fd93Bb ynrBgc xwcR9d").text
url = "https://play.google.com/store/apps/details?id=com.ea.games.r3_na"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lafa29 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.ea.games.r3_na"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lafa30 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.ea.games.r3_na"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lafa31 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.hutchgames.formularacing"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lafa32 = soup.find('h1', class_="Fd93Bb F5UCq p5VxAd").text
url = "https://play.google.com/store/apps/details?id=com.hutchgames.formularacing"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lafa33 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.hutchgames.formularacing"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lafa34 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.hutchgames.formularacing"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lafa35 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.creativemobile.nno"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lafa36 = soup.find('h1', class_="Fd93Bb F5UCq p5VxAd").text
url = "https://play.google.com/store/apps/details?id=com.creativemobile.nno"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lafa37 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.creativemobile.nno"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lafa38 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.creativemobile.nno"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lafa39 = soup.find('span', itemprop="contentRating").text
