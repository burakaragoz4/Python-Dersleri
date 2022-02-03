myList =[1,2,3]
# myString = "My String"

# print(len(myList))
# print(len(myString))
# print(type(myList))
# print(type(myString))

class Movie():
    def __init__(self,title,director,duration):
        self.title = title
        self.director = director
        self.duration = duration
        print("Movie Objesi Oluşturuldu")

    def __str__(self):
        return f"{self.title} by {self.director}"

    def __len__(self):
        return self.duration

    def __del__(self):
        print("Film Objesi Silindi")

m = Movie("Film Adı","Yönetmen Adı",120)

# print(str(myList))
print(str(m))
# print(str(myList))
# print(len(m))
