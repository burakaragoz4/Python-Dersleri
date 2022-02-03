'''
    1-100 Arasında rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile
    buldurmaya çalışın. (hak = 5)

     "random modülü" için "python random" şeklinde arama yapın.
        100 üzerinden puanlama yapın. Her soru 20 puan.
        Hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı
        üzerinden hesaplansın.

'''
import random

sayi = random.randint(1,10)
can = int(input("Kaç hak kullanmak istersiniz: "))
hak = can
sayac = 0
puan = 100
while hak > 0:
    hak -=1
    sayac +=1
    puan =int(100 - (sayac-1) * (100/can))
    tahmin  = int(input("Tahmin: "))
    if (sayi == tahmin):

        print(f"Tebrikler {sayac}. Tahminde Bildiniz\nRandom Sayı: {sayi} \nSizin Sayınız: {tahmin} \nPuanınız: {puan} ")
        break
    elif(sayi>tahmin):
        print("Yukarı")

    elif(sayi<tahmin):
        print("Aşağı")
    else:
        print("HATALI TUŞLAMA YAPTINIZ")

    if hak == 0:
        print(f"Hakkınız bitti. Tutulan sayı:{sayi}\nPuanınız: {puan}")