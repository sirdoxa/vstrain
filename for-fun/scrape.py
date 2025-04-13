import requests
from bs4 import BeautifulSoup

def decorated_output(func):
    def wrapper():
        print('*' * 40)
        func()
        print('*' * 40)
    return wrapper

def format_price(price):
    return "{:,}".format(int(price))

@decorated_output
def dollar():
    response = requests.get("https://www.tgju.org/")
    soup = BeautifulSoup(response.text, 'html.parser')
    prices = soup.find_all('td', class_='market-price')
    dollar_price = prices[0].text.replace(',', '').strip()
    print(f"Dollar price: {format_price(dollar_price)} IRR")

@decorated_output
def euro():
    response = requests.get("https://www.tgju.org/")
    soup = BeautifulSoup(response.text, 'html.parser')
    prices = soup.find_all('td', class_='market-price')
    euro_price = prices[1].text.replace(',', '').strip()
    print(f"Euro price: {format_price(euro_price)} IRR")

@decorated_output
def pound():
    response = requests.get("https://www.tgju.org/")
    soup = BeautifulSoup(response.text, 'html.parser')
    prices = soup.find_all('td', class_='market-price')
    pound_price = prices[3].text.replace(',', '').strip()
    print(f"Pound price: {format_price(pound_price)} IRR")

@decorated_output
def gold():
    response = requests.get("https://www.tgju.org/")
    soup = BeautifulSoup(response.text, 'html.parser')
    prices = soup.find_all('td', class_='nf')
    gold_price = prices[18].text.replace(',', '').strip()
    print(f"Second-hand gold price: {format_price(gold_price)} IRR")

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
