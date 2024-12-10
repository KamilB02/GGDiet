import random
import time
from api.services.all_recipes import available_recipes
from api.serializers import DietPlanSerializer

used_recipes = set()


# user_requirements = {
#     'calories': 1903,
#     'protein': 119,
#     'carbs': 238,
#     'fats': 53,
#
#     'required_breakfast1': [],
#     'required_breakfast2': [],
#     'required_lunch': [],
#     'required_tea': [],
#     'required_dinner': [],
#
#     'unwanted_ingredients': [
#         'mleko',
#         'tofu'
#     ]
# }


def prepare_user_requirements(preferences):
    user_requirements = {
        'calories': preferences['calories'],
        'protein': preferences['protein'],
        'carbs': preferences['carbs'],
        'fats': preferences['fats'],
        'unwanted_ingredients': preferences['avoidedIngredients'],
        'required_breakfast1_1': preferences['mealPreferences1']['breakfast'],
        'required_breakfast1_2': preferences['mealPreferences2']['breakfast'],
        'required_breakfast1_3': preferences['mealPreferences3']['breakfast'],
        'required_breakfast2_1': preferences['mealPreferences1']['secondBreakfast'],
        'required_breakfast2_2': preferences['mealPreferences2']['secondBreakfast'],
        'required_breakfast2_3': preferences['mealPreferences3']['secondBreakfast'],
        'required_lunch_1': preferences['mealPreferences1']['lunch'],
        'required_lunch_2': preferences['mealPreferences2']['lunch'],
        'required_lunch_3': preferences['mealPreferences3']['lunch'],
        'required_tea_1': preferences['mealPreferences1']['tea'],
        'required_tea_2': preferences['mealPreferences2']['tea'],
        'required_tea_3': preferences['mealPreferences3']['tea'],
        'required_dinner_1': preferences['mealPreferences1']['dinner'],
        'required_dinner_2': preferences['mealPreferences2']['dinner'],
        'required_dinner_3': preferences['mealPreferences3']['dinner'],
    }

    return user_requirements

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

    def to_dict(self):

        return {
            'breakfast1': self.breakfast1,
            'breakfast2': self.breakfast2,
            'lunch': self.lunch,
            'tea': self.tea,
            'dinner': self.dinner,
            'calories_breakfast1': self.calories_breakfast1,
            'calories_breakfast2': self.calories_breakfast2,
            'calories_lunch': self.calories_lunch,
            'calories_tea': self.calories_tea,
            'calories_dinner': self.calories_dinner,
            'calories_total': self.calories,
            'macros': self.macros
        }


