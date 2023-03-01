import requests
from bs4 import BeautifulSoup

url = "https://play.google.com/store/apps/details?id=com.axlebolt.standoff2"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
link = soup.find('h1', class_="Fd93Bb ynrBgc xwcR9d").text
url = "https://play.google.com/store/apps/details?id=com.axlebolt.standoff2"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
link1 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.axlebolt.standoff2"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
link2 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.axlebolt.standoff2"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
link3 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.tencent.ig"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
link4 = soup.find('h1', class_="Fd93Bb ynrBgc xwcR9d").text
url = "https://play.google.com/store/apps/details?id=com.tencent.ig"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
link5 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.tencent.ig"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
link6 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.tencent.ig"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
link7 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.mobile.legends"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
link8 = soup.find('h1', class_="Fd93Bb F5UCq p5VxAd").text
url = "https://play.google.com/store/apps/details?id=com.mobile.legends"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
link9 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.mobile.legends"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
link10 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.mobile.legends"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
link11 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.activision.callofduty.shooter"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
link12 = soup.find('h1', class_="Fd93Bb F5UCq p5VxAd").text
url = "https://play.google.com/store/apps/details?id=com.activision.callofduty.shooter"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
link13 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.activision.callofduty.shooter"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
link14 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.activision.callofduty.shooter"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
link15 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.supercell.brawlstars"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
link16 = soup.find('h1', class_="Fd93Bb ynrBgc xwcR9d").text
url = "https://play.google.com/store/apps/details?id=com.supercell.brawlstars"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
link17 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.supercell.brawlstars"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
link18 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.supercell.brawlstars"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
link19 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.dts.freefireth"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
link20 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.dts.freefireth"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
link21 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.dts.freefireth"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
link22 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.pixonic.wwr"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
link23 = soup.find('h1', class_="Fd93Bb F5UCq p5VxAd").text
url = "https://play.google.com/store/apps/details?id=com.pixonic.wwr"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
link24 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.pixonic.wwr"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
link25 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.pixonic.wwr"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
link26 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.fungames.battletanksbeta"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
link27 = soup.find('h1', class_="Fd93Bb F5UCq p5VxAd").text
url = "https://play.google.com/store/apps/details?id=com.fungames.battletanksbeta"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
link28 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.fungames.battletanksbeta"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
link29 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.fungames.battletanksbeta"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
link30 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.dts.freefiremax"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
link31 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.dts.freefiremax"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
link32 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.dts.freefiremax"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
link33 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=zombie.survival.craft.z"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
link34 = soup.find('h1', class_="Fd93Bb F5UCq p5VxAd").text
url = "https://play.google.com/store/apps/details?id=zombie.survival.craft.z"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
link35 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=zombie.survival.craft.z"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
link36 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=zombie.survival.craft.z"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
link37 = soup.find('span', itemprop="contentRating").text
