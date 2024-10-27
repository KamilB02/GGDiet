import random

# Przykładowe przepisy
available_recipes = [
    {'name': 'Salatka z kurczakiem', 'calories': 400, 'macros': {'protein': 30, 'carbs': 20, 'fats': 15}},
    {'name': 'Zupa jarzynowa', 'calories': 150, 'macros': {'protein': 5, 'carbs': 25, 'fats': 5}},
    # Dodaj więcej przepisów
]


# Klasa reprezentująca plan dietetyczny
class DietPlan:
    def __init__(self, recipes):
        self.recipes = recipes
        self.calories = sum(recipe['calories'] for recipe in recipes)
        self.macros = self.calculate_macros()

    def calculate_macros(self):
        total_macros = {'protein': 0, 'carbs': 0, 'fats': 0}
        for recipe in self.recipes:
            for macro, value in recipe['macros'].items():
                total_macros[macro] += value
        return total_macros


# Generowanie początkowej populacji
def generate_initial_population(user_requirements, size=20):
    population = []
    for _ in range(size):
        selected_recipes = random.sample(available_recipes, k=7)  # Wybierz 7 losowych przepisów
        population.append(DietPlan(selected_recipes))
    return population


# Funkcja dopasowania
def fitness(plan, user_requirements):
    score = 0
    # Przykład: dodaj punkty za kalorie i makroskładniki
    if plan.calories <= user_requirements['calories']:
        score += 1
    # Dodaj inne kryteria oceny
    return score


# Algorytm genetyczny
def genetic_algorithm(user_requirements, generations=10):
    population = generate_initial_population(user_requirements)

    for generation in range(generations):
        population.sort(key=lambda x: fitness(x, user_requirements), reverse=True)
        new_population = population[:10]  # Najlepsze 10 planów

        # Krzyżowanie
        while len(new_population) < 20:
            parent1, parent2 = random.sample(new_population[:10], 2)
            crossover_recipes = random.sample(parent1.recipes + parent2.recipes, k=7)
            new_population.append(DietPlan(crossover_recipes))

        # Mutacja
        for plan in new_population:
            if random.random() < 0.1:  # 10% szans na mutację
                new_recipe = random.choice(available_recipes)
                plan.recipes[random.randint(0, 6)] = new_recipe  # Zmień losowy przepis
                plan.calories = sum(recipe['calories'] for recipe in plan.recipes)  # Zaktualizuj kalorie
                plan.macros = plan.calculate_macros()  # Zaktualizuj makroskładniki

        population = new_population

    return population[0]  # Zwróć najlepszy plan


# Przykładowe wymagania użytkownika
user_requirements = {
    'calories': 2000,
    # Dodaj inne wymagania
}

best_plan = genetic_algorithm(user_requirements)
print("Najlepszy plan dietetyczny:")
for recipe in best_plan.recipes:
    print(recipe['name'])