def generate_initial_population(user_requirements, meal_number, size):
    print("generowanie populacji")

    population = []

    if user_requirements['required_breakfast1_1'] and meal_number == 0:
        breakfast1_recipes = [recipe for recipe in available_recipes if
                              'breakfast' in recipe['meal_type'] and recipe['name'] in user_requirements[
                                  'required_breakfast1_1']]

    elif user_requirements['required_breakfast1_2'] and meal_number == 1:
        breakfast1_recipes = [recipe for recipe in available_recipes if
                              'breakfast' in recipe['meal_type'] and recipe['name'] in user_requirements[
                                  'required_breakfast1_2']]

    elif user_requirements['required_breakfast1_3'] and meal_number == 2:
        breakfast1_recipes = [recipe for recipe in available_recipes if
                              'breakfast' in recipe['meal_type'] and recipe['name'] in user_requirements[
                                  'required_breakfast1_3']]
    else:
        breakfast1_recipes = [recipe for recipe in available_recipes if
                              'breakfast' in recipe['meal_type'] and recipe['name'] not in used_recipes and not any(
                                  ingredient in user_requirements['unwanted_ingredients'] for ingredient in
                                  recipe['ingredients'])]

    if user_requirements['required_breakfast2_1'] and meal_number == 0:
        breakfast2_recipes = [recipe for recipe in available_recipes if
                              'breakfast' in recipe['meal_type'] and recipe['name'] in user_requirements[
                                  'required_breakfast2_1']]

    elif user_requirements['required_breakfast2_2'] and meal_number == 1:
        breakfast2_recipes = [recipe for recipe in available_recipes if
                              'breakfast' in recipe['meal_type'] and recipe['name'] in user_requirements[
                                  'required_breakfast2_2']]

    elif user_requirements['required_breakfast2_3'] and meal_number == 2:
        breakfast2_recipes = [recipe for recipe in available_recipes if
                              'breakfast' in recipe['meal_type'] and recipe['name'] in user_requirements[
                                  'required_breakfast2_3']]
    else:
        breakfast2_recipes = [recipe for recipe in available_recipes if
                              'breakfast' in recipe['meal_type'] and recipe['name'] not in used_recipes and not any(
                                  ingredient in user_requirements['unwanted_ingredients'] for ingredient in
                                  recipe['ingredients'])]

    if user_requirements['required_lunch_1'] and meal_number == 0:
        lunch_recipes = [recipe for recipe in available_recipes if
                         'lunch' in recipe['meal_type'] and recipe['name'] in user_requirements[
                             'required_lunch_1']]
        if 0.30 >= lunch_recipes[0]['calories'] / user_requirements['calories'] or 0.35 <= lunch_recipes[0]['calories'] / user_requirements['calories'] :
            lunch_recipes = [recipe for recipe in available_recipes if
                             'lunch' in recipe['meal_type'] and recipe['name'] not in used_recipes and not any(
                                 ingredient in user_requirements['unwanted_ingredients'] for ingredient in
                                 recipe['ingredients'])]

    elif user_requirements['required_lunch_2'] and meal_number == 1:
        lunch_recipes = [recipe for recipe in available_recipes if
                         'lunch' in recipe['meal_type'] and recipe['name'] in user_requirements[
                             'required_lunch_2']]
        if 0.30 >= lunch_recipes[0]['calories'] / user_requirements['calories'] or 0.35 <= lunch_recipes[0]['calories'] / user_requirements['calories'] :
            lunch_recipes = [recipe for recipe in available_recipes if
                             'lunch' in recipe['meal_type'] and recipe['name'] not in used_recipes and not any(
                                 ingredient in user_requirements['unwanted_ingredients'] for ingredient in
                                 recipe['ingredients'])]

    elif user_requirements['required_lunch_3'] and meal_number == 2:
        lunch_recipes = [recipe for recipe in available_recipes if
                         'lunch' in recipe['meal_type'] and recipe['name'] in user_requirements[
                             'required_lunch_3']]
        if 0.30 >= lunch_recipes[0]['calories'] / user_requirements['calories'] or 0.35 <= lunch_recipes[0]['calories'] / user_requirements['calories'] :
            lunch_recipes = [recipe for recipe in available_recipes if
                             'lunch' in recipe['meal_type'] and recipe['name'] not in used_recipes and not any(
                                 ingredient in user_requirements['unwanted_ingredients'] for ingredient in
                                 recipe['ingredients'])]
    else:
        lunch_recipes = [recipe for recipe in available_recipes if
                         'lunch' in recipe['meal_type'] and recipe['name'] not in used_recipes and not any(
                             ingredient in user_requirements['unwanted_ingredients'] for ingredient in
                             recipe['ingredients'])]

    if user_requirements['required_tea_1'] and meal_number == 0:
        tea_recipes = [recipe for recipe in available_recipes if
                       'breakfast' in recipe['meal_type'] and recipe['name'] in user_requirements[
                           'required_tea_1']]

    elif user_requirements['required_tea_2'] and meal_number == 1:
        tea_recipes = [recipe for recipe in available_recipes if
                       'breakfast' in recipe['meal_type'] and recipe['name'] in user_requirements[
                           'required_tea_2']]

    elif user_requirements['required_tea_2'] and meal_number == 2:
        tea_recipes = [recipe for recipe in available_recipes if
                       'breakfast' in recipe['meal_type'] and recipe['name'] in user_requirements[
                           'required_tea_2']]
    else:
        tea_recipes = [recipe for recipe in available_recipes if
                       'breakfast' in recipe['meal_type'] and recipe['name'] not in used_recipes and not any(
                           ingredient in user_requirements['unwanted_ingredients'] for ingredient in
                           recipe['ingredients'])]

    if user_requirements['required_dinner_1'] and meal_number == 0:
        dinner_recipes = [recipe for recipe in available_recipes if
                          'dinner' in recipe['meal_type'] and recipe['name'] in user_requirements[
                              'required_dinner_1']]

    elif user_requirements['required_dinner_2'] and meal_number == 1:
        dinner_recipes = [recipe for recipe in available_recipes if
                          'dinner' in recipe['meal_type'] and recipe['name'] in user_requirements[
                              'required_dinner_2']]

    elif user_requirements['required_dinner_3'] and meal_number == 2:
        dinner_recipes = [recipe for recipe in available_recipes if
                          'dinner' in recipe['meal_type'] and recipe['name'] in user_requirements[
                              'required_dinner_3']]
    else:
        dinner_recipes = [recipe for recipe in available_recipes if
                          'dinner' in recipe['meal_type'] and recipe['name'] not in used_recipes and not any(
                              ingredient in user_requirements['unwanted_ingredients'] for ingredient in
                              recipe['ingredients'])]

    for _ in range(size):

        selected_breakfast1 = random.sample(breakfast1_recipes, k=1)
        selected_breakfast2 = random.sample(breakfast2_recipes, k=1)
        selected_lunch = random.sample(lunch_recipes, k=1)
        selected_tea = random.sample(tea_recipes, k=1)
        selected_dinner = random.sample(dinner_recipes, k=1)

        while selected_dinner[0] == selected_lunch[0]:
            if random.random() < 0.5:
                selected_dinner = random.sample(dinner_recipes, k=1)
            else:
                selected_lunch = random.sample(lunch_recipes, k=1)

        while selected_breakfast1[0] == selected_breakfast2[0]:
            if random.random() < 0.5:
                selected_breakfast2 = random.sample(breakfast2_recipes, k=1)
            else:
                selected_breakfast1 = random.sample(breakfast1_recipes, k=1)

        while 'snack' in selected_breakfast1[0]['meal_type'] and 'snack' in selected_breakfast2[0]['meal_type']:
            if random.random() < 0.5:
                selected_breakfast2 = random.sample(breakfast2_recipes, k=1)
            else:
                selected_breakfast1 = random.sample(breakfast1_recipes, k=1)

        while 'snack' in selected_breakfast1[0]['meal_type'] and 'snack' in selected_tea[0]['meal_type']:
            if random.random() < 0.5:
                selected_tea = random.sample(tea_recipes, k=1)
            else:
                selected_breakfast1 = random.sample(breakfast1_recipes, k=1)

        while 'snack' in selected_breakfast2[0]['meal_type'] and 'snack' in selected_tea[0]['meal_type']:
            if random.random() < 0.5:
                selected_tea = random.sample(tea_recipes, k=1)
            else:
                selected_breakfast2 = random.sample(breakfast2_recipes, k=1)

        while not 'breakfast' in selected_tea[0]['meal_type']:
            selected_tea = random.sample(tea_recipes, k=1)

        while selected_lunch[0]['calories'] < selected_dinner[0]['calories']:
            if user_requirements['required_dinner_1'] and meal_number == 0:
                selected_lunch = random.sample(lunch_recipes, k=1)
            if user_requirements['required_dinner_2'] and meal_number == 1:
                selected_lunch = random.sample(lunch_recipes, k=1)
            if user_requirements['required_dinner_3'] and meal_number == 2:
                selected_lunch = random.sample(lunch_recipes, k=1)
            if user_requirements['required_lunch_1'] and meal_number == 0:
                selected_dinner = random.sample(dinner_recipes, k=1)
            if user_requirements['required_lunch_2'] and meal_number == 1:
                selected_dinner = random.sample(dinner_recipes, k=1)
            if user_requirements['required_lunch_3'] and meal_number == 2:
                selected_dinner = random.sample(dinner_recipes, k=1)
            else:
                selected_lunch = random.sample(lunch_recipes, k=1)

        diet_plan = DietPlan(
            breakfast1=selected_breakfast1,
            breakfast2=selected_breakfast2,
            lunch=selected_lunch,
            tea=selected_tea,
            dinner=selected_dinner
        )

        population.append(diet_plan)

    print("Koniec generowanie populacji")
    return population


