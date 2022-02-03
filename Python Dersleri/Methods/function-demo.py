# 1- Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazın.
# def yazdir(kelime,adet):
#     print(kelime * adet)
#
# yazdir("Merhaba\n",10)

# 2- Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren foksiyonu yazın.
# def listeyeCevir(*params):
#     liste = []
#
#     for param in params:
#         liste.append(param)
#
#     return liste
# result = listeyeCevir(10,20,30,'Merhaba')
# print(result)
# 3- Gönderilen 2 sayı arasındaki tüm asal sayıları bulun.
# def asalSayılariBul(sayi1, sayi2):
#         for sayi in range(sayi1, sayi2+1):
#             if sayi > 1:
#                 for i in range(2, sayi):
#                     if(sayi % i == 0):
#                         break
#                 else:
#                     print(sayi)
# sayi1 = int(input("1.Sayıyı Giriniz: "))
# sayi2 = int(input("2.Sayıyı Giriniz: "))
# asalSayılariBul(sayi1,sayi2)
# 4- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde dönndürün.
def tamBolenSayilar(sayi):
    liste = []

    for i in range(2, sayi):
        if(sayi % i == 0):
            liste.append(i)
    return liste

sayi = int(input("Lütfen Bir Sayı Giriniz: "))
print(tamBolenSayilar(sayi))