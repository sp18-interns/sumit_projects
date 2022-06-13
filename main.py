from dish_0 import *

quantity = random.choice(amount_of_ingredients)
ings = random.sample(ingredient, k=steps)  # use random.sample to generate unique ingredients and prevent duplicates
recipe = random.choice(cooking_phrases)
name = random.choice(recipe_name)
print(name)
for i in range(steps):
    ing = ings[i]
    print(ingredients_list(quantity, ing))

print("Recipe Instructions:")
for i in range(steps):
    ing = ings[i]
    print(recipe_instructions(recipe) + " " + ing)
