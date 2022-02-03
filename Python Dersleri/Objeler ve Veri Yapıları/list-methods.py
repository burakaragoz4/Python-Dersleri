numbers = [1,10,5,16,4,9,10]
letters = ["a","g","s","b","y","a","s"]

val = min(numbers)#dizideki en küçük değer
val = max(numbers)#dizideki en büyük değer
val = min(letters)#dizinin alfabeye göre en önce gelen harfi
val = max(letters)#dizinin alfabeye göre en son gelen harfi 

val = numbers[3:6] #3 den 6 ya kadar yazdır 6 dahil değil

val = numbers[:3] #baştan başla 3 indexi al 

val = numbers [4:] #4den başla sonra kadar git

val = numbers [4] = 40 #4. eleman yerinde 40 yazdırdık 

numbers .append(49)#diziye eleman ekledik
numbers .append(59)

numbers.insert(0,-2) #ilk elemandan önce -2 ekledik 
numbers.insert(-1,52)

#numbers.pop() #en sondaki elemanı siler 
# numbers.pop(0) #ilk elemanı siler
# numbers.pop(-1) son elemanı siler

# numbers.remove(49) silmek istediğinimiz değer

numbers.sort()#sayısal olarak sırala
letters.sort()#harfsel olarak sıralar

numbers.reverse()#sıralanamış diziyi tersten yazzdırır
letters.reverse()

print(len(numbers))
print(len(letters))


print(numbers.count(10))#numbers dizisinde 10 elemanından kaç tane var 
print(letters.count("a"))#letters dizisinde a elemanından kaç tane var

# numbers.clear()#bütün elemanları siler
print(numbers)

