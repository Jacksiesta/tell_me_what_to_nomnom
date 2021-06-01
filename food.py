import random
# find way to add/concatenate to my_foods extra meal

# array of easy meals I can prepare
my_foods = ["spag bol", "pizza", "fried rice"]

# array of ingredients
ingredients = ['pasta', 'tomato sauce', 'pizza dough', 'white rice', 'courgette', 'carrot']

class meal:
    def __init__(self, name, ingr1, ingr2):
        self.name = name
        self.ingr1 = ingr1
        self.ingr2 = ingr2

m1 = meal("spag bol", "pasta", "tomato sauce")
m2 = meal("pizza", "tomato sauce", "pizza dough")
m3 = meal("fried rice", "white rice", "courgette")


'''
yn = 'N'
while yn == 'N':
    print("Hey, how does :::" + my_foods[random.randint(0, 2)] + "::: sound?")
    value = input("-> Y/N\n")
    print("You entered {}".format(value))
    if value == 'Y':
        exit()
'''