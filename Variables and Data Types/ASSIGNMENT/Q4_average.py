"""
Q4: A student scored marks in 3 subjects. Take all three as input,
calculate the total and average, and print both using an f-string.
"""
Sub1 = int(input("Enter marks for subject 1 out of 100: "))
Sub2 = int(input("Enter marks for subject 2 out of 100: "))
Sub3 = int(input("Enter marks for subject 3 out of 100: "))
T = Sub1+Sub2+Sub3
A = T/3
print(f"The total marks are {T} out of 300 , and the average marks are {A}")