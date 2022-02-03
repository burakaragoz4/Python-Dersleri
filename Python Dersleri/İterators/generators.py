# def cube():
#     for i in range(5):
#      yield i ** 3 

# for i in cube():
#     print(i)

liste = (i for i in range(5)) # [i for i in range(5)]
print(liste)

for i in liste:
    print(i)
# print(next(liste))
# print(next(liste))
# print(next(liste))
# print(next(liste))
