from bs4 import BeautifulSoup
import requests

answer = 0
print("Привіт друже що будемо майнити")


def question():
    a = 1
    while a == 1:
        answer = int(input("1)Біткоїн, 2) Ефїрїум, 3) Солан : "))
        if (answer == 1 or answer == 2 or answer == 3):
            a = 0

        if answer == 1:
            response = requests.get("https://coinmarketcap.com/")

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, features="html.parser")
                soup_list = soup.find_all("a", {"href": "/currencies/bitcoin/markets/"})
                res = soup_list[0].find("span")
                m = print(res.text)

        if answer == 2:
            response = requests.get("https://coinmarketcap.com/")

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, features="html.parser")
                soup_list = soup.find_all("a", {"href": "/currencies/ethereum/markets/"})
                res = soup_list[0].find("span")
                n = print(res.text)

        if answer == 3:
            response = requests.get("https://coinmarketcap.com/")

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, features="html.parser")
                soup_list = soup.find_all("a", {"href": "/currencies/solana/markets/"})
                res = soup_list[0].find("span")
                v = print(res.text)

    answer2 = int(input("що хочете зробити? 1)Завершити,2)порахувати валюту: "))
    c = 1
    while c == 1:
        if answer2 == 1:
            c = 0
            return
        if answer2 == 2:
            c = 0
            print("Сорі я невстиг зробити!")

    """if answer2 == 2 and answer == 1:
      how = int(input("Скільки ти маеш Біткоїну?: "))
      print(how * int(m))
    if answer2 == 2 and answer == 2:
      how = int(input("Скільки ти маеш Ефіріум?: "))
      print(how * int(n))
    if answer2 == 2 and answer == 3:
      how = int(input("Скільки ти маеш Солана?: "))
      print(how * int(v))"""


question()