# try:
#     file = open ("newfile.txt","r",encoding="utf-8")
#     print(file.read())
# except FileNotFoundError:
#     print("Dosya Okuma Hatası")
# finally:
#     print("\nDosya Kapandı")
#     file.close()

from typing import ContextManager


file = open("newfile.txt","r",encoding="utf-8")

# # for döngüsü
# # for i in file:
# #     print(i, end = "") # Aralarına boş satır varsa kaldırma.

# # read() fonksiyonu
# content = file.read()
# print("İçerik 1")
# print(content)

# # file = open("newfile.txt","r",encoding="utf-8") Bu satır olmaz ise content2 boş olarak var sayılır çünkü satır sonuna gelinmiştir
# content2 = file.read()
# print("İçerik 2")
# print(content2)

# content = file.read(5)
# content = file.read()
# print(content)

# ********** readline() fonksiyonu Satır Okuma
 
# print(file.readline(),end = "")
# print(file.readline(),end = "")
# print(file.readline(),end = "")
# print(file.readline(),end = "")
# print(file.readline(),end = "")
# print(file.readline(),end = "")
# print(file.readline(),end = "")
# print(file.readline(),end = "")
# print(file.readline())
# print(file.readline())

# ************ readlines() fonksiyonu

liste = file.readlines()
print(liste)
print(liste[0])
print(liste[1])
file.close()