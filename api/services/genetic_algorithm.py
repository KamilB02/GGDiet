import random
from api.services.all_recipes import available_recipes

used_recipes = set()


user_requirements = {
    'calories': 1903,
    'protein': 119,
    'carbs': 238,
    'fats': 53,
    'required_lunch': [

    ],
    'unwanted_ingredients': [
        'mleko',
        'tofu'
    ]
}

required_lunch = user_requirements['required_lunch']
unwanted_ingredients = user_requirements['unwanted_ingredients']

class DietPlan:
    def __init__(self, breakfast1, breakfast2, lunch, tea, dinner):
        self.breakfast1 = breakfast1
        self.breakfast2 = breakfast2
        self.lunch = lunch
        self.tea = tea
        self.dinner = dinner

        self.calories_breakfast1 = sum(recipe['calories'] for recipe in self.breakfast1)
        self.calories_breakfast2 = sum(recipe['calories'] for recipe in self.breakfast2)
        self.calories_lunch = sum(recipe['calories'] for recipe in self.lunch)
        self.calories_tea = sum(recipe['calories'] for recipe in self.tea)
        self.calories_dinner = sum(recipe['calories'] for recipe in self.dinner)

        self.recipes = self.breakfast1 + self.breakfast2 + self.lunch + self.tea + self.dinner
        self.calories = sum(recipe['calories'] for recipe in self.recipes)
        self.macros = self.calculate_macros()

    def calculate_macros(self):
        total_macros = {'protein': 0, 'carbs': 0, 'fats': 0}
        for recipe in self.recipes:
            for macro, value in recipe['macros'].items():
                total_macros[macro] += value
        return total_macros


def generate_initial_population(user_requirements, size=3000):
    population = []

    if required_lunch:
        lunch_recipes = [recipe for recipe in available_recipes if recipe['name'] in required_lunch]
    else:
        lunch_recipes = [recipe for recipe in available_recipes if 'lunch' in recipe['meal_type'] and recipe['name'] not in used_recipes and not any(ingredient in unwanted_ingredients for ingredient in recipe['ingredients'])]

    breakfast_recipes = [recipe for recipe in available_recipes if 'breakfast' in recipe['meal_type'] and recipe['name'] not in used_recipes and not any(ingredient in unwanted_ingredients for ingredient in recipe['ingredients'])]

    dinner_recipes = [recipe for recipe in available_recipes if 'dinner' in recipe['meal_type'] and recipe['name'] not in used_recipes and not any(ingredient in unwanted_ingredients for ingredient in recipe['ingredients'])]

    for _ in range(size):

        selected_breakfast1 = random.sample(breakfast_recipes, k=1)
        selected_breakfast2 = random.sample(breakfast_recipes, k=1)
        selected_lunch = random.sample(lunch_recipes, k=1)
        selected_tea = random.sample(breakfast_recipes, k=1)
        selected_dinner = random.sample(dinner_recipes, k=1)

        while selected_dinner[0] == selected_lunch[0]:
            selected_dinner = random.sample(dinner_recipes, k=1)

        diet_plan = DietPlan(
            breakfast1=selected_breakfast1,
            breakfast2=selected_breakfast2,
            lunch=selected_lunch,
            tea=selected_tea,
            dinner=selected_dinner
        )

        population.append(diet_plan)

    return population


def fitness(plan, user_requirements):
    score = 0

    # 1. Punkty za ogólną zgodność kaloryczną
    calorie_diff = abs(plan.calories - user_requirements['calories'])
    if calorie_diff <= 20:
        score += 120
    elif calorie_diff <= 50:
        score += 80
    elif calorie_diff <= 100:
        score += 50
    else:
        score -= calorie_diff * 2

    # 2. Punkty za białko
    protein_diff = abs(plan.macros['protein'] - user_requirements['protein'])
    if protein_diff <= 4:
        score += 125
    elif protein_diff <= 8:
        score += 75
    elif protein_diff <= 12:
        score += 40
    else:
        score -= protein_diff * 2

    # 3. Punkty za węglowodany
    carb_diff = abs(plan.macros['carbs'] - user_requirements['carbs'])
    if carb_diff <= 4:
        score += 125
    elif carb_diff <= 8:
        score += 75
    elif carb_diff <= 12:
        score += 40
    else:
        score -= carb_diff * 2

    # 4. Punkty za tłuszcze
    fat_diff = abs(plan.macros['fats'] - user_requirements['fats'])
    if fat_diff <= 4:
        score += 125
    elif fat_diff <= 8:
        score += 75
    elif fat_diff <= 12:
        score += 40
    else:
        score -= fat_diff * 2

    # 5. Procentowy rozkład kaloryczności posiłków
    if 0.18 <= plan.calories_breakfast1 / user_requirements['calories'] <= 0.22:
        score += 80
    if 0.10 <= plan.calories_breakfast2 / user_requirements['calories'] <= 0.12:
        score += 50
    if 0.30 <= plan.calories_lunch / user_requirements['calories'] <= 0.35:
        score += 80
    if 0.10 <= plan.calories_tea / user_requirements['calories'] <= 0.15:
        score += 50
    if 0.25 <= plan.calories_dinner / user_requirements['calories'] <= 0.30:
        score += 80

    # 6. Zmienność posiłków
    unique_meals = len(set([recipe['name'] for recipe in plan.recipes]))
    score += unique_meals * 10

    # 7. Wprowadzenie współczynnika zgodności
    total_match_ratio = (1 - calorie_diff / user_requirements['calories']) * 100
    score += total_match_ratio

    return score


