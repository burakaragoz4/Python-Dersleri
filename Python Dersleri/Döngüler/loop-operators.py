 # for item in range(10,100,20):
#     print(item)
#
# print(list(range(10,100,20)))

#enumerate

# greeting = "Hello There"
#
# for item in enumerate(greeting):
#     print(item)
# # for index, letter in enumerate(greeting):
# #     print(f"index: {index} ,letter: {letter}")
# #     index +=1

#zio
list1 = [1,2,3,4,5]
list2 = ["a","b","c","d","e"]

# print(list(zip(list1,list2)))

for item in (zip(list1,list2)):
    print(item)