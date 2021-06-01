import random
# find way to add/concatenate to my_foods extra meal
# create tiers of ingredients - main - secondary - optional
class meal:
    def __init__(self, name, ingr1, ingr2):
        self.name = name
        self.ingr1 = ingr1
        self.ingr2 = ingr2
#what if 3rd ingredient?

m = []
m.append(meal("spag bol", "pasta", "tomato sauce"))
m.append(meal("pizza", "tomato sauce", "pizza dough"))
m.append(meal("fried rice", "white rice", "courgette"))
m.append(meal("Nutella sandwich", "Nutella", "bread"))

### WORKS
#r = random.randint(0, len(m) - 1)
#print("Hey, you hungy? How does " + m[r].name + " sound?\n")
#print("You're gonna need \n - " + m[r].ingr1 + " \n - " + m[r].ingr2)

# it'd be cool to input an ingredient, and output suggestion meal
food = input("What ingredient do you have?\n -> ").lower()
for i in range(0, len(m)):
    if m[i].ingr1 == food:
        print("You can make {}".format(m[i].name))
        break
    elif m[i].ingr2 == food:
        print("You can make {}".format(m[i].name))
        break