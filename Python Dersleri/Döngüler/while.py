# 1-100 e kadar yazdırma

# x = 0
# while x <= 100 :
#     if( x % 2 == 1):
#         print(x)
#     x += 1
# print("bitti ...")

name = ""
while not name.strip() :
    name = input("İsminizi Giriniz: ")

print("Merhaba {}".format(name))