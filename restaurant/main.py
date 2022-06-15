from kitchen import *
from menu import buildmenu

Foods = buildmenu(names, costs)

n = 1
for food in Foods:
    print(n, '. ', food)
    n = n + 1
