#############################################
#Doesnt Work
#
##########################################
class Students():

    def __init__(self):
        self.name = None
        self.record_number = None

def data(name, record_number):
    student1 = Students()

    student1.name = "Sam"
    student1.record_number = 2345



def main():
    register = []
    student1 = data("Sam", 2345)
    register.append(student1)

    if student1 in register:
        return True

main()

if __name__ == '__main__':
    if main == True:
        print("valid")

