# Copyright (c) 2026 bozuk_devre
# All rights reserved.
# Developed as part of Data Structures coursework at Yaşar Üniversitesi with instructor guidance.
# This code may not be copied, modified, or distributed without explicit permission from the author.

#Bu phyton kodu, kullanıcın girdiği verilere dayanarak Vki değerini hesaplar ve durumunu bildirir

print("Vücut Kitle İndeksi Hesaplama Aracına Hoşgeldin..")
boy=float(input("boyunuzu giriniz(mesela: 1.75):"))
kilo=float(input("kilonuzu giriniz(mesela: 56):"))
Vki=kilo/(boy*boy)#kilo/boykare=vki


print("vücut kitle indeksi sonucunuz:",Vki)

if Vki< 18.5:
    print("Durum: 🔵    Tüy gibisin")
elif Vki < 25:
    print("Durum: 🟢    Normal/Sağlıklı")
elif Vki < 30:
    print("Durum: 🟡    Şişman (Balık etli)")
elif Vki < 35:
    print("Durum: 🟠    1.der.Obez (Az yee)")
elif Vki < 40:
    print("Durum: 🔴    2.der.Obez (Bi beni yememişsin)")
else:
    print("Durum: ‼️ 💀 Morbid obez")

input()

