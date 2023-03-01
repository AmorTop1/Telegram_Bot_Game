import requests
from bs4 import BeautifulSoup

url = "https://play.google.com/store/apps/details?id=net.supertreat.solitaire"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lifti = soup.find('h1', class_="Fd93Bb F5UCq xwcR9d").text
url = "https://play.google.com/store/apps/details?id=net.supertreat.solitaire"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lifti1 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=net.supertreat.solitaire"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lifti2 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=net.supertreat.solitaire"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lifti3 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.playtika.wsop.gp"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lifti4 = soup.find('h1', class_="Fd93Bb F5UCq p5VxAd").text
url = "https://play.google.com/store/apps/details?id=com.playtika.wsop.gp"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lifti5 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.playtika.wsop.gp"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lifti6 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.playtika.wsop.gp"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lifti7 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.gsn.android.tripeaks"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lifti8 = soup.find('h1', class_="Fd93Bb F5UCq xwcR9d").text
url = "https://play.google.com/store/apps/details?id=com.gsn.android.tripeaks"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lifti9 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.gsn.android.tripeaks"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lifti10 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.gsn.android.tripeaks"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lifti11 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.mattel163.phase10"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lifti12 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.mattel163.phase10"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lifti13 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.mattel163.phase10"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lifti14 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.zynga.livepoker"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lifti15 = soup.find('h1', class_="Fd93Bb F5UCq p5VxAd").text
url = "https://play.google.com/store/apps/details?id=com.zynga.livepoker"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lifti16 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.zynga.livepoker"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lifti17 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.zynga.livepoker"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lifti18 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=net.peakgames.mobile.spades.android"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lifti19 = soup.find('h1', class_="Fd93Bb F5UCq xwcR9d").text
url = "https://play.google.com/store/apps/details?id=net.peakgames.mobile.spades.android"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lifti20 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=net.peakgames.mobile.spades.android"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lifti21 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=net.peakgames.mobile.spades.android"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lifti22 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.wizards.mtga"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lifti23 = soup.find('h1', class_="Fd93Bb F5UCq p5VxAd").text
url = "https://play.google.com/store/apps/details?id=com.wizards.mtga"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lifti24 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.wizards.mtga"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lifti25 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.wizards.mtga"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lifti26 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.bbumgames.spadesroyale"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lifti27 = soup.find('h1', class_="Fd93Bb F5UCq xwcR9d").text
url = "https://play.google.com/store/apps/details?id=com.bbumgames.spadesroyale"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lifti28 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.bbumgames.spadesroyale"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lifti29 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.bbumgames.spadesroyale"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lifti30 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.island.card"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lifti31 = soup.find('h1', class_="Fd93Bb F5UCq xwcR9d").text
url = "https://play.google.com/store/apps/details?id=com.island.card"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lifti32 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.island.card"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lifti33 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.island.card"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lifti34 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=jp.konami.duellinks"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lifti35 = soup.find('h1', class_="Fd93Bb F5UCq xwcR9d").text
url = "https://play.google.com/store/apps/details?id=jp.konami.duellinks"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lifti36 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=jp.konami.duellinks"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lifti37 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=jp.konami.duellinks"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lifti38 = soup.find('span', itemprop="contentRating").text
