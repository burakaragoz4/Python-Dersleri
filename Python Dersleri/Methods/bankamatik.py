# Bankamatik Uygulaması

BurakHesap = {
    "ad" : "Burak Karagöz",
    "hesapNo" : "123456789",
    "bakiye": 3000,
    "ekHesap" : 2000
}

AliHesap = {
     "ad" : "Ali Turan",
    "hesapNo" : "11111",
    "bakiye": 2000,
    "ekHesap" : 1000
}

def paraCek(hesap, miktar):
    print(f"Merhaba Sayın {hesap['ad']}")

    if (hesap['bakiye'] >= miktar):
        hesap['bakiye'] -= miktar
        print(f"Sayın {hesap['ad'] } Paranızı Alabilirsiniz.")
        bakiyeSorgula(hesap)
    else:
        toplam = hesap['bakiye'] + hesap["ekHesap"]
        if (toplam >= miktar):
            ekHesapKullanimi = input(f"Ek Hesap Kullanılsın mı (Ek Hesab Bakiyeniz: {hesap['ekHesap']}) \n(e/h): ")

            if(ekHesapKullanimi == 'e'):      
                ekHesapKullanilacakMiktar = miktar - hesap['bakiye']               
                hesap['ekHesap'] -= ekHesapKullanilacakMiktar - hesap['bakiye']               
                print(f"Sayın {hesap['ad']} Paranızı Alabilirsiniz.")
                bakiyeSorgula(hesap)

            else:
                print(f"Sayın {hesap['ad'] }  {hesap ['hesapNo']} Nolu Hesabınızın Toplam Bakiyesi {hesap['bakiye']+hesap['ekHesap']} Bulunmaktadır.")

        else:
            print(f"Sayın {hesap['ad']} Bakiyeniz Yetersiz ...")
            bakiyeSorgula(hesap)
def bakiyeSorgula(hesap):
    print(f"Sayın {hesap['ad']} {hesap['hesapNo']} Numaralı Hesabınız da {hesap['bakiye']} TL Bulunmaktadır.\nEk Hesabınızda ise {hesap['ekHesap']} TL Bulunmaktadır.")

paraCek(BurakHesap,3000)

print("************************")

paraCek(BurakHesap,2000)




