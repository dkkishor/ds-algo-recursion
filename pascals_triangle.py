'''
Recursion
Problem: Pascal's Triangle

Example:
Starting with 1 at the top, build next lines by taking sum of 2 numbers right above it
    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1

Solution:
Base case - if input is zero, return [1]
Recursion - List starts with [1] and ends with [1].
For the logic in the middle, initialize previous line using recursion,
loop through the index for remaining elements and add numbers from the previous line.
'''

def printPascal(testVariable):
  # Write your code here

  # Base Case
  if testVariable == 0:
      return [1]

  # Recursive Case:

  # Left and Right most nodes are always [1]

  # Set left most node to [1]
  line = [1]

  # Get the previous Line
  prvLine = printPascal(testVariable - 1)
  # Execute for loop only from second row onwards
  # And add elements in the middle by adding 2 consecutive values
  for i in range(len(prvLine) - 1):
      line.append(prvLine[i] + prvLine[i+1])


  # Set right most node to 1
  line += [1]

  return line


# EXECUTION
print(printPascal(5))
print(printPascal(1))
print(printPascal(0))
print(printPascal(2))

'''
OUTPUT:
[1, 5, 10, 10, 5, 1]
[1, 1]
[1]
[1, 2, 1]
'''