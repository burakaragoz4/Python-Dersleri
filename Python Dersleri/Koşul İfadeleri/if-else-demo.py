# name = str(input("Lütfen Adınızı Giriniz: "))
# age = int(input("Lütfen Yaşınızı Giriniz: "))
# education = int(input("Eğitim Bilginiz 1-İlkokul, 2-Lise, 3-Üniversite Lütfen Biriniz Seçiniz: "))
#
# if (age >=18) :
#     if (education >= 2) :
#         print("{} Ehliyet Alabilirsin".format(name))
#     else:
#         print("{} Ehliyet Alamazsın".format(name))
# else:
#     print("Yaşınız Tutmuyor")

import datetime

date = input("Aracınızın Hangi Tarihte Trafiğe Çıktı (2019/8/9): ")
date = date.split("/")

trafigeCikis = datetime.datetime(int(date[0]),int(date[1]),int(date[2]))
simdi = datetime.datetime.now()
fark = simdi - trafigeCikis
day = fark.days
# 2. Çözüm day = input("Lütfen Trafiğe Çıkış Tarihini Yazınız: ")
if day <= 365:
    print("1.Servis Aralığı")
elif day>365 and day<=365*2:
    print("2.Servis Aralığı")
elif day>365*2 and day<=365*3:
    print("3.Servis Aralığı")
else:
    print("Hatalı Süre")