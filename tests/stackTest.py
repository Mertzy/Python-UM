from useful_methods import *

stack = Stack()

stack.push(5)
print("Pushed 5 onto the stack.")
stack.push("hello world")
print("Pushed 'hello world' onto the stack.")
stack.push(7.34)
print("Pushed 7.34 onto the stack.")
stack.push("Stacking this stuff!")
print("Pushed 'Stacking this stuff' onto the stack.")
print("")
print("This is the top of the stack: " + stack.top())
print("")
stack.pop()
print("Top of stack..." + str(stack.top()) + "...popped off the stack.")
stack.pop()
print("Top of stack..." + str(stack.top()) + "...popped off the stack.")
stack.pop()
print("Top of stack..." + str(stack.top()) + "...popped off the stack.")
print("")
input("Press Enter to quit: ")