class Pet:

    def __init__(self, Name, Age, Number_of_legs, Location, Climate):
        self.name = Name
        self.age = Age
        self.number_of_legs = Number_of_legs
        self.location = Location
        self.climate = Climate


    def description(self):
        print("Describe my self as : I am " + self.name + " I am " + str(self.age) + " years old")

    def speak(self, sound):
        print(f"Listen to me ... I am speaking: (sound)")



    def size(self):
        print("I am quiet big as I am " + str(self.age) + " years old")

    def description2(self):
        print("My name is " + self.name + " and I have " + str(self.number_of_legs) + " legs. I am quite " + self.climate + " as I live in a big " + self.location)


myPet = Pet("Tom",5,4,"Pet House","cold")
print(myPet.name)
print(myPet.description())
print(myPet.speak(1))
print(myPet.size())
print(myPet.size())
print(myPet.description2())
print(myPet.location)



