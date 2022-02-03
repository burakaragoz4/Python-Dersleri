# 1: Liste elemanları içideki sayısal değerleri bulunuz.
liste = ["1","2","5a","10a","abc","10","50"]
# for x in liste:
#     try:
#         result = int(x)
#         print(result)
#     except ValueError:
#         continue

# 2: Kullanıcı "q"(Quit) değerini girmedikçe aldığınız her inputun sayısal olduğundan emin olunuz
# aksi halde hata mesajı yazınız.
# while True:
#     sayi = input("Sayı: ")
#     if (sayi == "q"):
#         print("Güle Güle")
#         break

#     try:
#         result = float(sayi)
#         print("Girdiğiniz Sayı: ",result)
#     except ValueError :
#         print("Geçersiz sayı")
#         continue

# 3: Girilen parola içinde türkçe karakter hatası veriniz.
# def checkPassword(password):
#     turke_karakterler = "çğıöüşİ"

#     for i in password:
#         if (i in turke_karakterler):
#             raise TypeError("Parola Türkçe Karakter İçeremez.")
#         else:
#             pass
#     print("Parola Geçerli")

# parola = input("Parola: ")
# try:
#     checkPassword(parola)
# except TypeError as err:
#     print(err)


# 4: Faktöriyel fonksiyonu oluşturup fonksiyona gelen değer için 
# hata mesajları verin.

def factorial(number):

    number = int(number)
    if number < 0:
        raise ValueError("Negatif Değer Olamaz")
    
    result = 1
    
    for i in range(1,number+1):
        result *= i

    return result
for number in [5,10,20,-3,"10a"]:
    try :
        y = factorial(number)
    except ValueError as err:
        print(err)
        continue
    print(y)
