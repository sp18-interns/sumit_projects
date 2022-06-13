import random

recipe_name = ["Dum Aloo Lakhnavi", "Honey Chilli Potatoes", "Potatoes with Garlic Cream", "Bangbang Batata",
               "Heeng Aur Dhaniye Ke Chatpate Aloo", "Aloo Lafde Wala", "Bewkoof aloo"]
amount_of_ingredients = ["30g", "40g", "50g", "60g", "70g", "80g", "90g", "100g", "110g", "120g"]
ingredient = ["eggs", "sugar", "salt", "butter", "milk", "bacon", "tomatoes", "pasta", "rice", "potatoes", "onions",
              "carrots", "all-purpose flour", "vermicelli", "cheese", "chicken", "spinach", "strawberry",
              "apples", "blueberries", "olive oil", "soy sauce", "corn", "shrimp", "mayonnaise"]
cooking_phrases = ["In a medium sized bowl, whisk together the", "In a large skillet over medium heat, stir-fry the",
                   "In a skillet, Sauté the", "In a large pot, boil the", "Thoroughly wash the", "Thinly slice the",
                   "Make small, 1-inch cubes by dicing up the", "Set the timer for 1 minute and microwave the",
                   "Using a blender, thoroughly blend the", "For 20 minutes in a 350°F oven, bake the"]

steps = 6


def ingredients_list(self, ing):
    quantity = random.choice(amount_of_ingredients)
    return "{} {}".format(quantity, ing)


def recipe_instructions(self):
    recipe = random.choice(cooking_phrases)
    return "{}".format(recipe)
