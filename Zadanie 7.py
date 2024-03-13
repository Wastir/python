# Napisz program, który ułatwi milionom Polaków śledzenie własnych wydatków oraz ich analizę. Program pozwala na łatwe dodawanie nowych wydatków i generowanie raportów. Aplikacja działa także pomiędzy uruchomieniami, przechowując wszystkie dane w pliku. Każdy wydatek ma id, opis oraz wielkość kwoty.

# 1. Program posiada podkomendy add, report, export-python oraz import-csv. 

# 2. Podkomenda add pozwala na dodanie nowego wydatku. Należy wówczas podać jako kolejne argumenty wiersza poleceń wielkość wydatku (jako int) oraz jego opis (w cudzysłowach). Na przykład:
# $ python budget.py add 100 "stówa na zakupy". 
# Jako id wybierz pierwszy wolny id - np. jeśli masz już wydatki z id = 1, 2, 4, 5, wówczas wybierz id = 3.

# 3. Podkomenda report wyświetla wszystkie wydatki w tabeli. W tabeli znajduje się także kolumna "big?", w której znajduje się ptaszek, gdy wydatek jest duży, tzn. co najmniej 1000. Dodatkowo, na samym końcu wyświetlona jest suma wszystkich wydatów.

# 4. Podkomenda export-python wyświetla listę wszystkich wydatków jako obiekt (hint: zaimplementuj poprawnie metodę __repr__ w klasie reprezentującej pojedynczy wydatek).

# 5. Podkomenda import-csv importuję listę wydatków z pliku CSV.

# 6. Program przechowuje pomiędzy uruchomieniami bazę wszystkich wydatków w pliku budget.db. Zapisuj i wczytuj stan używając modułu pickle. Jeżeli plik nie istnieje, to automatycznie stwórz nową, pustą bazę. Zauważ, że nie potrzebujemy podpolecenia init.

# 7. Wielkość wydatku musi być dodatnią liczbą. Gdzie umieścisz kod sprawdzający, czy jest to spełnione? W jaki sposób zgłosisz, że warunek nie jest spełniony?

import click
import csv
from dataclasses import dataclass
import pickle
import sys

"""

Usage:
python M07/M07L12_projekt.py add [amount] [description]

"""
@dataclass
class Expense:
    amount: float
    description: str
    id: int

    def __post_init__(self):
        if self.amount <= 0:
            raise ValueError("Amount cannot be zero or negative")
FILEPATH = 'M07\\expenses.db'
def empty_list():
    with open(FILEPATH, 'wb') as stream:
        pickle.dump([], stream)
    
def get_content():
    try:
        with open(FILEPATH, 'rb') as stream:
            reader = pickle.load(stream)
            return reader
    except FileNotFoundError:
        empty_list()
        print("Nie znaleziono pliku, został on stworzony.")
        sys.exit(1)

    
def add_id(expenses):
    ids = {expense.id for expense in expenses}
    counter = 1
    while counter in ids:
        counter += 1
    return counter

def print_expenses(expenses):
    print("ID | Wydatek | Big? | Opis")
    for expense in expenses:
        if expense.amount >= 1000:
            big = "{!}"
        else:
            big = "   "
        print(f"{expense.id:2} {expense.amount:9} {big:8} {expense.description:30}")
        
def add_expense(amount, description):
    content = get_content()
    expense = Expense(
        id=add_id(content),
        amount= float(amount),
        description=description
    )
    content.append(expense)
    with open(FILEPATH, 'wb') as stream:
        pickle.dump(content, stream)       

@click.group()
def cli():
    pass

@cli.command()
@click.argument('amount', type=int)
@click.argument('description')
def add(amount, description):
    add_expense(amount, description)

@cli.command()
def report():
    print_expenses(get_content())
    
@cli.command('export-python')
def export_python():
    print(get_content())

@cli.command('import-csv')
@click.argument('csvfile')
def import_csv(csvfile):
    empty_list()
    with open(csvfile, 'r', encoding="UTF-8") as stream:
        reader = csv.DictReader(stream)
        for row in reader:
            add_expense(row['amount'], row['description'])

if __name__ == "__main__":
    cli()


    

