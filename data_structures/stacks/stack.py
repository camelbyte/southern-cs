class Stack:

    """
    This class implements a stack data structure with a list

    """
    def __init__(self):
        # stack is initialized as a list to hold the operands, operators and result.
        self.items = []
    
    # checks if the stack is empty
    def is_empty(self):
        return len(self.items) == 0

    #push an item onto the stack
    def push(self, item):
        self.items.append(item)

    # pop the item
    def pop(self):
        if not self.is_empty():
            return self.items.pop()

        else:
            print("empty stack. ")
    # peek the item
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else: 
            print("empty stack. ")

    # get the size of the stack 
    def size(self):
        return len(self.items)



