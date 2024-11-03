import random

# Przykładowe przepisy
available_recipes = [
    {'name': 'Salatka z kurczakiem', 'calories': 400, 'macros': {'protein': 30, 'carbs': 20, 'fats': 15},
     'meal_type': ['lunch', 'dinner']},
    {'name': 'Zupa jarzynowa', 'calories': 150, 'macros': {'protein': 5, 'carbs': 25, 'fats': 5},
     'meal_type': ['lunch', 'dinner']},
    {'name': 'Omlet warzywny', 'calories': 250, 'macros': {'protein': 18, 'carbs': 10, 'fats': 15},
     'meal_type': ['breakfast']},
    {'name': 'Ryż z warzywami i tofu', 'calories': 320, 'macros': {'protein': 15, 'carbs': 50, 'fats': 8},
     'meal_type': ['lunch', 'dinner']},
    {'name': 'Kanapka z awokado i jajkiem', 'calories': 350, 'macros': {'protein': 12, 'carbs': 30, 'fats': 20},
     'meal_type': ['breakfast', 'lunch']},
    {'name': 'Kurczak z kaszą bulgur', 'calories': 450, 'macros': {'protein': 35, 'carbs': 45, 'fats': 10},
     'meal_type': ['lunch', 'dinner']},
    {'name': 'Pasta z soczewicą', 'calories': 400, 'macros': {'protein': 20, 'carbs': 60, 'fats': 8},
     'meal_type': ['lunch', 'dinner']},
    {'name': 'Łosoś z batatami', 'calories': 500, 'macros': {'protein': 35, 'carbs': 40, 'fats': 20},
     'meal_type': ['dinner']},
    {'name': 'Sałatka grecka', 'calories': 220, 'macros': {'protein': 8, 'carbs': 10, 'fats': 15},
     'meal_type': ['lunch', 'dinner']},
    {'name': 'Smoothie bananowo-szpinakowe', 'calories': 180, 'macros': {'protein': 5, 'carbs': 35, 'fats': 2},
     'meal_type': ['breakfast', 'snack']},
    {'name': 'Indyk z ryżem i brokułami', 'calories': 450, 'macros': {'protein': 40, 'carbs': 50, 'fats': 8},
     'meal_type': ['lunch', 'dinner']},
    {'name': 'Pieczone warzywa z komosą ryżową', 'calories': 300, 'macros': {'protein': 10, 'carbs': 45, 'fats': 8},
     'meal_type': ['lunch', 'dinner']},
    {'name': 'Placuszki owsiane', 'calories': 290, 'macros': {'protein': 10, 'carbs': 40, 'fats': 10},
     'meal_type': ['breakfast']},
    {'name': 'Tortilla z hummusem i warzywami', 'calories': 350, 'macros': {'protein': 10, 'carbs': 50, 'fats': 12},
     'meal_type': ['lunch', 'dinner']},
    {'name': 'Zapiekanka z batatem i kurczakiem', 'calories': 480, 'macros': {'protein': 30, 'carbs': 55, 'fats': 15},
     'meal_type': ['dinner']},
    {'name': 'Makaron z warzywami i tofu', 'calories': 400, 'macros': {'protein': 15, 'carbs': 65, 'fats': 8},
     'meal_type': ['lunch', 'dinner']},
    {'name': 'Gulasz warzywny z ciecierzycą', 'calories': 370, 'macros': {'protein': 20, 'carbs': 45, 'fats': 12},
     'meal_type': ['lunch', 'dinner']},
    {'name': 'Kanapka z masłem orzechowym', 'calories': 280, 'macros': {'protein': 8, 'carbs': 25, 'fats': 18},
     'meal_type': ['breakfast', 'snack']},
    {'name': 'Budyń chia z owocami', 'calories': 200, 'macros': {'protein': 5, 'carbs': 30, 'fats': 8},
     'meal_type': ['breakfast', 'snack']},
    {'name': 'Ryż z fasolą i warzywami', 'calories': 350, 'macros': {'protein': 12, 'carbs': 60, 'fats': 6},
     'meal_type': ['lunch', 'dinner']},
    {'name': 'Kanapka z szynką i warzywami', 'calories': 300, 'macros': {'protein': 15, 'carbs': 35, 'fats': 10},
     'meal_type': ['breakfast', 'lunch']},
    {'name': 'Sałatka z tuńczykiem', 'calories': 250, 'macros': {'protein': 20, 'carbs': 10, 'fats': 15},
     'meal_type': ['lunch', 'dinner']},
    {'name': 'Owsianka z owocami', 'calories': 320, 'macros': {'protein': 10, 'carbs': 50, 'fats': 8},
     'meal_type': ['breakfast']},
    {'name': 'Kurczak z warzywami', 'calories': 380, 'macros': {'protein': 30, 'carbs': 20, 'fats': 15},
     'meal_type': ['lunch', 'dinner']},
    {'name': 'Zupa krem z dyni', 'calories': 180, 'macros': {'protein': 4, 'carbs': 25, 'fats': 8},
     'meal_type': ['lunch', 'dinner']},
    {'name': 'Makaron pełnoziarnisty z sosem pomidorowym', 'calories': 330,
     'macros': {'protein': 10, 'carbs': 60, 'fats': 6}, 'meal_type': ['lunch', 'dinner']},
    {'name': 'Filet z dorsza z warzywami', 'calories': 300, 'macros': {'protein': 25, 'carbs': 20, 'fats': 10},
     'meal_type': ['lunch', 'dinner']},
    {'name': 'Omlet ze szpinakiem', 'calories': 270, 'macros': {'protein': 20, 'carbs': 10, 'fats': 15},
     'meal_type': ['breakfast']},
    {'name': 'Curry z ciecierzycą', 'calories': 380, 'macros': {'protein': 15, 'carbs': 50, 'fats': 15},
     'meal_type': ['lunch', 'dinner']},
    {'name': 'Batony energetyczne owsiane', 'calories': 200, 'macros': {'protein': 5, 'carbs': 30, 'fats': 8},
     'meal_type': ['snack']},
    {'name': 'Zapiekanka makaronowa z serem', 'calories': 450, 'macros': {'protein': 20, 'carbs': 60, 'fats': 15},
     'meal_type': ['dinner']},
    # ...
]