def fitness(plan, user_requirements):
    score = 0

    calorie_diff = abs(plan.calories - user_requirements['calories'])
    if calorie_diff <= 20:
        score += 120
    elif calorie_diff <= 50:
        score += 80
    elif calorie_diff <= 100:
        score += 50
    else:
        score -= calorie_diff * 2

    protein_diff = abs(plan.macros['protein'] - user_requirements['protein'])
    if protein_diff <= 4:
        score += 125
    elif protein_diff <= 8:
        score += 75
    elif protein_diff <= 12:
        score += 40
    else:
        score -= protein_diff * 2

    carb_diff = abs(plan.macros['carbs'] - user_requirements['carbs'])
    if carb_diff <= 4:
        score += 125
    elif carb_diff <= 8:
        score += 75
    elif carb_diff <= 12:
        score += 40
    else:
        score -= carb_diff * 2

    fat_diff = abs(plan.macros['fats'] - user_requirements['fats'])
    if fat_diff <= 4:
        score += 125
    elif fat_diff <= 8:
        score += 75
    elif fat_diff <= 12:
        score += 40
    else:
        score -= fat_diff * 2

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

    total_match_ratio = (1 - calorie_diff / user_requirements['calories']) * 100
    score += total_match_ratio

    return score


def genetic_algorithm(user_requirements, meal_number, generations, additional_generations, max_extra_generations, max_extra_reset):
    def generate_population():
        return generate_initial_population(user_requirements, meal_number, 10000)

    population = generate_population()

    if user_requirements['required_breakfast1_1'] and meal_number == 0:
        breakfast1_recipes = [recipe for recipe in available_recipes if
                              'breakfast' in recipe['meal_type'] and recipe['name'] in user_requirements[
                                  'required_breakfast1_1']]

    elif user_requirements['required_breakfast1_2'] and meal_number == 1:
        breakfast1_recipes = [recipe for recipe in available_recipes if
                              'breakfast' in recipe['meal_type'] and recipe['name'] in user_requirements[
                                  'required_breakfast1_2']]

    elif user_requirements['required_breakfast1_3'] and meal_number == 2:
        breakfast1_recipes = [recipe for recipe in available_recipes if
                              'breakfast' in recipe['meal_type'] and recipe['name'] in user_requirements[
                                  'required_breakfast1_3']]
    else:
        breakfast1_recipes = [recipe for recipe in available_recipes if
                              'breakfast' in recipe['meal_type'] and recipe['name'] not in used_recipes and not any(
                                  ingredient in user_requirements['unwanted_ingredients'] for ingredient in
                                  recipe['ingredients'])]

    if user_requirements['required_breakfast2_1'] and meal_number == 0:
        breakfast2_recipes = [recipe for recipe in available_recipes if
                              'breakfast' in recipe['meal_type'] and recipe['name'] in user_requirements[
                                  'required_breakfast2_1']]

    elif user_requirements['required_breakfast2_2'] and meal_number == 1:
        breakfast2_recipes = [recipe for recipe in available_recipes if
                              'breakfast' in recipe['meal_type'] and recipe['name'] in user_requirements[
                                  'required_breakfast2_2']]

    elif user_requirements['required_breakfast2_3'] and meal_number == 2:
        breakfast2_recipes = [recipe for recipe in available_recipes if
                              'breakfast' in recipe['meal_type'] and recipe['name'] in user_requirements[
                                  'required_breakfast2_3']]
    else:
        breakfast2_recipes = [recipe for recipe in available_recipes if
                              'breakfast' in recipe['meal_type'] and recipe['name'] not in used_recipes and not any(
                                  ingredient in user_requirements['unwanted_ingredients'] for ingredient in
                                  recipe['ingredients'])]

    if user_requirements['required_lunch_1'] and meal_number == 0:
        lunch_recipes = [recipe for recipe in available_recipes if
                         'lunch' in recipe['meal_type'] and recipe['name'] in user_requirements[
                             'required_lunch_1']]

    elif user_requirements['required_lunch_2'] and meal_number == 1:
        lunch_recipes = [recipe for recipe in available_recipes if
                         'lunch' in recipe['meal_type'] and recipe['name'] in user_requirements[
                             'required_lunch_2']]

    elif user_requirements['required_lunch_3'] and meal_number == 2:
        lunch_recipes = [recipe for recipe in available_recipes if
                         'lunch' in recipe['meal_type'] and recipe['name'] in user_requirements[
                             'required_lunch_3']]
    else:
        lunch_recipes = [recipe for recipe in available_recipes if
                         'lunch' in recipe['meal_type'] and recipe['name'] not in used_recipes and not any(
                             ingredient in user_requirements['unwanted_ingredients'] for ingredient in
                             recipe['ingredients'])]

    if user_requirements['required_tea_1'] and meal_number == 0:
        tea_recipes = [recipe for recipe in available_recipes if
                       'breakfast' in recipe['meal_type'] and recipe['name'] in user_requirements[
                           'required_tea_1']]

    elif user_requirements['required_tea_2'] and meal_number == 1:
        tea_recipes = [recipe for recipe in available_recipes if
                       'breakfast' in recipe['meal_type'] and recipe['name'] in user_requirements[
                           'required_tea_2']]

    elif user_requirements['required_tea_2'] and meal_number == 2:
        tea_recipes = [recipe for recipe in available_recipes if
                       'breakfast' in recipe['meal_type'] and recipe['name'] in user_requirements[
                           'required_tea_2']]
    else:
        tea_recipes = [recipe for recipe in available_recipes if
                       'breakfast' in recipe['meal_type'] and recipe['name'] not in used_recipes and not any(
                           ingredient in user_requirements['unwanted_ingredients'] for ingredient in
                           recipe['ingredients'])]

    if user_requirements['required_dinner_1'] and meal_number == 0:
        dinner_recipes = [recipe for recipe in available_recipes if
                          'dinner' in recipe['meal_type'] and recipe['name'] in user_requirements[
                              'required_dinner_1']]

    elif user_requirements['required_dinner_2'] and meal_number == 1:
        dinner_recipes = [recipe for recipe in available_recipes if
                          'dinner' in recipe['meal_type'] and recipe['name'] in user_requirements[
                              'required_dinner_2']]

    elif user_requirements['required_dinner_3'] and meal_number == 2:
        dinner_recipes = [recipe for recipe in available_recipes if
                          'dinner' in recipe['meal_type'] and recipe['name'] in user_requirements[
                              'required_dinner_3']]
    else:
        dinner_recipes = [recipe for recipe in available_recipes if
                          'dinner' in recipe['meal_type'] and recipe['name'] not in used_recipes and not any(
                              ingredient in user_requirements['unwanted_ingredients'] for ingredient in
                              recipe['ingredients'])]

    extra_generations = 0
    stop = 0

    while extra_generations <= max_extra_generations:
        for generation in range(generations):
            population.sort(key=lambda x: fitness(x, user_requirements), reverse=True)
            new_population = population[:20]

            while len(new_population) < 60:
                parent1, parent2 = random.sample(population[:20], 2)

                crossover_breakfast1 = random.sample(parent1.breakfast1 + parent2.breakfast1, k=1)
                crossover_breakfast2 = random.sample(parent1.breakfast2 + parent2.breakfast2, k=1)
                crossover_lunch = random.sample(parent1.lunch + parent2.lunch, k=1)
                crossover_tea = random.sample(
                    [recipe for recipe in (parent1.tea + parent2.tea) if 'breakfast' in recipe['meal_type']],
                    k=1
                )
                crossover_dinners = random.sample(parent1.dinner + parent2.dinner, k=1)

                while crossover_dinners[0] == crossover_lunch[0]:
                    if user_requirements['required_dinner_1'] and meal_number == 0:
                        crossover_lunch = random.sample(parent1.lunch + parent2.lunch, k=1)
                    if user_requirements['required_dinner_2'] and meal_number == 1:
                        crossover_lunch = random.sample(parent1.lunch + parent2.lunch, k=1)
                    if user_requirements['required_dinner_3'] and meal_number == 2:
                        crossover_lunch = random.sample(parent1.lunch + parent2.lunch, k=1)
                    if user_requirements['required_lunch_1'] and meal_number == 0:
                        crossover_dinners = random.sample(parent1.dinner + parent2.dinner, k=1)
                    if user_requirements['required_lunch_2'] and meal_number == 1:
                        crossover_dinners = random.sample(parent1.dinner + parent2.dinner, k=1)
                    if user_requirements['required_lunch_3'] and meal_number == 2:
                        crossover_dinners = random.sample(parent1.dinner + parent2.dinner, k=1)
                    elif parent1.dinner == parent2.dinner:
                        crossover_lunch = random.sample(parent1.lunch + parent2.lunch, k=1)
                    else:
                        crossover_dinners = random.sample(parent1.dinner + parent2.dinner, k=1)

                while crossover_breakfast1[0] == crossover_breakfast2[0]:
                    if parent1.breakfast1 == parent2.breakfast1:
                        crossover_breakfast2 = random.sample(parent1.breakfast2 + parent2.breakfast2, k=1)
                    else:
                        crossover_breakfast1 = random.sample(parent1.breakfast1 + parent2.breakfast1, k=1)

                # Sprawdzenie czy oba breakfast1 i breakfast2 mają ten sam typ "snack"
                while 'snack' in crossover_breakfast1[0]['meal_type'] and 'snack' in crossover_breakfast2[0][
                    'meal_type']:
                    if random.random() < 0.5:
                        crossover_breakfast2 = random.sample(parent1.breakfast2 + parent2.breakfast2, k=1)
                    else:
                        crossover_breakfast1 = random.sample(parent1.breakfast1 + parent2.breakfast1, k=1)

                # Sprawdzenie czy breakfast1 i tea mają ten sam typ "snack"
                while 'snack' in crossover_breakfast1[0]['meal_type'] and 'snack' in crossover_tea[0]['meal_type']:
                    if random.random() < 0.5:
                        crossover_tea = random.sample(parent1.tea + parent2.tea, k=1)
                    else:
                        crossover_breakfast1 = random.sample(parent1.breakfast1 + parent2.breakfast1, k=1)

                # Sprawdzenie czy breakfast2 i tea mają ten sam typ "snack"
                while 'snack' in crossover_breakfast2[0]['meal_type'] and 'snack' in crossover_tea[0]['meal_type']:
                    if random.random() < 0.5:
                        crossover_tea = random.sample(parent1.tea + parent2.tea, k=1)
                    else:
                        crossover_breakfast2 = random.sample(parent1.breakfast2 + parent2.breakfast2, k=1)

                new_population.append(
                    DietPlan(crossover_breakfast1, crossover_breakfast2, crossover_lunch, crossover_tea,
                             crossover_dinners))

            for plan in new_population:

                if random.random() < 0.05:
                    random_number = random.randint(1, 5)

                    if random_number == 1:
                        plan.breakfast1[0] = random.choice(breakfast1_recipes)
                    if random_number == 2:
                        plan.breakfast2[0] = random.choice(breakfast2_recipes)
                    if random_number == 3:
                        plan.lunch[0] = random.choice(lunch_recipes)
                    if random_number == 4:
                        plan.tea[0] = random.choice(
                            [recipe for recipe in tea_recipes if 'breakfast' in recipe['meal_type']])
                    if random_number == 5:
                        plan.dinner[0] = random.choice(dinner_recipes)


                    while plan.dinner[0] == plan.lunch[0]:
                        if user_requirements['required_dinner_1'] and meal_number == 0:
                            plan.lunch[0] = random.choice(lunch_recipes)
                        elif user_requirements['required_dinner_2'] and meal_number == 1:
                            plan.lunch[0] = random.choice(lunch_recipes)
                        elif user_requirements['required_dinner_3'] and meal_number == 2:
                            plan.lunch[0] = random.choice(lunch_recipes)
                        elif user_requirements['required_lunch_1'] and meal_number == 0:
                            plan.dinner[0] = random.choice(dinner_recipes)
                        elif user_requirements['required_lunch_2'] and meal_number == 1:
                            plan.dinner[0] = random.choice(dinner_recipes)
                        elif user_requirements['required_lunch_3'] and meal_number == 2:
                            plan.dinner[0] = random.choice(dinner_recipes)
                        else:
                            if random.random() < 0.5:
                                plan.dinner[0] = random.choice(dinner_recipes)
                            else:
                                plan.lunch[0] = random.choice(lunch_recipes)

                    # Sprawdzenie, czy breakfast1 i breakfast2 mają taki sam typ "snack"
                    while 'snack' in plan.breakfast1[0]['meal_type'] and 'snack' in plan.breakfast2[0]['meal_type']:
                        plan.breakfast2[0] = random.choice(dinner_recipes)

                    # Sprawdzenie, czy breakfast1 i tea mają taki sam typ "snack"
                    while 'snack' in plan.breakfast1[0]['meal_type'] and 'snack' in plan.tea[0]['meal_type']:
                        plan.tea[0] = random.choice(
                            [recipe for recipe in tea_recipes if 'breakfast' in recipe['meal_type']])

                    # Sprawdzenie, czy breakfast2 i tea mają taki sam typ "snack"
                    while 'snack' in plan.breakfast2[0]['meal_type'] and 'snack' in plan.tea[0]['meal_type']:
                        plan.tea[0] = random.choice(
                            [recipe for recipe in tea_recipes if 'breakfast' in recipe['meal_type']])

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

        if (calories_difference <= 100 and protein_difference <= 20 and carbs_difference <= 20 and fats_difference <= 10 and best_plan.calories_lunch > best_plan.calories_dinner):
            print("Znaleziono plan")
            print("Najlepszy plan dietetyczny :")
            for recipe in best_plan.recipes:
                print(recipe['name'])
                used_recipes.add(recipe['name'])
            print()
            print("Kalorie:", best_plan.calories)
            print()
            print("Kalorie sniadania:", best_plan.calories_breakfast1)
            print("Kalorie sniadania2:", best_plan.calories_breakfast2)
            print("Kalorie obiad:", best_plan.calories_lunch)
            print("Kalorie podw:", best_plan.calories_tea)
            print("Kalorie kolacja:", best_plan.calories_dinner)
            print()
            print("Makroskładniki:", best_plan.macros)
            return best_plan.to_dict()
        else:
            print("Nie znaleziono, szukam dalej")
            generations = additional_generations
            extra_generations += 1

        if stop > max_extra_reset:
            break

        if extra_generations > max_extra_generations:
            print("Nie znaleziono odpowiedniego planu, resetowanie populacji...")
            population = generate_population()
            extra_generations = 0
            generations = 2000
            stop += 1

    return best_plan.to_dict()

# for _ in range(3):
#     best_plan = genetic_algorithm(user_requirements)
#
#     print("Najlepszy plan dietetyczny :")
#     for recipe in best_plan.recipes:
#         print(recipe['name'])
#     print()
#     print("Kalorie:", best_plan.calories)
#     print()
#     print("Kalorie sniadania:", best_plan.calories_breakfast1)
#     print("Kalorie sniadania2:", best_plan.calories_breakfast2)
#     print("Kalorie obiad:", best_plan.calories_lunch)
#     print("Kalorie podw:", best_plan.calories_tea)
#     print("Kalorie kolacja:", best_plan.calories_dinner)
#     print()
#     print("Makroskładniki:", best_plan.macros)
#     print(used_recipes)
#     print()
