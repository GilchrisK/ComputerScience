# myStack = [" ", " ", " ", " ", " ", " ", " "]
#
# StackPointer = 0
# Max = len(myStack) - 1  # Max is the maximum number of Stack elements
#
#
# def push():
#     global Max              #THESE ARE GLOBAL AS IT ALLOWS THE VALUES OF MAX AND STACKPOINTER AT THE START OF THE CODE TO BE APART OF THE FUNCTION
#     global StackPointer
#
#     if StackPointer == Max:
#         print("Stack is full")
#     else:
#         data = input("enter name  ")
#         myStack[StackPointer] = data
#         StackPointer += 1
#
#
# def pop():
#     global Max
#     global StackPointer
#
#     if StackPointer == 0:
#         # return True
#         print("Stack is empty")
#
#     else:
#         # return False
#         StackPointer -= 1
#         data = myStack[StackPointer]
#         print("Popping " + str(data) + " from the stack")
#
#
#
# if __name__ == "__main__":
#
#     print (myStack)  # use pop or push to read from or add to stack.
#     push()
#     print (myStack)
#     push()
#     print (myStack)
#     push()
#     print (myStack)
#     push()
#     print (myStack)
#     pop()
#     print (myStack)
#     push()
#     print(myStack)



myStack = [" ", " ", " ", " ", " ", " ", " "]

StackPointer = 0
Max = len(myStack) - 1  # Max is the maximum number of Stack elements


def push():
    global Max              #THESE ARE GLOBAL AS IT ALLOWS THE VALUES OF MAX AND STACKPOINTER AT THE START OF THE CODE TO BE APART OF THE FUNCTION
    global StackPointer

    if StackPointer == Max:
        return True
    else:
        return False

def pop():
    global Max
    global StackPointer

    if StackPointer == 0:
        return True
    else:
        return False



if __name__ == "__main__":
    push()
    push()
    push()
    pop()
    pop()
    pop()
    push()

    if push() == True:
        print("Stack is full")
    else:
        data = input("enter name  ")
        myStack[StackPointer] = data
        StackPointer += 1

    if pop() == True:
        print("Stack is empty")
    else:
        StackPointer -= 1
        data = myStack[StackPointer]
        print("Popping " + str(data) + " from the stack")

  # use pop or push to read from or add to stack.


