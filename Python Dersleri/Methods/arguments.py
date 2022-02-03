# def changeName(n):
#     n = "Ada"
#
# name = "yiğit"
# changeName(name)
# print(name)
#
# def change(n):
#     n[0] = "İstanbul"
#
# sehirler = ["Ankara","İzmir"]
#
# change(sehirler[:])
#
# n = sehirler[:] #slicing
# n[0] = "İstanbul"
#
# print(sehirler)

# def add(a,b,c=0,d=0,e=0):
#     return sum((a,b,c,d,e))
# print(add(10,20))
# print(add(10,20,30))
#
# def add(*params):
#     print(f"Girilen Değerler: {params} ")
#     return "Sayıların Toplamı " +str(sum((params))) +"\n"
#
# print(add(10,30,60))
# print(add(5,10))
# print(add(50,100,150))
# def displayUser(**args):
#     print(type(args))
#     for key,value in args.items():
#         print("{} is {}".format(key,value))
#
# displayUser(name = "Çınar", age = 2, city = "Ankara")
#
# displayUser(name = "Ada", age = 12, city = "İzmir", phone ="12341234")
#
# displayUser(name = "Bora", age = 14, city = "Kocaeli", phone ="12341", email = "burak@hotmail.com")
#
# def myFun(a,b,c,*args,**kwargs):
#     print(a)
#     print(b)
#     print(c)
#     print(args)
#     print(kwargs)
#
# myFun(10,20,30,40,50, key1 = "value1",key2 = "value2")