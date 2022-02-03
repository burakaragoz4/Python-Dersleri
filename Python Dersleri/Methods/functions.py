# fonksiyon

# name = str(input("Lütfen İsminizi Giriniz: "))
# def sayHello(name):
#     return "Hello " + name
#
# msg = sayHello(name)
# print(msg)
# msg = sayHello("Burak")
# print(msg)

# def total(num1,num2):
#     return num1 + num2
#
# result = total(10,20)
#
# print(result)

def yasHesapla(doyumYili):
     return 2021-doyumYili
ageCinar = yasHesapla(1999)
ageBurak = yasHesapla(2010)
ageSena = yasHesapla(2017)
print(ageCinar,"\n",ageBurak,"\n",ageSena)

def EmeklilikgeKacYilKaldi(dogumYili,isim):
    yas = yasHesapla(dogumYili)
    emeklilik = 65 -yas

    if(emeklilik > 0):
        print(f"{isim} Bey Emekliliğinze {emeklilik} yıl kaldı")
    else:
        print("Zaten Emekli Oldunuz")

EmeklilikgeKacYilKaldi(1983,"Ali")