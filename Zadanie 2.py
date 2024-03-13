# Jesteś konsultantem działającym dla Niebezpiecznika - polskiego lidera cyberbezpieczeństwa. Napisz program, który będzie dokonywał audytu bezpieczeństwa u klientów Niebezpiecznika - jesteś odpowiedzialny za moduł sprawdzający złożoność haseł i generujący raport z rekomendacjami. 
#
# 1. Poproś użytkownika o hasło, a następnie sprawdź, czy spełnia ono reguły bezpieczeństwa.
# 2. Hasło powinno mieć minimum jedną małą literę, jedną wielką literę i jeden znak specjalny.
# 3. Hasło nie może zawierać spacji!  (wewnętrzny wymóg klienta wynikający z ograniczeń ich systemu teleinformatycznego)
# 4. Hasło musi mieć minimum 8 znaków.
# 5. Jeśli hasło jest niepoprawne, wyświetl raport w punktach co należy zmienić.


password = input("Wprowadź hasło: ")
special = "!@#$%^&*()-_=+[{]}|;:'\",<.>/?"
upper_letter = 0
lower_letter = 0
special_sign = 0
space = 0


if len(password) >= 8:
    for char in password:
        if char.isspace():
            space += 1
        elif char.isupper():
            upper_letter += 1
        elif char.islower():
            lower_letter += 1
        elif char in special:
            special_sign += 1
            
    if space == 0:
        if upper_letter == 0:
            print("Wymagana wielka litera")
        if lower_letter == 0:
            print("Wymagana mała litera")
        if special_sign == 0:
            print("Wymagany znak specjalny")
    else:
        print("Hasło nie może zawierać spacji")
else:
    print("Hasło jest za krótkie.")