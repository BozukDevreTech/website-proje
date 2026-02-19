# Copyright (c) 2026 bozuk_devre
# All rights reserved.
# Developed as part of Data Structures coursework at Yaşar Üniversitesi with instructor guidance.
# This code may not be copied, modified, or distributed without explicit permission from the author.


#kullanıcıdan alınan sayıya kadar tüm asal olan sayıları ekrana yazdıran algoritma

alinan_sayi = int(input("bir sayı giriniz:"))
for sayi in range(2,alinan_sayi-1,1):
        asal = True

        for i in range(2,sayi-1,1): #eğer 101 olursa kendisine bölündüğünde sonuç 0 olur ve asal olarak çıkar
            if sayi%i==0:
                asal=False

            else:
                asal == False
                #kodu durdurmaz ama o sayı artık asal değildir

        if asal == True:
            print(sayi)
#sonuna sayaç koyularak asal bölenler var mı diye kontrol edilebilir