# Algorytm genetyczny
def genetic_algorithm(user_requirements, generations=5000, additional_generations=5000, max_extra_generations=4):
    def generate_population():
        return generate_initial_population(user_requirements)

    population = generate_population()

    if required_lunch:
        lunch_recipes = [recipe for recipe in available_recipes if recipe['name'] in required_lunch]
    else:
        lunch_recipes = [recipe for recipe in available_recipes if'lunch' in recipe['meal_type'] and recipe['name'] not in used_recipes and not any(ingredient in unwanted_ingredients for ingredient in recipe['ingredients'])]

    breakfast_recipes = [recipe for recipe in available_recipes if 'breakfast' in recipe['meal_type'] and recipe['name'] not in used_recipes and not any(ingredient in unwanted_ingredients for ingredient in recipe['ingredients'])]
    dinner_recipes = [recipe for recipe in available_recipes if 'dinner' in recipe['meal_type'] and recipe['name'] not in used_recipes and not any(ingredient in unwanted_ingredients for ingredient in recipe['ingredients'])]

    extra_generations = 0

    while extra_generations <= max_extra_generations:
        for generation in range(generations):
            population.sort(key=lambda x: fitness(x, user_requirements), reverse=True)
            new_population = population[:30]

            while len(new_population) < 60:
                parent1, parent2 = random.sample(new_population[:30], 2)

                crossover_breakfast1 = random.sample(parent1.breakfast1 + parent2.breakfast1, k=1)
                crossover_breakfast2 = random.sample(parent1.breakfast2 + parent2.breakfast2, k=1)
                crossover_lunch = random.sample(parent1.lunch + parent2.lunch, k=1)
                crossover_tea = random.sample(parent1.tea + parent2.tea, k=1)
                crossover_dinners = random.sample(parent1.dinner + parent2.dinner, k=1)

                while crossover_dinners[0] == crossover_lunch[0]:
                    crossover_dinners = random.sample(parent1.dinner + parent2.dinner, k=1)

                while crossover_breakfast1[0] == crossover_breakfast2[0]:
                    crossover_breakfast1 = random.sample(breakfast_recipes, k=1)

                new_population.append(DietPlan(crossover_breakfast1, crossover_breakfast2, crossover_lunch, crossover_tea, crossover_dinners))

            for plan in new_population:
                if random.random() < 0.2:
                    if random.random() < 0.5:
                        plan.breakfast1[0] = random.choice(breakfast_recipes)
                    if random.random() < 0.5:
                        plan.breakfast2[0] = random.choice(breakfast_recipes)
                    if random.random() < 0.5:
                        plan.lunch[0] = random.choice(lunch_recipes)
                    if random.random() < 0.5:
                        plan.tea[0] = random.choice(breakfast_recipes)
                    if random.random() < 0.5:
                        plan.dinner[0] = random.choice(dinner_recipes)

                    while plan.dinner[0] == plan.lunch[0]:
                        plan.dinner[0] = random.choice(dinner_recipes)

                    # Aktualizacja kalorii i makroskładników po mutacji
                    plan.recipes = plan.breakfast1 + plan.breakfast2 + plan.lunch + plan.tea + plan.dinner
                    plan.calories = sum(recipe['calories'] for recipe in plan.recipes)
                    plan.macros = plan.calculate_macros()

            population = new_population

        best_plan = population[0]

        calories_difference = abs(best_plan.calories - user_requirements['calories'])
        protein_difference = abs(best_plan.macros['protein'] - user_requirements['protein'])
        carbs_difference = abs(best_plan.macros['carbs'] - user_requirements['carbs'])
        fats_difference = abs(best_plan.macros['fats'] - user_requirements['fats'])

        if (calories_difference <= 70 and protein_difference <= 15 and carbs_difference <= 20 and fats_difference <= 10
                and best_plan.calories_lunch > best_plan.calories_breakfast1 and best_plan.calories_lunch > best_plan.calories_dinner):
            print("Znaleziono plan")
            return best_plan
        else:
            print("Nie znaleziono, szukam dalej")
            generations = additional_generations
            extra_generations += 1

        if extra_generations > max_extra_generations:
            print("Nie znaleziono odpowiedniego planu, resetowanie populacji...")
            population = generate_population()
            extra_generations = 0
            generations = 5000

    return best_plan

#best_plan = genetic_algorithm(user_requirements)

#print("Najlepszy plan dietetyczny :")
#for recipe in best_plan.recipes:
#    print(recipe['name'])

#print()
#print("Kalorie:", best_plan.calories)
#print()
#print("Kalorie sniadania:", best_plan.calories_breakfast1)
#print("Kalorie sniadania2:", best_plan.calories_breakfast2)
#print("Kalorie obiad:", best_plan.calories_lunch)
#print("Kalorie podw:", best_plan.calories_tea)
#print("Kalorie kolacja:", best_plan.calories_dinner)
#print()
#print("Makroskładniki:", best_plan.macros)
#   print(used_recipes)
#print()






