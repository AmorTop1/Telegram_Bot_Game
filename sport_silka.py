import requests
from bs4 import BeautifulSoup

url = "https://play.google.com/store/apps/details?id=com.ea.gp.fifamobile"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
sport1 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.ea.gp.fifamobile"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
sport2 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.ea.gp.fifamobile"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
sport3 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=jp.konami.pesam"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
sport4 = soup.find('h1', class_="Fd93Bb ynrBgc xwcR9d").text
url = "https://play.google.com/store/apps/details?id=jp.konami.pesam"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
sport5 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=jp.konami.pesam"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
sport6 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=jp.konami.pesam"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
sport7 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=eu.nordeus.topeleven.android"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
sport8 = soup.find('h1', class_="Fd93Bb F5UCq p5VxAd").text
url = "https://play.google.com/store/apps/details?id=eu.nordeus.topeleven.android"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
sport9 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=eu.nordeus.topeleven.android"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
sport10 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=eu.nordeus.topeleven.android"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
sport11 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.miniclip.eightballpool"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
sport12 = soup.find('h1', class_="Fd93Bb ynrBgc xwcR9d").text
url = "https://play.google.com/store/apps/details?id=com.miniclip.eightballpool"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
sport13 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.miniclip.eightballpool"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
sport14 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.miniclip.eightballpool"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
sport15 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.firsttouchgames.dls7"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
sport16 = soup.find('h1', class_="Fd93Bb F5UCq xwcR9d").text
url = "https://play.google.com/store/apps/details?id=com.firsttouchgames.dls7"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
sport17 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.firsttouchgames.dls7"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
sport18 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.firsttouchgames.dls7"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
sport19 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.greenhorsegames.footballrivals"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
sport20 = soup.find('h1', class_="Fd93Bb F5UCq p5VxAd").text
url = "https://play.google.com/store/apps/details?id=com.greenhorsegames.footballrivals"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
sport21 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.greenhorsegames.footballrivals"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
sport22 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.greenhorsegames.footballrivals"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
sport23 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.ea.gp.fifaultimate"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
sport24 = soup.find('h1', class_="Fd93Bb F5UCq p5VxAd").text
url = "https://play.google.com/store/apps/details?id=com.ea.gp.fifaultimate"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
sport25 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.ea.gp.fifaultimate"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
sport26 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.ea.gp.fifaultimate"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
sport27 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.tfgco.games.sports.free.tennis.clash"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
sport28 = soup.find('h1', class_="Fd93Bb F5UCq p5VxAd").text
url = "https://play.google.com/store/apps/details?id=com.tfgco.games.sports.free.tennis.clash"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
sport29 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.tfgco.games.sports.free.tennis.clash"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
sport30 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.tfgco.games.sports.free.tennis.clash"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
sport31 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.miniclip.footballstrike"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
sport32 = soup.find('h1', class_="Fd93Bb F5UCq p5VxAd").text
url = "https://play.google.com/store/apps/details?id=com.miniclip.footballstrike"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
sport33 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.miniclip.footballstrike"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
sport34 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.miniclip.footballstrike"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
sport35 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.masomo.headball2"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
sport36 = soup.find('h1', class_="Fd93Bb F5UCq p5VxAd").text
url = "https://play.google.com/store/apps/details?id=com.masomo.headball2"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
sport37 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.masomo.headball2"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
sport38 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.masomo.headball2"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
sport39 = soup.find('span', itemprop="contentRating").text
