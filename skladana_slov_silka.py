import requests
from bs4 import BeautifulSoup

url = "https://play.google.com/store/apps/details?id=com.fugo.wow"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lirti = soup.find('h1', class_="Fd93Bb F5UCq p5VxAd").text
url = "https://play.google.com/store/apps/details?id=com.fugo.wow"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lirti1 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.fugo.wow"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lirti2 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.fugo.wow"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lirti3 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.zynga.words3"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lirti4 = soup.find('h1', class_="Fd93Bb F5UCq p5VxAd").text
url = "https://play.google.com/store/apps/details?id=com.zynga.words3"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lirti5 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.zynga.words3"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lirti6 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.zynga.words3"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lirti7 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.peoplefun.wordcross"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lirti8 = soup.find('h1', class_="Fd93Bb ynrBgc xwcR9d").text
url = "https://play.google.com/store/apps/details?id=com.peoplefun.wordcross"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lirti9 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.peoplefun.wordcross"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lirti10 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.peoplefun.wordcross"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lirti11 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=in.playsimple.wordtrip"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lirti12 = soup.find('h1', class_="Fd93Bb ynrBgc xwcR9d").text
url = "https://play.google.com/store/apps/details?id=in.playsimple.wordtrip"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lirti13 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=in.playsimple.wordtrip"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lirti14 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=in.playsimple.wordtrip"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lirti15 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=in.playsimple.tripcross"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lirti16 = soup.find('h1', class_="Fd93Bb ynrBgc xwcR9d").text
url = "https://play.google.com/store/apps/details?id=in.playsimple.tripcross"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lirti17 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=in.playsimple.tripcross"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lirti18 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=in.playsimple.tripcross"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lirti19 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.bitmango.go.wordcookies"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lirti20 = soup.find('h1', class_="Fd93Bb ynrBgc xwcR9d").text
url = "https://play.google.com/store/apps/details?id=com.bitmango.go.wordcookies"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lirti21 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.bitmango.go.wordcookies"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lirti22 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.bitmango.go.wordcookies"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lirti23 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.scopely.wheeloffortune"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lirti24 = soup.find('h1', class_="Fd93Bb F5UCq p5VxAd").text
url = "https://play.google.com/store/apps/details?id=com.scopely.wheeloffortune"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lirti25 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.scopely.wheeloffortune"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lirti26 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.scopely.wheeloffortune"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lirti27 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.wordgame.words.connect"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lirti28 = soup.find('h1', class_="Fd93Bb ynrBgc xwcR9d").text
url = "https://play.google.com/store/apps/details?id=com.wordgame.words.connect"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lirti29 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.wordgame.words.connect"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lirti30 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.wordgame.words.connect"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lirti31 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.nytimes.crossword"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lirti32 = soup.find('h1', class_="Fd93Bb F5UCq p5VxAd").text
url = "https://play.google.com/store/apps/details?id=com.nytimes.crossword"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lirti33 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.nytimes.crossword"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lirti34 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.nytimes.crossword"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lirti35 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.pieyel.scrabble"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lirti36 = soup.find('h1', class_="Fd93Bb F5UCq p5VxAd").text
url = "https://play.google.com/store/apps/details?id=com.pieyel.scrabble"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lirti37 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.pieyel.scrabble"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lirti38 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.pieyel.scrabble"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lirti39 = soup.find('span', itemprop="contentRating").text
