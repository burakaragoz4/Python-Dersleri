# 1- Girilen 2 sayıdan hangisi Büyüktür ? 
# sayi1 = input("Lütfen 1. Sayıyı Giriniz: ")
# sayi2 = input("Lütfen 2. Sayıyı Giriniz: ")

# if sayi1 > sayi2 :
#     print(f"{sayi1} Büyüktür {sayi2}'den")

# elif sayi2 > sayi1 :
#     print(f"{sayi2} Büyüktür {sayi1}'den")

# else :
#     print(f"{sayi1} Eşittir {sayi2}'e")    

# 2- Kullanıcıdan 2 vize(%60) ve finL (%40) notunu alıp ortalama hesaplayınız eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın 

# vize1 = input ("Lütfen 1. Vize Notunuzu Giriniz: ")
# vize2 = input ("Lütfen 2. Vize Notunuzu Giriniz: ")
# final = input ("Lütfen Final Notunuzu Giriniz: ")

# vizetotal = (int(vize1)+int(vize2)) * 60/100
# print("Vize Ortalaması = ",vizetotal)
# finaltotal = (int(final)*40/100)
# print("Final Ortalaması = ",finaltotal)
# ortalama = int(vizetotal + finaltotal)

# print("Ortalama = ",ortalama)

# if ortalama >= 50 :
#     print("Geçti")
# else :
#     print("Kaldı")

# 3- Girilen sayının tek mi çift mi olduğunu yazdırın 

# sayi1 = input ("Lütfen bir sayi giriniz: ")
# if int(sayi1) > 0 :
#     if int(sayi1)  % 2 == 0:
#         print(f"Girilen Sayı {sayi1} Çifttir")
#     else :
#             print(f"Girilen Sayi {sayi1} Tektir")
# else :
#     print("Negatif Sayı Girdiniz ...")  
# 4- Girilen sayının negatif  pozitif durumunu yazdırın 

# sayi1 = input ("Lütfen bir sayi giriniz: ")     
# if int(sayi1)>0 :
#     print(f"Girilen {sayi1} sayısı Pozitifir")
# elif int(sayi1) ==0 :
#     print(f"Girilen {sayi1} sayısı 0'a Eşittir ")
# else :
#     print(f"Girilen {sayi1} sayısı Negatiftir")

# 5- Parola ve email bilgisini isteyip doğruluğunu kontrol ediniz

email = "email@sadikturan.com"
password = "abc123"

girilenEmail = input("Email: ")
girilenPassword = input("Parola: ")

isEmail = (email == girilenEmail)
isPassword = (password == girilenPassword)

print(f"Email bilgisi doğru mu : {isEmail}")
print(f"Parola bilgisi doğru mu : {isPassword}")

