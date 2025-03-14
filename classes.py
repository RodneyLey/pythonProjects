class Mwales:
    def __init__(self,name, age, location):
        self.name = name
        self.age = age
        self.location = location
    def doubleAge (self):
        self.age =self.age * 2
     


bigBro = Mwales("Rodney", 29, "Canada")
bigSiz = Mwales("Laureen", 31, "Komarock")
smallBro = Mwales ("Prince", 15, "Machakos")
father = Mwales("Maurice", 55, "Ngong")
mother = Mwales("Connie", 55, "Ngong")


print (f"Our mother {mother.name} is currently at {mother.location} and is {mother.age} old")
mother.doubleAge()
print (f"Our mother {mother.name} double age is {mother.age}")
print(mother.age)