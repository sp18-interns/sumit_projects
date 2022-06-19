from kitchen_list import *
from menu import buildmenu
from quantity_plate_list import amount_of_Dish
import random


Foods = buildmenu(names, costs)
plates = amount_of_Dish
n = 1
for food in Foods:
    print(n, '. ', food)
    n = n + 1
    print (random.choice(plates))