# Klasa reprezentująca plan dietetyczny
class DietPlan:
    def __init__(self, breakfast, lunch, dinner):
        self.breakfast = breakfast
        self.lunch = lunch
        self.dinner = dinner

        self.recipes = self.breakfast + self.lunch + self.dinner
        self.calories = sum(recipe['calories'] for recipe in self.recipes)
        self.macros = self.calculate_macros()

    def calculate_macros(self):
        total_macros = {'protein': 0, 'carbs': 0, 'fats': 0}
        for recipe in self.recipes:
            for macro, value in recipe['macros'].items():
                total_macros[macro] += value
        return total_macros


# Generowanie początkowej populacji
def generate_initial_population(user_requirements, size=1000000):
    population = []

    # Zakładamy, że dostępne przepisy są posegregowane na kategorie
    breakfast_recipes = [recipe for recipe in available_recipes if 'breakfast' in recipe['meal_type']]
    lunch_recipes = [recipe for recipe in available_recipes if 'lunch' in recipe['meal_type']]
    dinner_recipes = [recipe for recipe in available_recipes if 'dinner' in recipe['meal_type']]

    for _ in range(size):
        # Wybierz 2 przepisy na śniadanie
        selected_breakfasts = random.sample(breakfast_recipes, k=2)
        # Wybierz 1 przepis na obiad
        selected_lunch = random.sample(lunch_recipes, k=1)
        # Wybierz 1 przepis na kolację
        selected_dinner = random.sample(dinner_recipes, k=1)

        # Tworzenie obiektu DietPlan z podziałem na posiłki
        diet_plan = DietPlan(
            breakfast=selected_breakfasts,
            lunch=selected_lunch,
            dinner=selected_dinner
        )

        # Dodaj plan do populacji
        population.append(diet_plan)

    return population

