'''
Subject: Recursion
Problem: Find the Greatest Common Divisor

Example:
Take two numbers 42 and 56.
42 can be completely divided by 1, 2, 3, 6, 7, 14, 21 and 42.
56 can be completely divided by 1, 2, 4, 7, 8, 14, 28 and 56.
Therefore the greatest common divisor of 42 and 56 is 14.

Solution:
This approach is not the best approach but close to Brute Force.
It reduces the values by half in each iteration and if that remainder can divide the number
it will add the number and quotient to the final array.

Once we find divisors for input values, it then intersects the 2 lists to find common elements, sorts the list
and takes the last value which will be the maximum common divisor
'''

import math

def gcd(testVariable1, testVariable2) :
  # Write your code here
  divList1, divList2 = [], []
  divisors(testVariable1, testVariable1, divList1)
  divisors(testVariable2, testVariable2, divList2)

  gcdList = list(set(divList1) & set(divList2))
  gcdList.sort()
  print(gcdList[-1])
  return gcdList[-1]


def divisors(testVariable, div, divList):
    if div <= 1 and div < testVariable // div:
        return
    elif testVariable%div == 0:
        divList.append(testVariable // div)
        if (div != testVariable // div):
            divList.append(div)

    div = math.ceil(div / 2)
    divisors(testVariable, div, divList)
    return


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