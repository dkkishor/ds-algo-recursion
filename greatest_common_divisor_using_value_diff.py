'''
Subject: Recursion
Problem: Find the Greatest Common Divisor

Example:
Take two numbers 42 and 56.
42 can be completely divided by 1, 2, 3, 6, 7, 14, 21 and 42.
56 can be completely divided by 1, 2, 4, 7, 8, 14, 28 and 56.
Therefore the greatest common divisor of 42 and 56 is 14.

Solution:
This approach stores the diff of two values into one of the 2 variables whichever is greater.
'''

def gcd(testVariable1, testVariable2) :
  # Write your code here
  if testVariable1 == testVariable1:
      print(testVariable1)
      return testVariable1

  if testVariable1 > testVariable2:
      gcd(testVariable1 - testVariable2, testVariable2)
  else:
      gcd(testVariable1, testVariable2 - testVariable1)


gcd(56, 42)
gcd(6, 9)
gcd(14, 30)
gcd(23, 23)
gcd(43, 24)

'''
OUTPUT:
14
3
2
23
1
'''