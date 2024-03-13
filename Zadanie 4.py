# Pomóż szwajcarskiemu bankowi HSBC tworząc aplikację, która odczytuje i analizuje dane z Narodowego Banku Polskiego (NBP) udostępnione przez API i podaje ile była warta wskazana waluta we wskazanym dniu.

# Dzięki Tobie HSBC będzie mógł poprawnie wystawiać w Polsce faktury w walucie obcej - przepisy wymagają, aby kwoty na takich fakturach przeliczać na złotówki wg kursów NBP z określonych dni.

# 1. Zapoznaj się z opisem API: http://api.nbp.pl.
#    1. Ustal jak wygląda URL, pod którym znajdziesz kurs danej waluty z danego dnia?
#    2. W jakim formacie musi być data?
#    3. Co trzeba zmienić w URLu, aby otrzymać odpowiedź w JSONie zamiast XMLu?
# 2. Tabele kursów są publikowane tylko w dni robocze. Przeczytaj w dokumentacji co się stanie, gdy zapytasz o kurs z weekendu lub innego dnia wolnego od pracy?
# 3. Twój program przyjmuje walutę oraz datę jako dwa argumenty wiersza poleceń. Jeśli jednak nie zostaną podane, wówczas poproś użytkownika o podanie tych dwóch informacji przy pomocy funkcji input.

import requests
import sys
from dateutil import parser
import json

#Podaj dane
try:
    currency = sys.argv[1]
    date = sys.argv[2]
except IndexError:
    currency = input("Podaj skrót waluty która cię interesuje:")
    date = input("Podaj datę z jakiej interesuje cię dany kurs: ")

#Konwerter daty
try:
    date_object = parser.parse(date)
    # print('date_object:', date_object)
    formatted_date = date_object.strftime("%Y-%m-%d")
    # print(formatted_date)

except ValueError:
    print("Nieprawidłowy format daty.")

#Pobieranie API
try:
    URL = r"http://api.nbp.pl/api/exchangerates/rates/a/" + currency.lower() + "/" + formatted_date + "/?format=json"
    resp = requests.get(URL)
    resp = resp.json()
    currency_format = resp['rates'][0]['mid']
    date_foramt = resp['rates'][0]['effectiveDate']
    print("Data: ", date_foramt)
    print("Kurs: ", currency_format)
except requests.exceptions.JSONDecodeError:
    print("Waluta nie została pobrana z serwisu, sprawdź datę lub walutę.")
