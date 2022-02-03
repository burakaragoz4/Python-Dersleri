#Sayilar listesindeki hangi sayılar 3'ün katıdır ?
from math import sqrt

sayilar = [1,3,5,7,9,12,19,21]
# for number in sayilar :
#     if(number % 3==0):
#       print(number)
#Sayiların toplamı nedir?
# toplam = 0
# for number in sayilar:
#      toplam += number
# print(toplam)
#Listeki tek sayıların karelerini alınız
# for number in sayilar:
#     if(number % 2 == 1):
#         kare = number**2
#         print("{} 'si = {}'dir".format(number,kare))
#Şehirlerden hangileri en fazla 5 karakterlidir ?
# sehirler = ["kocaeli","istanbul","ankara","izmir","rize"]
# for sehir in sehirler:
#     if(len(sehir)<=5):
#         print(sehir)
#ürünlerin fiyatları toplamı nedir ?
urunler = [
    {"name ": "samsung s6", "price": "3000"},
    {"name ": "samsung s7", "price": "4000"},
    {"name ": "samsung s8", "price": "5000"},
    {"name ": "samsung s9", "price": "6000"},
    {"name ": "samsung s10", "price": "7000"},
]
# toplam = 0
# for urun in urunler:
#     fiyat = int(urun['price'])
#     toplam += fiyat
# print(toplam)
#Ürünlerden fiyatı en fazla 5000 olan ürenleri gösteriniz ?
for urun in urunler:
    if(int(urun['price'])<=5000):
        print(urun)
