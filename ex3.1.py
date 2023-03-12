# In this exercise, you are going to produce a stack-based interpreter that can compute the result
# of such an expression. Your code (ex3.1.py) must:
# 1. Receive a string representing an expression as a command line parameter [1 pt].
# 2. Implement a stack data structure as discussed in lab and class [3 pts].
# 3. Using the stack, compute the overall result of an expression [6 pts].


# READ ME -> the command line variable must be surrounded by double quotes for this implementation. Example: "(+ 1 5)"

import sys
import re

def evaluate_expression(expression):
    stack = []
    expressionValues = re.findall(r'\(|\)|[-+]?\d*\.\d+|\d+|[+\-*/]|\S+', expression)
   # print(expressionValues)

    for val in expressionValues:
        
        if val == '(':
            continue
        elif val == ')':
            operand2 = stack.pop()
            operand1 = stack.pop()
            operator = stack.pop()
            if operator == '+':
                stack.append(operand1 + operand2)
            elif operator == '-':
                stack.append(operand1 - operand2)
            elif operator == '*':
                stack.append(operand1 * operand2)
            elif operator == '/':
                stack.append(operand1 / operand2)
            else:
                print("Error: invalid operator.")
                sys.exit(1)

        elif val in ['+', '-', '*', '/']:
            stack.append(val)   

        else:
            stack.append(int(val))

    return stack.pop()

    
#main

if "\'" in sys.argv[1]:
    print("The commandline input expression must be surrounded by double quotes.")
    print("Example: \"(+ 1 5)\"")
    sys.exit(1)

print(sys.argv[1])

result = evaluate_expression(sys.argv[1])
resultToPrint = str(result)

if len(resultToPrint) == 3:
    if resultToPrint[2] =='0':
        print(int(result))
else:
    print(result)


