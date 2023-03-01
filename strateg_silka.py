import requests
from bs4 import BeautifulSoup

url = "https://play.google.com/store/apps/details?id=net.wargaming.wot.blitz"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
strateg1 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=net.wargaming.wot.blitz"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
strateg2 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=net.wargaming.wot.blitz"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
strateg3 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.igg.android.lordsmobile"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
strateg4 = soup.find('h1', class_="Fd93Bb F5UCq p5VxAd").text
url = "https://play.google.com/store/apps/details?id=com.igg.android.lordsmobile"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
strateg5 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.igg.android.lordsmobile"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
strateg6 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.igg.android.lordsmobile"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
strateg7 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.hcg.cok.gp"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
strateg8 = soup.find('h1', class_="Fd93Bb ynrBgc xwcR9d").text
url = "https://play.google.com/store/apps/details?id=com.hcg.cok.gp"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
strateg9 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.hcg.cok.gp"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
strateg10 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.hcg.cok.gp"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
strateg11 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.lilithgame.roc.gp"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
strateg12 = soup.find('h1', class_="Fd93Bb F5UCq p5VxAd").text
url = "https://play.google.com/store/apps/details?id=com.lilithgame.roc.gp"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
strateg13 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.lilithgame.roc.gp"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
strateg14 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.lilithgame.roc.gp"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
strateg15 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.kingsgroup.sos"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
strateg16 = soup.find('h1', class_="Fd93Bb F5UCq p5VxAd").text
url = "https://play.google.com/store/apps/details?id=com.kingsgroup.sos"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
strateg17 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.kingsgroup.sos"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
strateg18 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.kingsgroup.sos"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
strateg19 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.plarium.vikings"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
strateg20 = soup.find('h1', class_="Fd93Bb F5UCq p5VxAd").text
url = "https://play.google.com/store/apps/details?id=com.plarium.vikings"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
strateg21 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.plarium.vikings"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
strateg22 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.plarium.vikings"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
strateg23 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.im30.ROE.gp"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
strateg24 = soup.find('h1', class_="Fd93Bb F5UCq p5VxAd").text
url = "https://play.google.com/store/apps/details?id=com.im30.ROE.gp"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
strateg25 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.im30.ROE.gp"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
strateg26 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.im30.ROE.gp"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
strateg27 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.supercell.clashofclans"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
strateg28 = soup.find('h1', class_="Fd93Bb ynrBgc xwcR9d").text
url = "https://play.google.com/store/apps/details?id=com.supercell.clashofclans"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
strateg29 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.supercell.clashofclans"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
strateg30 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.supercell.clashofclans"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
strateg31 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.star.union.planetant"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
strateg32 = soup.find('h1', class_="Fd93Bb F5UCq p5VxAd").text
url = "https://play.google.com/store/apps/details?id=com.star.union.planetant"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
strateg33 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.star.union.planetant"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
strateg34 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.star.union.planetant"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
strateg35 = soup.find('span', itemprop="contentRating").text

url = "https://play.google.com/store/apps/details?id=com.yottagames.mafiawar"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
strateg36 = soup.find('h1', class_="Fd93Bb ynrBgc xwcR9d").text
url = "https://play.google.com/store/apps/details?id=com.yottagames.mafiawar"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
strateg37 = soup.findAll('div', class_="wVqUob")[0].text
url = "https://play.google.com/store/apps/details?id=com.yottagames.mafiawar"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
strateg38 = soup.findAll('div', class_="wVqUob")[1].text
url = "https://play.google.com/store/apps/details?id=com.yottagames.mafiawar"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
strateg39 = soup.find('span', itemprop="contentRating").text
