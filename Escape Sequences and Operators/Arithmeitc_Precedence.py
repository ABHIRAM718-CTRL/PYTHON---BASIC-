"""
priority order of arithmetic operators in Python:
** - exponentiation
*,/,//,% - multiplication, division, floor division, modulo
+,- - addition, subtraction
This is the operator precedence in Python. 
"""

print(2 + 3 * 4) # 14 not 24
print(20 - 2**3) # 12 not 54

print((2 + 3) * 4)# If you want specific order , force it using parenthesis.