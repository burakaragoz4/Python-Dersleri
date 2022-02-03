# name = "Burak Karagöz"
#
# for letter in name:
#     if letter == "a":
#         continue
#     print(letter)

# x = 0
#
# while x < 5 :
#     x += 1
#     if x == 2:
#         continue
#     print(x)

# 1- 100 e kadar tek sayıların toplamı
result = 0
x = 1
while x <= 100 :
    x+=1
    if x%2 == 1:
        continue
    result +=x

print(f"Toplam:{result}")




