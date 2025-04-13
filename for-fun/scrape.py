import requests
from bs4 import BeautifulSoup

def dec(func):
    def wrapper():
        print('*' * 40)
        func()
        print('*' * 40)
    return wrapper

def fp(price):
    return "{:,}".format(int(price))

@dec
def dollar():
    response = requests.get("https://www.tgju.org/")
    soup = BeautifulSoup(response.text, 'html.parser')
    prices = soup.find_all('td', class_='market-price')
    dollar_price = prices[0].text.replace(',', '').strip()
    print(f"Dollar price: {fp(dollar_price)} IRR")

@dec
def euro():
    response = requests.get("https://www.tgju.org/")
    soup = BeautifulSoup(response.text, 'html.parser')
    prices = soup.find_all('td', class_='market-price')
    euro_price = prices[1].text.replace(',', '').strip()
    print(f"Euro price: {fp(euro_price)} IRR")

@dec
def pound():
    response = requests.get("https://www.tgju.org/")
    soup = BeautifulSoup(response.text, 'html.parser')
    prices = soup.find_all('td', class_='market-price')
    pound_price = prices[3].text.replace(',', '').strip()
    print(f"Pound price: {fp(pound_price)} IRR")

@dec
def gold():
    response = requests.get("https://www.tgju.org/")
    soup = BeautifulSoup(response.text, 'html.parser')
    prices = soup.find_all('td', class_='nf')
    gold_price = prices[18].text.replace(',', '').strip()
    print(f"Second-hand gold price: {fp(gold_price)} IRR")

while True:
    print("\nSelect an option:")
    print("1) Dollar")
    print("2) Euro")
    print("3) Pound")
    print("4) Second-hand Gold")
    choice = input("==> ")

    if choice == '1':
        dollar()
        break
    elif choice == '2':
        euro()
        break
    elif choice == '3':
        pound()
        break
    elif choice == '4':
        gold()
        break
    else:
        print('\n' * 2 + 'Wrong choice, try again!' + '\n' * 2)
