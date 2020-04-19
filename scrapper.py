import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.com.mx/Apple-A1474-Wi-Fi-Black-Refurbished/dp/B00M4L4NHY/ref=lp_16880760011_1_1?s=electronics&ie=UTF8&qid=1587317775&sr=1-1'

headers = {"User-agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0"}

page = request.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')
print (soup.prettify())