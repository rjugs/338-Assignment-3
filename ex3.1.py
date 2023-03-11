# In this exercise, you are going to produce a stack-based interpreter that can compute the result
# of such an expression. Your code (ex3.1.py) must:
# 1. Receive a string representing an expression as a command line parameter [1 pt].
# 2. Implement a stack data structure as discussed in lab and class [3 pts].
# 3. Using the stack, compute the overall result of an expression [6 pts].



# 1. The code below implements a barebone linked list (by cutting some corners)

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class List:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, val):
        if self.head is None:
            self.head = ListNode(val)
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = ListNode(val)
        self.size += 1

    def getListHead(self):
        return self.head

    def getNextNode(self, node):
        return node.next

    def getLastNode(self):
        node = self.head
        while node.next is not None:
            node = node.next
        return node


# Stack implementation based on 'List' class above

class Stack:
    def __init__(self):
        self.list = List()

    def push(self, val):
        node = ListNode(val)
        node.next = self.list.head
        self.list.head = node
        self.list.size += 1

    def pop(self):
        if self.list.head == None:
            return None
        else:
            val = self.list.head.val
            self.list.head = self.list.head.next
            self.list.size -= 1
            return val

# Examples of use:


# Create a stack
stack = Stack()

# Push some values (push each operand and remmeber the order)
stack.push(1)
stack.push(2)
stack.push(3)

# Pop some values (build equation using pop)

print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print("end of lab work")


#my implementation

# import sys

# if len(sys.argv) != 2:
#     print("Usage: python my_script.py <polish_notation_expression>")
#     sys.exit(1)

# tokens = sys.argv[1].split()

# stack = []

# for token in reversed(tokens):
#     if token.isdigit():
#         stack.append(int(token))
#     else:
#         try:
#             op2 = stack.pop()
#             op1 = stack.pop()
#         except IndexError:
#             print("Error: not enough operands.")
#             sys.exit(1)
#         if token == '+':
#             result = op1 + op2
#         elif token == '-':
#             result = op1 - op2
#         elif token == '*':
#             result = op1 * op2
#         elif token == '/':
#             result = op1 / op2
#         else:
#             print("Error: invalid operator.")
#             sys.exit(1)
#         stack.append(result)

# if len(stack) != 1:
#     print("Error: too many operands.")
#     sys.exit(1)

# print("The result is:", stack[0])

import sys

def evaluate_expression(expression):
    stack = []
    tokens = expression.split()

    for token in reversed(tokens):
        if token.isdigit():
            stack.append(int(token))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()

            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                result = operand1 / operand2
            else:
                print("Error: invalid operator.")
                sys.exit(1)

            stack.append(result)

    return stack.pop()

if len(sys.argv) != 2:
    print("Usage: python my_script.py 'expression'")
    sys.exit(1)

result = evaluate_expression(sys.argv[1])

print("The result is:", result)



