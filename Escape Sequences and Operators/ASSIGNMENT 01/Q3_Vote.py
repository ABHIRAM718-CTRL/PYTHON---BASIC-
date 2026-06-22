"""
Q3: Take the user's age as input. Check and print whether they are eligible
to vote (age >= 18) and whether they are a senior citizen (age >= 60).
Print both results.
"""

age = int(input("Enter the age of the voter: "))
Gen = age >= 18
Sen = age >= 60

print("Eligible to vote:", Gen)
print("Senior citizen:", Sen)
