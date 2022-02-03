name = ["Ali","Yağmur","Hakan","Deniz"]
years = [1998,2000,1998,1987]

#1  Cenk ismini listenin sonuna ekleyin 
# name.append("Cenk") 
# print(name)

#2 Sena Değerini listenin başına ekleyin
# name.insert(0,"Sena")
# print(name)

#3 Deniz ismini listeden siliniz
# name.remove("Deniz")
# print(name)

#4 Deniz isminin indexi nedir
# print(name.index("Deniz"))

#5 Ali listenin bir elemanı mıdır
# print("Ali" in name)

#6 Liste elemanlarını tesr çevir
# print(name[::-1])

#7 Liste elemanlarını alfabetik olarak sırala
# name.sort()
# print(name)

#8 Years listesinin rakamsal büyüklüğüne göre sıralayınız
# years.sort()
# print(years)

#str = "Chevrolet , Dacia" #karakter dizisini listeye çevirme
str = "Chevrolet , Dacia"
result = str.split(",")
print(result)

#10 years dizisinin en büyük ve en küçük elemanı
# print(max(years))
# print(min(years))

#11 years dizisinde kaç tane 1998 değeri vardır
# print(years.count(1998))

#12 years dizisinin tüm elemanlarını siliniz
# years.clear()
# print(years)

#13 Kullanıcıdan alacağınız 3 tane marka bilgisini listede saklayınız

markalar = []

marka = input("Marka Giriniz: ")
markalar.append(marka)
marka = input("Marka Giriniz: ")
markalar.append(marka)
marka = input("Marka Giriniz: ")
markalar.append(marka)

print(markalar)

