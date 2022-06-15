
class Menu:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def getprice(self):
        return self.price

    def __str__(self):
        return self.name + ' : ' + str(self.getprice())


def buildmenu(names, costs):
    menu = []
    for i in range(len(names)):
        menu.append(Menu(names[i], costs[i]))
        return menu
