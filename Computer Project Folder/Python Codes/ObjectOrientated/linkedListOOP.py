class Node:

    def __init__(self, data=None, next=None):

        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

def main():
# The head is the first node in a linked list declared as global
    global Head
    node1 = Node("Apple") #create the first node with data as Apple.
    Head = node1 # node1 is the Head of the list (first element)
# Other nodes are added as follows:
    node2 = Node("Orange")
    node3 = Node("Pear")
# creating pointers to link nodes together:
    node1.next = node2
    node2.next = node3
    node4 = Node("Pineapple")
    node3.next = node4
# node3.next is set to None by default

def print_List():  # node gives the head node
    # An example of printing the data of the list in order:
    node = Head
    while node != None:
        print(node.data)
        node = node.next
main()
print_List()

def InsertData(data,location):
    node = Head
    while node != None:
        if node.data == location:
            NewNode = Node(data)
            NewNode.next = node.next
            node = node.next

main()
InsertData("hello",0)
print_List()

def DeleteData(Head,data):
    current = Head
    previous = None
    found = False
    while not found:
        if current.data == data:
            found = True
        else:
            previous = current
            current = current.next

    if previous == None:
        Head = current.next
    else:
        previous.next = current.next

    return Head



