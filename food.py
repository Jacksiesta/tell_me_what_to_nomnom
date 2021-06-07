import random
# find way to add/concatenate to my_foods extra meal
# create tiers of ingredients - main - secondary - optional
class meal:
    def __init__(self, name, ingr1, ingr2):
        self.name = name
        self.ingr1 = ingr1
        self.ingr2 = ingr2
# what if 3rd ingredient?

# creates list of meals + ingr

m = []
m.append(meal("spag bol", "pasta", "tomato sauce"))
m.append(meal("pizza", "tomato sauce", "pizza dough"))
m.append(meal("fried rice", "white rice", "courgette"))
m.append(meal("Nutella sandwich", "Nutella", "bread"))
m.append(meal("Thuna sandwich", "bread", "thuna"))

### WORKS
#r = random.randint(0, len(m) - 1)
#print("Hey, you hungy? How does " + m[r].name + " sound?\n")
#print("You're gonna need \n - " + m[r].ingr1 + " \n - " + m[r].ingr2)



# it'd be cool to input an ingredient, and output suggestion meal
'''
food = input("What ingredient do you have in your fridge?\n -> ").lower()
for i in range(0, len(m)):
    if m[i].ingr1 == food:
        print("You can make {}".format(m[i].name))
        yn = input("Sounds good? Type y/n -> ").lower()
        if yn == 'y':
            print("Bon appetit!\n")
            break
    elif m[i].ingr2 == food:
        print("You can make {}".format(m[i].name))
        yn = input("Sounds good? Type y/n -> ").lower()
        if yn == 'y':
            print("Bon appetit!\n")
            break
'''

# list all possible meals

def list_all_meals():
    yn = input("Would you like to see all meals you are capable of making? y/n \n").lower()
    if yn == 'y':
        for i in range(0, len(m)):
            print(f"{i + 1}. {m[i].name}")
    if yn == 'n':
        print("oh well \n")

print(list_all_meals())

