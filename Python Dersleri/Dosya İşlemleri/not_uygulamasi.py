def not_hesapla(satir):
    satir = satir[:-1] # satırların arasında ki boşlukları aldık 
    liste = satir.split(':') # : öncesini ve sonrasını ayırdık 

    ogrenciAdi = liste[0]
    notlar = liste[1].split(',')

    not1= int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])
    
    ortalama = (not1 + not2 + not3)/3

    if (ortalama > 90) and (ortalama <= 100):
        harf = "AA"
    elif (ortalama >= 85) and (ortalama <=89):
        harf = "BB"
    elif (ortalama >= 65) :
        harf = "CC"
    else:
        harf = "FF"
    return ogrenciAdi + ": "+ harf + "\n"

def ortalamalari_oku():
    with open("sinav_notlari.txt", "r",encoding="utf-8") as file:
        for satir in file:
            print(not_hesapla(satir))

def not_gir():
    ad = input("Öğrenci Adı:")
    soyad = input("Öğrenci Soyad:")
    not1 = input("Not 1: ")
    not2 = input("Not 2: ")
    not3 = input("Not 3: ")
    with open("sinav_notlari.txt", "a",encoding="utf-8") as file:
        file.write(ad+" "+ soyad+ ":"+not1+","+not2+","+not3+"\n")


def notlari_kayitEt():
    with open("sinav_notlari.txt", "r",encoding="utf-8") as file:
        liste = []
        for i in file:
            liste.append(not_hesapla(i))

    with open("sonuclar.txt", "w",encoding="utf-8") as file2:
        for i in liste:
            file2.write(i)

while True:
    islem = input("1- Notları Oku\n2- Not Gir\n3- Notları Kayıt Et\n4- Çıkış\n")

    if islem == "1":
        ortalamalari_oku()
    elif islem == "2":
        not_gir()
    elif islem == "3":
        notlari_kayitEt()
    elif islem == "4":
        break