# Class

class Person():
    # Class attributes her zaman kullanılacak objeleri burda tanımlaya biliriz
    address = "No Information"
    # Constructor (Yapıcı Method)

    def __init__(self,name,year):
    # Object attributes
        self.name = name 
        self.year = year
    print("init methodu çalıştı")

    # methods

# Object, (instance)

p1 = Person(name="Burak",year = 1999)
p2 = Person(name="Taner",year = 2000)

# Updating

p1.name = "Ahmet"
p1.address = "Ankara"

p2.address = "Bartın"
# Accessing Object Attributes
print(f"p1: name: {p1.name}. Year: {p1.year} Address: {p1.address}")
print(f"p2: name: {p2.name}. Year: {p2.year} Address: {p2.address}")

