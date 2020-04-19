import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.com.mx/Apple-A1474-Wi-Fi-Black-Refurbished/dp/B00M4L4NHY/ref=lp_16880760011_1_1?s=electronics&ie=UTF8&qid=1587317775&sr=1-1'

headers = {"User-agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0"}

def check_price():

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id='productTitle').getText()
    price = soup.find(id='price').getText()

    converted_price = float(price[13:18])
    if(converted_price  < 1700):
        send_mail()

    print ("El precio es: " + price.strip())
    print ("El precio convertido es: " + converted_price.strip())
    print ("El titulo del producto es: "+ title.strip())
def send_mail():
    