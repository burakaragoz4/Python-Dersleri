# # Class

# class Person():
#     # Class attributes her zaman kullanılacak objeleri burda tanımlaya biliriz
#     address = "No Information"

#     # Constructor (Yapıcı Method)
#     def __init__(self,name,year):
#     # Object attributes
#         self.name = name 
#         self.year = year
    
#     # instance methods
#     def intro(self):
#         print("Hello There.I am " +self.name)
    
#     # instance methods
#     def calculateAge(self):
#         return 2021 - self.year


# # Object, (instance)
# p1 = Person(name="Burak",year = 1999)
# p2 = Person(name="Taner",year = 2000)

# # Updating

# # p1.name = "Ahmet"
# p1.address = "Ankara"
# p2.address = "Bartın"

# # Accessing Object Attributes
# p1.intro()
# p2.intro()

# print(f"Adım: {p1.name} ve yaşım: {p1.calculateAge()} ")
# print(f"Adım: {p2.name} ve yaşım: {p2.calculateAge()}")

class Circle:
    # Class Object Attribute
    pi = 3.14

    def __init__(self,yaricap = 1):
        self.yaricap = yaricap

    # Methods
    def cevreHesapla(self):
        return round(2 * self.pi * self.yaricap,2)
    
    def alanHesapla(self):
        return round(self.pi * (self.yaricap ** 2),2) # Virgülden sonra 2 basamak 

c1 = Circle() #Circle içerisine yarıçap belirtirmezseniz yarıçapı 1 kabul eder yukarıda tanımladığımız için
c2 = Circle(5)

print(f"C1 : Alan = {c1.alanHesapla()} ve Çevre = {c1.cevreHesapla()}")
print(f"C2 : Alan = {c2.alanHesapla()} ve Çevre = {c2.cevreHesapla()}")

