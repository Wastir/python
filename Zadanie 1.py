### 🔴 Projekt

# Napisz dla BBC program sprawdzający złożoność artykułów i wpisów, dzięki czemu pracę dziennikarzy będzie można sparametryzować i automatycznie ustalić, czy piszą teksty proste i łatwe w zrozumieniu. Policz jaka jest średnia długość słów i wyświetl rezultat.

print("Wprowadź tekst swojego artykułu")
text = input("Tekst: ")
print("Ilość znaków w podanym artykule:", len(text))

words = len(text.split())  # liczba słów

print("Ilość słów zawartych w artykule:", words)
a = len(text)  
b = words
division = a / b
print("Srednia długość słów:", division)