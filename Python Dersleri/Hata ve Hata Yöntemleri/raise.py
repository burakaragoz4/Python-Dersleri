# import re

# # x = 10

# # if(x > 5):
# #     raise Exception("X 5 den büyük değer alamaz")

# def check_password(psw):
#     if (len(psw) < 8):
#         raise Exception("Parola en az 7 karakter olmalıdır")
#     elif not re.search("[a-z]",psw):
#         raise Exception("Parola küçük harf içirmelidir.")
#     elif not re.search("[A-Z]",psw):
#         raise Exception("Parola büyük harf içirmelidir.") 
#     elif not re.search("[0-9]",psw):
#         raise Exception("Parola rakam harf içirmelidir.")
#     elif not re.search("[_@$]",psw):
#         raise Exception("Parola alpha numberic karakter içirmelidir.")
#     elif re.search("\s",psw):
#         raise Exception("Parola boşluk içirmemelidir.")

# password = "12345@6B7a9"

# try:
#     check_password(password)
# except Exception as ex:
#     print(ex)
# else:
#     print("Parola Geçerli ")
# finally:
#     print("Validation Tamamlandı")

class Person:
    def __init__(self, name, year):
        if (len(name)> 10):
            raise Exception("Name Alanı Fazla Karakter İçeriyor.")
        else:
            self.name = name 

p = Person("Aliiiiiiiiiiiiiiii",2021)