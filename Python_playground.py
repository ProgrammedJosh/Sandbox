import random
Family = ["Josh", "Suzie", "Lara", "Jacob", "Dominic", "Tori"]
<<<<<<< HEAD
print(random.choice(Family))

# Please iterate over the list you've created using a "for" loop.
# Use the for loop to print each item in the list.
# For guidance, refer to https://docs.python.org/3/tutorial/controlflow.html#for-statements

for a in Family:
    print(a, len(a), "Python", "Python")
    
Ages = [11, 14, 46, 45, 7, 2]
print(random.choice(Ages))
if random.choice(Ages) == 45:
    print("Jacob has been chosen!")

FamilyAges = {"Jacob": "45", "Lara": "46", "Suzie": "14", "Josh": "11", "Dominic": "7", "Tori": "2"}
# print(random.choice(FamilyAges))
for n,a in FamilyAges.items():
    print(n,"is ",a,"years old!")
=======
print(random.choice(Family), "!")
>>>>>>> 7edcf5e77256130dea9ab6fb6bc7d00762a3bdab
