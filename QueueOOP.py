class Queue():

    def __init__(self, given_size):
        self.head = 0
        self.tail = 0
        self.aList = []
        self.size = given_size


        while len(self.aList)< given_size:
            self.aList.append(" ")


    def isEmpty(self):
        if self.head == self.tail:
            return True
        else:
            return False

    def isFull(self):
        if self.head == 0 and self.tail == len(self.aList) - 1 or self.head == self.tail + 1:
            return True
        else:
            return False

    def enqueue(self,item):
        if self.isFull() == True:
            print("Error...The queue is full")
        else:
            self.tail += 1
            self.aList[self.tail] = item
            if self.tail == self.size:
                self.tail = 0
            #add the circular motion

    def dequeue(self):
        if self.isEmpty() == True:
            print("Error...The queue is empty")
        else:
            self.head += 1
            if self.head == self.size:
                self.head = 0



if __name__ == "__main__":
    myQueue = Queue(5)
    item = ("Hello")
    print(myQueue.head)
    print(myQueue.isEmpty())
    print(myQueue.isFull())
    print(myQueue.dequeue())
    print(myQueue.enqueue(item))
    print(myQueue.enqueue(item))
    print(myQueue.enqueue(item))
    print(myQueue.enqueue(item))
    print(myQueue.enqueue(item))
    print(myQueue.aList)


