# Napisz własną analitykę do aplikacji do śledzenia czasu takich jak np. Toggl Track. Twój moduł wczytuje dane o czasie wykonania poszczególnych zadań w formacie CSV, a następnie generuje raport wykorzystania czasu z podziałem na projekty, klientów i inne tagi.

# 1. Dane w pliku CSV mają trzy kolumny: desc, time oraz tags. Desc jest opisem zadania. Time to liczba całkowita określająca czas wykonywania tego zadania w minutach. Natomiast tags jest listą tagów porozdzielanych spacjami. Jedno zadanie może mieć wiele tagów. Jednym tagiem może być otagowane wiele zadań. Tagi służą do oznaczania zadań wg projektów, klientów lub innych kryteriów.

# 2. Upakuj te trzy informacje w klasie Entry. Upewnij się, że ma ona metodę __repr__.

# 3. Program przyjmuje scieżkę do pliku CSV jako argument linii poleceń. Następnie wyświetla raport. Każda jego linia to jeden tag. Dla każdego tagu wyliczona jest suma wszystkich otagowanych nim zadań.

# 4. Nie musisz pisać testów, ale podziel program na funkcje tak, aby każda z nich robiła tylko jedną rzecz.

"""
Usage: Python M06\M06L14_projekt.py [TRACK_FILE]
"""
import csv
import click

class Entry:
    def __init__(self, desc, time, tags):
        self.desc = desc
        self.time = time
        self.tags = tags
    def __repr__(self):
        return f"Entry({self.desc!r}, {self.time!r}, {self.tags!r})"

def return_tracklist(row):
    return Entry(
        desc = row["desc"],
        time = int(row["time"]),
        tags = row["tags"]
    )

def track_open(file):
    with open(file, encoding = "UTF-8") as stream:
        reader = csv.DictReader(stream)
        return [return_tracklist(row) for row in reader]
    
def list_track(trackers):
    return list({word for track in trackers for word in track.tags.strip().split()})

def time_count(tag_list, trackers):
    tag_times = {tag: 0 for tag in tag_list}
    for track in trackers:
        track_tags = track.tags.strip().split()
        for tag in track_tags:
            if tag in tag_times:
                tag_times[tag] += track.time
    return tag_times
    

@click.command()
@click.argument('track_file')

def main(track_file):
    tracking = track_open(track_file)
    tag_times = time_count(list_track(tracking), tracking)
    for tag, time in tag_times.items():
        print(f"Tag: {tag}, Total time: {time}")
if __name__ == "__main__":
    main()

