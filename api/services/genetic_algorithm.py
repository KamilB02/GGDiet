import random
from all_recipes import available_recipes

used_recipes = set()
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
def generate_initial_population(user_requirements, size=20000):
    population = []

    breakfast_recipes = [recipe for recipe in available_recipes if 'breakfast' in recipe['meal_type'] and recipe['name'] not in used_recipes]
    lunch_recipes = [recipe for recipe in available_recipes if 'lunch' in recipe['meal_type'] and recipe['name'] not in used_recipes]
    dinner_recipes = [recipe for recipe in available_recipes if 'dinner' in recipe['meal_type'] and recipe['name'] not in used_recipes]

    for _ in range(size):

        selected_breakfasts = random.sample([r for r in breakfast_recipes if r['name'] not in used_recipes], k=2)
        selected_lunch = random.sample([r for r in lunch_recipes if r['name'] not in used_recipes], k=1)
        selected_dinner = random.sample([r for r in dinner_recipes if r['name'] not in used_recipes], k=1)

        while selected_dinner[0] == selected_lunch[0]:
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
            score += 30
    else:
        score -= 100

    if plan.macros['protein'] <= user_requirements['protein']:
        if abs(plan.calories - user_requirements['protein']) <= 4:
            score += 100
        elif abs(plan.calories - user_requirements['protein']) <= 8:
            score += 50
        elif abs(plan.calories - user_requirements['protein']) <= 12:
            score += 25
        elif abs(plan.calories - user_requirements['protein']) <= 16:
            score -= 50
        else:
            score -= 100

    if plan.macros['carbs'] <= user_requirements['carbs']:
        if abs(plan.calories - user_requirements['carbs']) <= 4:
            score += 100
        elif abs(plan.calories - user_requirements['carbs']) <= 8:
            score += 50
        elif abs(plan.calories - user_requirements['carbs']) <= 12:
            score += 25
        else:
            score -= 100

    if plan.macros['fats'] <= user_requirements['fats']:
        if abs(plan.calories - user_requirements['fats']) <= 4:
            score += 100
        elif abs(plan.calories - user_requirements['fats']) <= 8:
            score += 50
        elif abs(plan.calories - user_requirements['fats']) <= 12:
            score += 25
        else:
            score -= 10

    if plan.macros['fats'] < 30:
        score -= 50

    return score


# Algorytm genetyczny
def genetic_algorithm(user_requirements, generations=30000):
    population = generate_initial_population(user_requirements)

    breakfast_recipes = [recipe for recipe in available_recipes if 'breakfast' in recipe['meal_type'] and recipe['name'] not in used_recipes]
    lunch_recipes = [recipe for recipe in available_recipes if 'lunch' in recipe['meal_type'] and recipe['name'] not in used_recipes]
    dinner_recipes = [recipe for recipe in available_recipes if 'dinner' in recipe['meal_type'] and recipe['name'] not in used_recipes]

    for generation in range(generations):
        population.sort(key=lambda x: fitness(x, user_requirements), reverse=True)
        new_population = population[:30]  # Najlepsze 10 planów

        while len(new_population) < 60:
            parent1, parent2 = random.sample(new_population[:30], 2)

            # Zachowanie struktury posiłków: 2 śniadania, 1 obiad, 2 kolacje
            crossover_breakfasts = random.sample(parent1.breakfast + parent2.breakfast, k=2)
            crossover_lunch = random.sample(parent1.lunch + parent2.lunch, k=1)
            crossover_dinners = random.sample(parent1.dinner + parent2.dinner, k=1)

            while crossover_dinners[0] == crossover_lunch[0]:
                crossover_dinners = random.sample(parent1.dinner + parent2.dinner, k=1)

            while crossover_breakfasts[0] == crossover_breakfasts[1]:
                crossover_breakfasts = random.sample(breakfast_recipes, k=2)

            new_population.append(DietPlan(crossover_breakfasts, crossover_lunch, crossover_dinners))

        # Mutacja
        for plan in new_population:

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

                while plan.dinner[0] == plan.lunch[0]:
                    plan.dinner[0] = random.choice(dinner_recipes)

                # Aktualizacja kalorii i makroskładników po mutacji
                plan.recipes = plan.breakfast + plan.lunch + plan.dinner
                plan.calories = sum(recipe['calories'] for recipe in plan.recipes)
                plan.macros = plan.calculate_macros()

        population = new_population

    #used_recipes.update([r['name'] for r in population[0].recipes])
    return population[0]


# Przykładowe wymagania użytkownika
user_requirements = {
    'calories': 2410,
    'protein': 151,
    'carbs': 301,
    'fats': 67,
    # Dodaj inne wymagania
}

for _ in range(7):
    best_plan = genetic_algorithm(user_requirements)

    print("Najlepszy plan dietetyczny :")
    for recipe in best_plan.recipes:
        print(recipe['name'])
    print("Kalorie:", best_plan.calories)
    print("Makroskładniki:", best_plan.macros)
    #   print(used_recipes)
    print()






