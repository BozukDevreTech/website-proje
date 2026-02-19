# Copyright (c) 2026 bozuk_devre
# All rights reserved.
# Developed as part of Data Structures coursework at Yaşar Üniversitesi with instructor guidance.
# This code may not be copied, modified, or distributed without explicit permission from the author.

#Bu kod bir tahmin oyunu oluşturmak amacıyla hazırlanmıştır
#Kullanıcı rastgele seçilen sayıyı yönlendirmelerle tahmin etmeye çalışır

import random
rastgele_sayi=random.randint(0,50)


while True:
    try:
        tahmin=int(input("0-50 arasında bir sayı tahmin et:"))
        if tahmin<0 or tahmin>50:
            print("0-50 arasında dedim! bir daha gir")
            continue
        if tahmin<rastgele_sayi:
            print("biraz arttır kanka")
            continue
        elif tahmin>rastgele_sayi:
            print("çok gittin azalt kanka")
            continue
        else:
            print("Bravo doğru tahmin!")
            break
    except ValueError:
        print("Özel karakter olmaz! sayı girmelisin.")
input("çıkmak için bir tuşa bas")