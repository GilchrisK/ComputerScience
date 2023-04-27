class Car():

    def __init__(self, model, Color, company, speed_limit):

        self.color = Color
        self.company = company
        self.speed_limit = speed_limit
        self.model = model

    def start(self):
        print("started")

    def stop(self):
        print("stopped")

    def accelarate(self):
        print("accelarating...")

    def change_gear(self, gear_type):
        print("gear changed")

myAudi = Car("A6", "red", "audi", 80)
print(myAudi.speed_limit)
print(myAudi.color)
print(myAudi.change_gear(1))
print(myAudi.start())
print(myAudi.company)

