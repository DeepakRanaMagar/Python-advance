# implementation methods: list, collections.deque, queue.LifoQueue

from collections import deque


stack  = deque()

stack.append('a')
stack.append('b')
stack.append('c')

print("Initial Stack", stack)

print("\nElements popped from the stack are: ")
print(stack.pop())

print("\nAfter popped elements:")
print(stack)

