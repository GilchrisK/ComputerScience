class Stack():


    def __init__(self,size):   #SIZE is a local variable set by the user
        self.__sp= 0        #These are private
        self.__alist = []
        self.stacksize = size
        while len(self.__alist)<size: #we dont use slef outside of the object because we dont know self in the object.
            self.__alist.append(" ")

    def isEmpty(self):
        if self.__sp == 0:
            return True
        else:
            return False

    def isFull(self):
        if self.__sp == self.stacksize:
            return True
        else:
            return False

    def push(self,item):
        if self.isFull():
            print("ERROR....Your stack is full")
        else:
            self.__alist[self.__sp] = item
            self.__sp += 1

    def pop(self):
        if self.isEmpty():
            print("ERROR...Your list is empty")
        else:
            self.__sp -= 1
            self.__alist[self.__sp]

    def get__sp(self):
        return self.__sp

    def get__alist(self):
        return self.__alist


if __name__ == "__main__":
    mystack = Stack(3)


    print(mystack.isFull())
    print(mystack.isEmpty())

    print(mystack.get__sp())


    mystack.push("Chris")
    mystack.push("paul")
    mystack.push("Chris")

    print(mystack.get__alist())

    print(mystack.get__sp())
    print(mystack.get__alist())
    mystack.pop()
    mystack.pop()
    print(mystack.get__alist())

    print(mystack.get__alist())
    print(mystack.isFull())
    print(mystack.isEmpty())
    print(mystack.isFull())




