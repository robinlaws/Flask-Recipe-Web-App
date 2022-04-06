import csv

all_recipes = []
fields = ['name', 'image', 'ingredients', 'instructions', 'servings', 'reviews', 'difficulty']


def write_to_file(filename):
    with open(filename, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(fields)
        for r in all_recipes:
            writer.writerow(
                [r.name, r.image, r.ingredients, r.instructions, r.servings, r.reviews, r.difficulty])


def read_from_file():
    with open('recipes.csv', 'r') as file:
        recipe_dict = {}
        reader = csv.reader(file)
        for rows in reader:
            recipe_dict[rows[0]] = {'image': rows[1],
                                    'ingredients': rows[2],
                                    'instructions': rows[3],
                                    'servings': rows[4],
                                    'reviews': rows[5],
                                    'difficulty': rows[6]}
    return recipe_dict


def get_all_recipes():
    return all_recipes


class CSVRecipes:
    def __init__(self, name, image, ingredients, instructions, servings, reviews, difficulty):
        self.name = name
        self.image = image
        self.ingredients = ingredients
        self.instructions = instructions
        self.servings = servings
        self.reviews = reviews
        self.difficulty = difficulty
        all_recipes.append(self)


CSVRecipes("Chicken and Veggie Stir-Fry", "chicken_and_veggie_stirfry.png",
           ["1lb chicken breast", "salt", "pepper", "1lb broccoli florets", "8 oz mushroom", "3 tbl oil",
            "3 cloves garlic",
            "1 tbl ginger", "1 cup chicken broth", "1 tbl brown sugar", "1/3 cup soy sauce",
            "1/4 cup flower"],
           [
               "In a large pan on medium-high heat, add oil and chicken. Season with salt and pepper and saute until brown",
               "Remove chicken, in the same pan heat oil add muchrooms and brocolli until tender.",
               "Remove veggies from pan, add oil and saute garlic and ginger. Add remaining sauce ingredients.",
               "Put chicken and veggies back in pan and stir until headed through.",
               "Serve with rice or noodles."],
           ["Serves 6", "Cook Time: 32 minutes", "Prep Time: 20 minutes"],
           [],
           "easy")
CSVRecipes("Butter Chicken", "butter_chicken.png",
           ["2lb boneless, skinless chicken breast", "salt", "pepper", "2 tsp chili powder",
            "1/2 tsp turmeric", "6 tbls butter", "1 1/2 cups yellow onion", "1 tsp cumin",
            "1 tsp cayenne pepper",
            "1 tbl ginger", "3 cloves garlic", "1 cinnamon stick", "14 oz tomato sauce", "1 cup water",
            "1 cup heavy cream",
            "rice", "fresh cilantro"],
           [
               "In a large bowl, season the chicken breast with salt, pepper, 1 teaspoon of chili powder, and the teaspoon of turmeric. Let sit for 15 minutes to marinate.",
               "Melt 2 tablespoons of butter in a large pot over medium heat. Brown the chicken, then remove from the pot.",
               "Melt another 2 tablespoons of butter in the pot, then add the onion, garam masala, remaining teaspoon of chili powder, the cumin, ginger, garlic, cayenne, cinnamon, salt and pepper. Cook until fragrant.",
               "Add the tomato sauce and bring to a simmer.",
               "Add the water and cream and return to a simmer.",
               "Return the chicken to the pot, cover, and simmer for another 10-15 minutes.",
               "Stir in the last 2 tablespoons of butter and season with more salt and pepper to taste.",
               "Serve the chicken over rice and garnish with cilantro."],
           ["Serves 4", "Total Time: 50 minutes", "Prep Time: 10 minutes", "Cook Time: 25 minutes"],
           [],
           "Medium")

CSVRecipes("Pesto Chicken", "pesto_chicken.png",
           ["2 tablespoons olive oil", "4 boneless, skinless chicken thighs, sliced", "salt", "pepper",
            "1 lb green beans", "2 cups cherry tomato", "½ cup basil pesto"],
           ["In a large pan, heat olive oil and add chicken thighs.",
            "Season with salt and pepper. When the chicken is completely cooked through, remove from pan.",
            "Slice into strips, and set aside.", "Add green beans and cook until crisp tender.",
            "Return the chicken strips to the pan, then add tomatoes and pesto. Stir until fully incorporated.",
            "Serve immediately or divide into 4 food storage containers and store in the refrigerator. Can be kept refrigerated for up to 4 days."],
           ["Serves 4", "Total Time: 22 minutes", "Prep Time: 10 minutes", "Cook Time: 12 minutes"],
           [],
           "Easy")

write_to_file('recipes.csv')
