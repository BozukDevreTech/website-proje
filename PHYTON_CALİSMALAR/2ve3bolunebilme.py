# Copyright (c) 2026 bozuk_devre
# All rights reserved.
# Developed as part of Data Structures coursework at Yaşar Üniversitesi with instructor guidance.
# This code may not be copied, modified, or distributed without explicit permission from the author.
#bu kod, kullanıcıdan alınan sayının asal 2'e ve 3'e bölünebilme durumunu kontrol eder ve bildirir.

while True:
    print("2 & 3'e bölünme çalışmama hoşgeldin..")
    try:
        verilen=int(input("Kafadan bir sayı at:"))
        if verilen%2==0:
            if verilen%3==0:
                print("Nokta atışı!! sayı her ikisine de tam bölünebiliyor!")
            else:
                print("sayı sadece 2'e tam bölünüyor")
        elif verilen%3==0:
            print("sayı sadece 3le tam bölünebiliyor")
        else:
            print("sayı hiçbirine bölünmüyor bune")

    except ValueError:
        print("❌ sayı gir dedim!")
        continue

# tekrar mı çıkış mı?
    secim = input("\nTekrar denemek ister misin? (E/H): ").lower()

    if secim == "h":
        print("Peki, Bye 👋 ...")
        input()
        break

    elif secim == "e":
        continue

    else:
        print("Geçersiz seçim. Program kapatılıyor.")
        break