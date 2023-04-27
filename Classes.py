class Pets():
    def __init__(self, givenName, givenAge):
        self.name = givenName #the name is not private so you can change it(change it).
        self.__age = givenAge  # age is private so it CANNOT be changed

    def describe(self):
        return self.name + " I am " + str(self.__age) + " years old"

        # myPet.describe() #this will print the name + i am the age + years old
        # print(myPet.describe)#….error

    def speak(self, sound):
        print(self.name + " says " + sound)
        myPet = Pets("Max", 5)
        myPet.speak("Hello")



    def sleep(self):  # all Pets sleep silently
        print("Sleeping Silently")

    def ask(self, question):
        return (question)

        myPet = Pets("Max",5) #generates an object with name max and age 5

    def set_age(self, newAge):
        self.__age = newAge
        #here you can change the age

    def get_age(self):
        return self.__age


class Dog(Pets):  # dog inherits  all attributes and methods from Pets

    def __init__(self, givenspecies, givenname, givenage):
        self.species = givenspecies
        number_of_legs = 4  # all dogs have 4 legs
        super().__init__(givenname, givenage) # this means create a pet then make it as a dog. because it is from  the super class
                                                # go to Pets and run '__init__'


    def bark(self):
        print(" Woof .... Woof...Woof")


class Cat(Pets):  # Cat also inherits  attributes and methods from pets

    def __init__(self, givenbread, givenname, givenage):
        self.bread = givenbread
        number_of_legs = 4  # all cats have 4 legs
        super().__init__(givenname, givenage)

    def meow(self):
        print(" Meow .... meow..... Meow")

    def sleep(self):
        print("my name is  " + self.name +
              " I am closing my eyes slowly and ... Snore....Snore....Snore")
        myCat = Cat("felion","felix",5)
        print(myCat.meow())

    #--> Now the cat will sleep differently

if __name__ == '__main__':
    myDog = Dog("Bull dog", "Max", 8)
    myCat = Cat("Birman Cat", "Felix", 3)

    # print("the dog: " +myDog.species + " ... \n" + myDog.describe(),
    # "\nthe cat: " +myCat.bread + " says ...\n  " + myCat.describe())
    # myDog.speak("hello everyone I can Bark .. ")
    # myDog.bark()
    # myDog.sleep()
    # myCat.meow()
    # myCat.sleep()
    # myDog.ask(myCat.meow())    # interaction
    # myCat.ask(myDog.bark())    # interaction

    ############################################
    # trying methods which are not exist
    # print(myDog.colour)
    # myDog.breathe()
    ############################################

    ############################################
# using setter and getter
# print("my age before is " + str(myDog.get_age()))
# myDog.set_age(6)
# print("now my age is " +str(myDog.get_age()))

#############################################