# Importing deque module from collections library
from collections import deque

# Defining a function to check if opening and closing brackets match
def matches(opener, closer):
    pairs = {'(': ')', '[': ']', '{': '}'}
    return pairs.get(opener) == closer

# Defining a function to check if a string of brackets is balanced
def checker(test_string):
    stack = deque()
    balanced = True
    index = 0

    # Loop through the string until either the string is not balanced or the end of the string is reached
    while balanced == True and index < len(test_string):

        symbol = test_string[index]
        if symbol in '({[':
            stack.append(symbol)
        else:
            # If the stack is empty, the string is not balanced
            if len(stack) == 0:
                balanced = False
            else:
                # Pop the top element from the stack
                top = stack.pop()
                # Check if the opening and closing brackets match
                if not matches(top, symbol):
                    balanced = False

        index += 1 # Move to the next symbol in the string

    # If the string is balanced and the stack is empty, return True
    if balanced == True and len(stack) == 0:
        return True
    else:
        return False
