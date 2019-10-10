import requests
from bs4 import BeautifulSoup
from firebase import firebase
from datetime import datetime
import mail,os,shutil,sys

def add_to_startup():
    user=os.getlogin()
    location = r'C:\Users\{}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup'.format(user)
    filename = 'Pricetrack.exe'
    cwd = os.getcwd()
    shutil.copy2(os.path.join(cwd, filename), location)

def post_to_firebase():
    url = 'https://laptop-prices.firebaseio.com/'
    dt = datetime.now()
    date = dt.strftime('%d-%b-%Y')
    fire = firebase.FirebaseApplication(url,None)
    fire.put('/postdate','date',date)

def check_last_update():
    url = 'https://laptop-prices.firebaseio.com/'
    dt = datetime.now()
    date = dt.strftime('%d-%b-%Y')
    fire = firebase.FirebaseApplication(url,None)
    result = fire.get('/postdate',None)
    if date==result['date']:
        return True
    else:
        return False

def fetch_price(url):
    price = []

    for i in range(2):
        source_code = requests.get(url[i])
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text,'html.parser')
        price.append(soup.find('div',{'class':"_1vC4OE _3qQ9m1"}).getText())
    return price

def main():
    try:
        add_to_startup()
    except:
        pass

    url = [
        'https://www.flipkart.com/acer-predator-helios-300-core-i5-8th-gen-8-gb-1-tb-hdd-128-gb-ssd-windows-10-home-4-graphics-ph315-51-ph315-51-51v7-gaming-laptop/p/itmf5nvpr5xsh2pg?pid=COMF5NVPQAZDMZFB&srno=s_1_1&otracker=AS_QueryStore_HistoryAutoSuggest_2_0&lid=LSTCOMF5NVPQAZDMZFBBVX5AO&fm=SEARCH&iid=6c1c7d2a-ce7d-488e-9d01-14f08c3c0c72.COMF5NVPQAZDMZFB.SEARCH&ppt=Homepage&ppn=Homepage&ssid=9cd5bnztpc0000001543659151767&qH=4aa32b2ea749cb27',
        'https://www.flipkart.com/asus-tuf-core-i5-8th-gen-8-gb-1-tb-hdd-128-gb-ssd-windows-10-home-4-graphics-fx504ge-e4366t-gaming-laptop/p/itmf5g6h6ypz5zhy?pid=COMF5G6HCVMFUMAU&srno=s_1_1&otracker=AS_QueryStore_HistoryAutoSuggest_0_2&lid=LSTCOMF5G6HCVMFUMAUYOJPPW&fm=SEARCH&iid=bac91392-9d7b-46aa-85d0-0d1e25daf3e8.COMF5G6HCVMFUMAU.SEARCH&ppt=SearchPage&ppn=Search&ssid=ct5dsimty80000001543660587324&qH=7ec1d95853ab0b71']

    laptop = ['Acer Predator Helios 300', 'Asus TUF i5 8th Gen']

    if not check_last_update():
        price = fetch_price(url)
        mail.sendMail(laptop, price, url)
        post_to_firebase()
    os._exit(0)

if __name__=='__main__':
    main()
