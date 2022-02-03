fruits = {"orange","apple","banana"}
# print(fruits [0]) #indekslenemez

for x in fruits:
    print(x)

fruits.add("Cherry")
fruits.update(["mango","grape","apple"])#elmayı bir kere daha eklemeye çalıştık ama olmaz

fruits.remove("mango")
fruits.discard("apple")
print(fruits)
fruits.pop()

fruits.clear()
print(fruits)#rastgele bir elemanı siler

# myList = [1,2,5,4,4,2,1]
# print(set(myList)) #set tekrarlıyan elemanları çıkartır
