import requests
from bs4 import BeautifulSoup

url = "https://play.google.com/store/apps/details?id=com.piano.tiles.music.game.circles.dancing.beat.magictiles"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lift = soup.find('h1', class_="Fd93Bb F5UCq p5VxAd").text
url = "https://play.google.com/store/apps/details?id=com.piano.tiles.music.game.circles.dancing.beat.magictiles"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lift1 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.piano.tiles.music.game.circles.dancing.beat.magictiles"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lift2 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.piano.tiles.music.game.circles.dancing.beat.magictiles"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lift3 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.amanotes.beathopper"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lift4 = soup.find('h1', class_="Fd93Bb F5UCq xwcR9d").text
url = "https://play.google.com/store/apps/details?id=com.amanotes.beathopper"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lift5 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.amanotes.beathopper"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lift6 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.amanotes.beathopper"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lift7 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.joyjourney.PianoWhiteGo"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lift8 = soup.find('h1', class_="Fd93Bb F5UCq p5VxAd").text
url = "https://play.google.com/store/apps/details?id=com.joyjourney.PianoWhiteGo"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lift9 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.joyjourney.PianoWhiteGo"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lift10 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.joyjourney.PianoWhiteGo"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lift11 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.music.game.dancing.hair.beat.race"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lift12 = soup.find('h1', class_="Fd93Bb F5UCq p5VxAd").text
url = "https://play.google.com/store/apps/details?id=com.music.game.dancing.hair.beat.race"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lift13 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.music.game.dancing.hair.beat.race"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lift14 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.music.game.dancing.hair.beat.race"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lift15 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.orange.kidspiano.music.songs"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lift16 = soup.find('h1', class_="Fd93Bb F5UCq p5VxAd").text
url = "https://play.google.com/store/apps/details?id=com.orange.kidspiano.music.songs"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lift17 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.orange.kidspiano.music.songs"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lift18 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.orange.kidspiano.music.songs"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lift19 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=beatmaker.edm.musicgames.PianoGames"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lift20 = soup.find('h1', class_="Fd93Bb F5UCq p5VxAd").text
url = "https://play.google.com/store/apps/details?id=beatmaker.edm.musicgames.PianoGames"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lift21 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=beatmaker.edm.musicgames.PianoGames"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lift22 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=beatmaker.edm.musicgames.PianoGames"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lift23 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.youmusic.magictiles"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lift24 = soup.find('h1', class_="Fd93Bb ynrBgc xwcR9d").text
url = "https://play.google.com/store/apps/details?id=com.youmusic.magictiles"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lift25 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.youmusic.magictiles"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lift26 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.youmusic.magictiles"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lift27 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.bilkon.easypiano"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lift28 = soup.find('h1', class_="Fd93Bb ynrBgc xwcR9d").text
url = "https://play.google.com/store/apps/details?id=com.bilkon.easypiano"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lift29 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.bilkon.easypiano"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lift30 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.bilkon.easypiano"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lift31 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.rhythmdance.taptile.rt"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lift32 = soup.find('h1', class_="Fd93Bb F5UCq p5VxAd").text
url = "https://play.google.com/store/apps/details?id=com.rhythmdance.taptile.rt"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lift33 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.rhythmdance.taptile.rt"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lift34 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.rhythmdance.taptile.rt"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lift35 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.rhythm.games.pink.tiles"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lift36 = soup.find('h1', class_="Fd93Bb F5UCq p5VxAd").text
url = "https://play.google.com/store/apps/details?id=com.rhythm.games.pink.tiles"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lift37 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.rhythm.games.pink.tiles"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lift38 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.rhythm.games.pink.tiles"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lift39 = soup.find('span', itemprop="contentRating").text
