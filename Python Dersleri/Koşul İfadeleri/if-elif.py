x = input("X Sayısını Giriniz: ") # int(input("X Sayısını Giriniz: "))
y = input("Y Sayısını Giriniz: ")

if x > y :
    print("{} {} 'dan Büyük".format(x,y))
elif x == y:
    print("{}={}".format(x,y))
else:
    print("{} {} den Büyük".format(y,x))
