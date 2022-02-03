# Inheritance (Kalıtım): Miras Alma

# Person => name, surname, age, eat(), run(), drink()
# Student(Person), Teacher(Person) 

# Animal => Dog(Animal), Cat(Animal)

class Person():
    def __init__(self,fname,sname):
        self.firstname = fname
        self.lastname = sname
        print("Person Created")

    def who_am_i(self):
        print("I am a Person")

    def eat(self):
        print("I am eating")

class Student(Person):
    def __init__(self,fname,sname,number):
        Person.__init__(self,fname,sname)
        self.studentNumber = number
        print("Student Created")
    # override
    def who_am_i(self):
        print("I am a Student")

    def sayHello(self):
          print("Hello I am a Student")

class Teacher(Person):
    def __init__(self,fname,sname,branch):
        super().__init__(fname,sname)
        self.branch = branch

    def who_am_i(self):
        print(f"I am a {self.branch} Teacher")


p1 = Person("Burak","Karagöz")
s1 = Student("Taner","Egehan",100)
t1 = Teacher("Serkan","Yılmaz","Math")

print(f"Adınız: {p1.firstname} ve Soyadınız: {p1.lastname}")
print(f"Adınız: {s1.firstname} ve Soyadınız: {s1.lastname}, Numaranız: {s1.studentNumber}")

p1.who_am_i()
s1.who_am_i()
t1.who_am_i()

p1.eat()
s1.eat()

s1.sayHello()

