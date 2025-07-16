import requests
from bs4 import BeautifulSoup

URL = "http://127.0.0.1:5502/apps/app1.html"

res = requests.get(URL)

soup = BeautifulSoup(res.content,"html.parser")

print(soup.h1.text)