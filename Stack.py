class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from an empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from an empty stack")

    def size(self):
        return len(self.items)

# Example usage:
stack = Stack()

# Push elements onto the stack
stack.push(1)
stack.push(2)
stack.push(3)

# Peek at the top element
print("Peek:", stack.peek())

# Pop elements from the stack
print("Pop:", stack.pop())
print("Pop:", stack.pop())

# Check if the stack is empty
print("Is empty:", stack.is_empty())

# Get the size of the stack
print("Size:", stack.size())
