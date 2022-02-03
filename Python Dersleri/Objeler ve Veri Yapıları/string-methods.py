message = "Hello There. My name is Burak Karagöz"

# message = message.upper() Hepsi büyük harf olur
# message = message.lower() Hepsi küçük harf olur
# message = message.title() Baş harfleri büyük olur
# message = message.capitalize() Sadece ilk harf büyük olur 

# message = message.strip() Başta ve sondaki boşlukları kaldırır

# message = message.split('.') #Kelime kelime ayırıyor

# print(message[1])
# index=message.find("Burak")
# print(index)

# isFound = message.startswith('H') #Cümlenin baş harfi
# isFound = message.endswith('z') #Cümlenin son harfi
# print(isFound)

# message = message.replace("Burak","Çınar")# Cümlede istediğimiz kelimeyi istediğimiz kelimeye çeviririz.
# message = message.replace(" ","*")#Bütün boşluklar yerine * koyar
# print(message)

message = message.center(50,"*")
print(message)


