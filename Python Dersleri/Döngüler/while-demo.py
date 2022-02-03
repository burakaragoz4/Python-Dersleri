# sayilar = [1,3,5,7,9,12,19,21]
# 1: Sayiler listesini while ile ekrana yazdır.
# x = 0
# while ( x <len(sayilar)):
#     print(sayilar[x])
#     x+=1

# 2: Başlangıç ve bitiş değerlernini kullanıcıdan alıp aradaki tüm tam sayıları ekrana yazdırın
# baslangic = int(input("Başlangıç Değeri Giriniz: "))
# bitis = int(input("Bitiş Değeri Giriniz: "))
#
# while baslangic < bitis :
#     if(baslangic % 2 == 1):
#         print(baslangic)
#     baslangic += 1

# # 3: 1-100 arasındaki sayıları azalan şekilde yazdırın.
# x = 100
# while x > 0:
#     print(x)
#     x -=1

# 4: Kullanıcıdan aldığınız 5 sayıyı sıralı bir şekilde yazdırınız
numbers = []
i = 5
y = 1
while i>0 :

    sayi = int(input(f"Lütfen {y}. Sayiyi Giriniz :"))
    numbers.append(sayi)
    i-=1
    y+=1
    numbers.sort()
print(numbers)
