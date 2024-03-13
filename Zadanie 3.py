# Pomóż zespołowi Stanford AI Lab przeanalizować zbiór danych składający się z 50 tys. recenzji filmów, dzięki czemu będą mogli automatycznie określać sentyment nowych komentarzy i wypowiedzi w internecie. W szczególności zależy im, aby zidentyfikować te najbardziej pozytywne i negatywne wypowiedzi wśród milionów neutralnych komentarzy - dzięki temu będą mogli udostępnić te najbardziej pozytywne, a w przypadku tych najbardziej negatywnych będą mogli zareagować i odpowiedzieć zanim taki komentarz dotrze do szerszego grona.

# 1. Wszystkie pliki znajdują się w katalogu M03/data/aclImdb/train. W podkatalogu "pos" znajdują się pozytywne komentarze, tzn. minimum 7/10. W podkatalogu "neg" znajdują się negatywne komentarze, czyli te 6/10, 5/10 i niżej. Każda recenzja to osobny plik.
# 2. W recenzjach znajdują się fragmenty HTML - "<br />" oznaczający znak końca linii. Takie fragmenty zastąp spacją.
# 3. Wczytaj wszystkie pozytywne i negatywne recenzje do dwóch osobnych zmiennych. Będzie łatwiej, jeśli każdą recenzję będziesz reprezentować nie jako string, tylko jako listę słów. Tak więc każda z tych dwóch osobnych zmiennych będzie listą list.
# 4. Następnie poproś użytkownika, aby wpisał komentarz, którego sentyment chce wyliczyć. Podziel ten komentarz na słowa.
# 5. Sentyment poszczególnych słów w tym komentarzu liczymy wg wzoru (positive-negative)/all_, gdzie positive to liczba pozytywnych recenzji, w których pojawiło się to słowo. Negative to liczba negatywnych recenzji, w których pojawiło się to słowo. Natomiast all_ to liczba wszystkich recenzji, w których pojawiło się to słowo. Na przykład, jeśli dane słowo pojawia się w 5 pozytywnych i 5 negatywnych recenzjach, to jego sentyment wynosi (5-5)/10 = 0.0. Jeśli dane słowo pojawia się w 9 pozytywnych i 1 negatywnej recenzji, to jego sentyment wynosi (9-1)/10 = +0.8. Jeśli dane słowo pojawia się w 90 pozytywnych i 10 negatywnych recenzjach, to jego sentyment wynosi (90-10)/100 = +0.8, tak samo jak wcześniej. Tak więc liczba zawsze jest z zakresu od -1.0 do +1.0. 
# 6. Sentyment całego tego komentarza to średnia arytmetyczna sentymentu wszystkich słów. Tak więc wystarczy zsumować sentyment poszczególnych słów i następnie taką sumę podzielić przez liczbę słów. W ten sposób sentyment całego komentarza też będzie z zakresu od -1.0 do +1.0.
# 7. Cały komentarz uznajemy za pozytywny, gdy jego sentyment jest > 0, a negatywny gdy jest < 0.
import glob
BR = "<br />"
files = glob.glob('M03/data/aclImdb/train/pos/*.txt') + glob.glob('M03/data/aclImdb/train/neg/*.txt')
comments_pos = []
comments_neg = []

for files_list in files:
    with open(files_list, encoding = "UTF-8") as stream:
        file_text = stream.read().lower()
    file_text = file_text.replace("<br />", " ")
    if 'pos' in files_list:
        comments_pos.append(file_text.split())
    elif 'neg' in files_list:
        comments_neg.append(file_text.split())
input_text = input("Podaj komentarz do sprawdzenia: ").lower().split()
sentiment = 0
for index in input_text:
    pos_number = 0
    neg_number = 0
    for comment in comments_pos:
        if index in comment:
            pos_number += 1
    for comment in comments_neg:
        if index in comment:
            neg_number += 1
    all_commment_number = pos_number + neg_number
    print(pos_number, "   ", neg_number)
    print(all_commment_number)
    word_sentiment = (pos_number - neg_number) / all_commment_number
    sentiment = sentiment + word_sentiment
    print("Słowo ", index, "posiada sentyment ", word_sentiment)
sentiment = sentiment / len(input_text)
print("Ogólny sentyment: ", sentiment)


      


