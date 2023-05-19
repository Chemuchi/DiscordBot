from urllib.request import urlopen

import asdf as asdf
from bs4 import BeautifulSoup

asdf = urlopen("https://hangang.ivlis.kr/")
bsObject = BeautifulSoup(asdf, "html.parser")

print(bsObject)