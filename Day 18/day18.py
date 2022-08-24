# Implementation using Shunting Yard Algorithm
# To remember this algorthim (of course you don't have to, but in case if you still wanna do it), picture a Y - 
# where the right branch has the infix string, and the vertical bar is the stack and the left branch is the 
# postfix string. The digits go straight from left to right branch. However, operators drop down the stack.
# Based on precedence the operators get up the stack make room for operators having lower or equal precedence.
# And for brackets operators go up the stack only when we encounter a right bracket ')'.
import operator

def main():
    data = open("18.txt", "r").read()

    lines = [x for x in data.split("\n") if x != '']

    # Part 1
    precedence = {'+': 0, '*': 0}
    print(sol(lines, precedence))
    
    # Part 2
    precedence = {'+': 1, '*': 0}
    print(sol(lines, precedence))


def sol(lines, precedence):
    result = 0
    for line in lines:
        result += evaluate_postfix(convert_to_postfix(line.replace(" ", ""), precedence))

    return result

"""Algorithm
1. Scan the infix expression from left to right. 
2. If the scanned character is an operand, output it. 
3. Else, 
      1 If the precedence of the scanned operator is greater than the precedence of the operator in the stack(or the stack is empty           or the stack contains a ‘(‘ ), push it. 
      2 Else, Pop all the operators from the stack which are greater than or equal to in precedence than that of the scanned operator. After doing that Push the scanned operator to the stack. (If you encounter parenthesis while popping then stop there and push the scanned operator in the stack.) 
4. If the scanned character is an ‘(‘, push it to the stack. 
5. If the scanned character is an ‘)’, pop the stack and and output it until a ‘(‘ is encountered, and discard both the parenthesis. 
6. Repeat steps 2-6 until infix expression is scanned. 
7. Print the output 
8. Pop and output from the stack until it is not empty.

- Reference: GoG
"""

def convert_to_postfix(infix, precedence):
    OPERATOR = ['+', '*']
    BRACKETS = ['(', ')']

    postfix = ""
    stack = []
    for c in infix:
        if c in OPERATOR:
            if len(stack) == 0 or stack[-1] in BRACKETS or precedence[c] > precedence[stack[-1]]:
                stack.append(c)
                
            else:
                while len(stack) > 0 and stack[-1] not in BRACKETS and precedence[c] <= precedence[stack[-1]] and (m := stack.pop()) in OPERATOR:
                    postfix += m

                stack.append(c)
        
        elif c == '(':
            stack.append(c)
        
        elif c == ')':
            # Though it's subtle the left bracket '(' will be removed from the
            # stack with the last pop for which m will not be an operator and 
            # the loop will break simultaneously.
            while len(stack) > 0 and (m := stack.pop()) in OPERATOR:
                postfix += m

        else:
            postfix += c
    
    # Unload the remaining operators (poping from it until empty)
    postfix = postfix + "".join(reversed(stack))

    return postfix


"""
1) Create a stack to store operands (or values).
2) Scan the given expression and do following for every scanned element.
    a) If the element is a number, push it into the stack
    b) If the element is a operator, pop operands for the operator from stack. Evaluate the operator and push the result back to the stack
3) When the expression is ended, the number in the stack is the final answer

- Reference GoG
"""

def evaluate_postfix(postfix):
    OPERATOR = {'+': operator.add, '*': operator.mul}

    operand_stack = []
    for c in postfix:
        if c not in OPERATOR:
            operand_stack.append(c)

        else:
            n1 = int(operand_stack.pop())
            n2 = int(operand_stack.pop())
            operand_stack.append(OPERATOR[c](n1, n2))
            
    return operand_stack[0]


main()