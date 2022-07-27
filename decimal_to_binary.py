'''
Recursion
Problem: Convert Decimal Number to Binary Number

Example:
    15 is '1111'
'''


def decimalToBinary(testVariable):
    # Base Case
    if testVariable <= 1:
        return str(testVariable)

    # Recursive Case

    # Get the reminder of the current node
    reminder = str(testVariable % 2)
    # Get the reminder of the previous node
    prvReminder = decimalToBinary(testVariable // 2)

    # Concatenate Previous reminder and current reminder and return
    return prvReminder + reminder

# EXECUTION
print(decimalToBinary(0))
print(decimalToBinary(11))
print(decimalToBinary(2))
print(decimalToBinary(5))

'''
OUTPUT:
0
1011
10
101
'''