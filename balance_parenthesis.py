'''
Recursion
Problem: Balance Paranthesis

Example:
    () = True
    (  = False
    )( = False
    () = True
'''

def balanced(testVariable, startIndex = 0, netParanthesis = 0) :
  # Base Case 1
  if startIndex == len(testVariable):
      return netParanthesis == 0

  # Base Case 2
  if netParanthesis < 0:
      return False

  # Recursive Case

  # Increment netParanthesis for every open
  if testVariable[startIndex] == "(":
      return balanced(testVariable, startIndex + 1, netParanthesis + 1)
  # Decrement netParanthesis for every close
  elif testVariable[startIndex] == ")":
      return balanced(testVariable, startIndex + 1, netParanthesis - 1)


# EXECUTION
print(balanced([')', '(']))
print(balanced(['(', ')', '(', ')']))
print(balanced(['(', '(', ')', ')', '(', ')']))

'''
OUTPUT:
False
True
True
'''