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

# Push some values
stack.push(1)
stack.push(2)
stack.push(3)

# Pop some values
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())


#my implementation