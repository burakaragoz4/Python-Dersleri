website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"
 
result = len(course) 
lenght = len(website)
#1 kaç karakter olduğuna bak 
# print(result)
result = website[7:10] #2 www karakterlerini al 
# print(result)

result = website[22:25] #3 com karakterlerini al 
result = website[lenght-3:lenght]
# print(result)

result = course [0:15] #4 ilk 15 ve son 15 karakterlerini alın
# print(result)
result = course [:15] #15.satır ile aynı 
# print(result)
result = course [-15:]
# print(result)

result = course [::-1] #5 karakterli tersten yazdırın  "bütün elemanları : : ile alırız ve "
s = '12345' * 5
# print(s[::5]) #sadece 5. indexteki karakterleri alır ve 5 kere çarpmış olduk 
# print(result)

# name, surname, age, job = "Bora" ,"Yılmaz","32","Mühendis" #6
# print(f"Benim adım {name} {surname},Yaşım {age} ve mesliğim {job}")

# s = "Hello world"
# s = s[0:6]+'W'+s[-4:]#7 w harfini W yaptık
# s.replace('w',"W")#w gördüğün yere W yaz
# print(s)

result = "abc" *3
print(result)
