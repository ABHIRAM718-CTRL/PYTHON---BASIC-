"""
Q2: Take a number as input. Print whether it is even or odd using the %
operator and a comparison operator.
"""

A = int(input("Enter a number: "))
B = A % 2
even = B == 0
odd = B != 0
print(f"The number is even: {even}")
print(f"The number is odd: {odd}")
