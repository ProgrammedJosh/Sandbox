import random
Family = ["Josh", "Suzie", "Lara", "Jacob", "Dominic", "Tori"]
print(random.choice(Family))

# Please iterate over the list you've created using a "for" loop.
# Use the loop to print each item in the list.

for a in Family:
    print(a, len(a), "Python", "Python")

Ages = [11, 14, 46, 45, 7, 2]
print(random.choice(Ages))

# Make a dictionary of names and ages
# Iterate over the dictionary to print all names and ages.

FamilyAges = {"Jacob": "45", "Lara": "46", "Suzie": "14", "Josh": "11", "Dominic": "7", "Tori": "2"}
for n,a in FamilyAges.items():
    print(n,"is",a,"years old!")