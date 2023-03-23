MAX_SIZE = 5
stack = []
top = -1

def is_full(top):

    if top == MAX_SIZE - 1:
        return True
    else:
        return False

def push(stack, top,data):

    if is_full() == True:
        print("Stack is full")
    else:
        top = top + 1
        stack[top] = data
    return top
#NOT WORKINGGGGGGGGG

