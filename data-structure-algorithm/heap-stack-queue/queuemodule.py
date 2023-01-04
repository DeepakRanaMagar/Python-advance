# implementation of the stack using queue module


from queue import LifoQueue

# STACK initalization
stack = LifoQueue(maxsize=5)

# qsize(): show no of elements in the stack
print("Total number of stack: ", stack.qsize())

stack.put('a')
stack.put('b')
stack.put('c')
stack.put('d')
stack.put('e')

print("Full: ", stack.full())
print("Total number of stack: ", stack.qsize())

print('\nElements popped from the stack')
print(stack.get())
print(stack.get())
print(stack.get())
print(stack.get())
print(stack.get())

 
print("\nEmpty: ", stack.empty())

