from urllib.request import urlopen  # b_soup_1.py
from bs4 import BeautifulSoup

html = urlopen('https://www.foodsafety.gov/keep-food-safe/foodkeeper-app')

bsyc = BeautifulSoup(html.read(), "lxml")

fout = open('foodkeep.txt', 'wt', encoding='utf-8')

fout.write(str(bsyc))

fout.close()
app = bsyc.main.article.div.div.div.div
print(app)