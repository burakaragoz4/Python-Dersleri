x,y,z = 2 ,5,107

numbers = 1,5,7,10,6
#1 Kullanıcıdan aldığınız  sayının çarpımı ile x,y,z toplamının farkı nedir
# sayi1 = input("Lütfen 1. Sayıyı Giriniz: ")

# sayi2 = input("Lütfen 1. Sayıyı Giriniz: ")

# totalinput = int (sayi1) * int(sayi2)
# totalxyz = x+y+z
# print("X,Y,Z'nin Toplamı: ",totalxyz)

# total = totalinput - totalxyz
# print("Yaptığımız İşlemlerin Sonucu: ",total)


#2 y'nin x'e kalansız bölümünü hesaplayınız
# total = y//x
# print(total)

#3 x,y,z toplamının mod 3 ü nedir?
# total = (x+y+z)%3
# print(total)

#4 y'nin x. kuvvetini hesaplayınız 
# y = y**x
# print(y)

#5  x, *y,z = numbers işlemie göre z'nin küpü kaçtır ?
# numbers = 1,5,7,10,6
# x , *y ,z = numbers
# print(z**3)

#6 x, *y,z = numbers işlemine göre y nin değerleri toplamı kaçtır ?
numbers = 1,5,7,10,6
x,*y,z = numbers

result = y[0]+y[1]+y[2]
print(result)