# Funkcja dopasowania
def fitness(plan, user_requirements):
    score = 0
    # Przykład: dodaj punkty za kalorie i makroskładniki
    if plan.calories <= user_requirements['calories']:
        if plan.calories - user_requirements['calories'] <= 20:
            score += 100
    else:
        score += 1

    if plan.macros['protein'] <= user_requirements['protein']:
        if abs(plan.calories - user_requirements['protein']) <= 4:
            score += 100
        elif abs(plan.calories - user_requirements['protein']) <= 10:
            score += 50
        elif abs(plan.calories - user_requirements['protein']) <= 15:
            score += 25
        else:
            score -= 10

    if plan.macros['carbs'] <= user_requirements['carbs']:
        if plan.calories - user_requirements['carbs'] <= 4:
            score += 100
    else:
        score += 1

    if plan.macros['fats'] <= user_requirements['fats']:
        if plan.calories - user_requirements['fats'] <= 4:
            score += 100
    else:
        score += 1
    # Dodaj inne kryteria oceny
    print(score)
    return score


# Algorytm genetyczny
def genetic_algorithm(user_requirements, generations=2):
    population = generate_initial_population(user_requirements)

    for generation in range(generations):
        population.sort(key=lambda x: fitness(x, user_requirements), reverse=True)
        new_population = population[:10]  # Najlepsze 10 planów

        while len(new_population) < 20:
            parent1, parent2 = random.sample(new_population[:10], 2)

            # Zachowanie struktury posiłków: 2 śniadania, 1 obiad, 2 kolacje
            crossover_breakfasts = random.sample(parent1.breakfast + parent2.breakfast, k=2)
            crossover_lunch = random.sample(parent1.lunch + parent2.lunch, k=1)
            crossover_dinners = random.sample(parent1.dinner + parent2.dinner, k=1)

            new_population.append(DietPlan(crossover_breakfasts, crossover_lunch, crossover_dinners))

        # Mutacja
        for plan in new_population:

            breakfast_recipes = [recipe for recipe in available_recipes if 'breakfast' in recipe['meal_type']]
            lunch_recipes = [recipe for recipe in available_recipes if 'lunch' in recipe['meal_type']]
            dinner_recipes = [recipe for recipe in available_recipes if 'dinner' in recipe['meal_type']]

            if random.random() < 0.1:  # 10% szans na mutację
                # Mutacja śniadań
                if random.random() < 0.5:  # 50% szans na mutację śniadania
                    plan.breakfast[random.randint(0, 1)] = random.choice(breakfast_recipes)

                # Mutacja obiadu
                if random.random() < 0.5:  # 50% szans na mutację obiadu
                    plan.lunch[0] = random.choice(lunch_recipes)

                # Mutacja kolacji
                if random.random() < 0.5:  # 50% szans na mutację kolacji
                    plan.dinner[0] = random.choice(dinner_recipes)

                # Aktualizacja kalorii i makroskładników po mutacji
                plan.recipes = plan.breakfast + plan.lunch + plan.dinner
                plan.calories = sum(recipe['calories'] for recipe in plan.recipes)
                plan.macros = plan.calculate_macros()

        population = new_population

    return population[0]  # Zwróć najlepszy plan


# Przykładowe wymagania użytkownika
user_requirements = {
    'calories': 1381,
    'protein': 86,
    'carbs': 173,
    'fats': 38,
    # Dodaj inne wymagania
}

best_plan = genetic_algorithm(user_requirements)
print("Najlepszy plan dietetyczny:")
for recipe in best_plan.recipes:
    print(recipe['name'])

print(best_plan.calories)

print(best_plan.macros)


