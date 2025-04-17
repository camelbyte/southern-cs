"""
    ____________Stacks____________

    A stack is a data structure that follows the Last In First Out (LIFO) principle.
    
    ____________Methods____________

    Push: Adds a new element on the stack.
    Pop: Removes and returns the top element from the stack.
    Peek: Returns the top element on the stack.
    isEmpty: Checks if the stack is empty.
    Size: Finds the number of elements in the stack.

"""

class Stack:
    def __init__(self):
        self.stack = []
        
        # stack methods are push, pop, peek, is_empty, reverse.


    def push(self, item):
            self.stack.append(item)
            

    def pop(self):
        """
        Description: If the stack is not empty, remove and return the top item so I can 
        see what was popped.
        """
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("pop from empty stack")


            
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("peek from empty stack")



    def is_empty(self):
        return len(self.stack) == 0


    def reverse(self):
        return self.stack[::-1]
    


# my numbers list 
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Instanstiating the stack class with an object called 's'.
s = Stack()

# This loop iterates through the nums list and shows how each number is pushed onto the stack.
# This is helpful for me to visualize the stack as it's being built. 

print("Pushing elements onto the stack:")
for num in nums:
    s.push(num)
    print(s.stack)


top_elemment = s.peek()
print("Top element:", top_elemment)

# Incorrect: print(s.length())
# Correct way:
print("Length of stack is:", len(s.stack))


# Reverse the stack using the reverse method, I can also use print(s(reversed(s.stack)))
print(s.reverse())

# Slicing the stack: The format is:  sequence[start:stop:step]
# s.stack[::2] means first(:) last(:) step=2
# This means from start to finish, take every sencond element. 

print("Print every second element in the stack.")
print(nums[::2])
     

new_stack = Stack()

new_stack.push(1)
new_stack.push(2)
new_stack.push(3)

print("New stack:", new_stack.stack)

# trying to get 213


def form(new_stack):

    a = [new_stack.pop() for _ in range(len(new_stack.stack))]
    return a


print("Formed stack:", form(new_stack))


# This is a test to see if the stack is empty.
print(s.is_empty())


def test_stack(new_stack):
    i = new_stack.pop(2)
    print(i)





