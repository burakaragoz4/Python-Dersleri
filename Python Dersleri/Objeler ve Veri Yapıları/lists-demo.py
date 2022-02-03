#1 
arabalar = ["BMW","Mercedes","Opel","Mazda"]

#2
# result = len(arabalar) #Dizide kaç eleman var


#3
# result = arabalar[0]
# print(result)
# result = arabalar[-1] Dizinin ilk ve son elemanı

#4
# arabalar[-1] ="Toyota" Mazda yerine toyota yazdırma
# result = arabalar
# print(result)

#5
# result = "Mercedes" in arabalar  Dizide Mercedes kelimesi var mı diye baktık
# print (result)

#6
# result = arabalar[-2] Dizinin -2. indexi
# print(result)

#7
# result = arabalar[0:3] Dizinin ilk 3 elemanını alın
# print(result)

#8
# arabalar[-1] = "Toyota"
# arabalar[-2] = "Renault"

# arabalar[-2:] = "Toyota" , "Renault"
# result = arabalar Dizinin son iki elemanını değiştir

#9
# arabalar += ["Audi","Nissan"] Diziye Auidi ve Nissanı ekle
# result = arabalar
# result = arabalar + ["Audi","Nissan"] 9. örneğin değişik çözümü

#10
# del arabalar[-1] İstediğimiz elemanı siliyoruz
# result = arabalar

#11
# result = arabalar[::-1] Dizi elemanlarını tersten yazdır
# print(result)

#12
studentA = ["Yiğit","Bilgi",2010,[70,60,70]]
studentB = ["Sena","Turan",1999,[80,80,70]]
studentC = ["Ahmet","Turan",1998,[80,70,90]]

students = studentA + studentB + studentC

result = f"{studentA[0]} {studentA[1]} {2021-studentA[2]} Yaşında ve not ortalaması {(studentA[3][0]+studentA[3][1]+studentA[3][2])/3}"

print(result)
