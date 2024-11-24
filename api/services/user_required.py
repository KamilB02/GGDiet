user_info = {
    'weight': 87,
    'height': 179,
    'age': 22,
    'gender': 'man',
    'physical_activity_at_work': 0,
    'physical_activity_in_free_time': 2,
    'objective': 'less',
}


def calculate_calories(user_info):
    weight = user_info['weight']
    height = user_info['height']
    age = user_info['age']
    gender = user_info['gender']
    activity_work = user_info['physical_activity_at_work'] - 1
    activity_free_time = user_info['physical_activity_in_free_time'] - 1
    objective = user_info['objective']

    if gender == 'man':
        bmr = 10 * weight + 6.25 * height - 5 * age + 5  # Mifflin-St Jeor Equation for man
    elif gender == 'woman':
        bmr = 10 * weight + 6.25 * height - 5 * age - 161 # Mifflin-St Jeor Equation for woman
    else:
        raise ValueError("Niepoprawna wartość płci, wybierz 'man' lub 'woman'.")

    activity_factors = [
        [1.30, 1.35, 1.40, 1.50],
        [1.40, 1.45, 1.50, 1.60],
        [1.50, 1.55, 1.60, 1.70],
        [1.60, 1.65, 1.70, 1.80],
        [1.70, 1.75, 1.80, 1.90],
    ]

    total_calories = round(bmr * activity_factors[activity_free_time][activity_work])

    if objective == 'less':
        total_calories = total_calories - 300
    elif objective == 'same':
        total_calories = total_calories - 50
    elif objective == 'more':
        total_calories = total_calories + 100

    return total_calories


def calculate_macro(user_info):
    protein = 0
    carbs = 0
    fats = 0
    objective = user_info['objective']

    calories = calculate_calories(user_info)

    if objective == 'less':
        protein = round((calories * 0.25)/4)
        carbs = round((calories * 0.50)/4)
        fats = round((calories * 0.25)/9)
    elif objective == 'same':
        protein = round((calories * 0.15)/4)
        carbs = round((calories * 0.55)/4)
        fats = round((calories * 0.30)/9)
    elif objective == 'more':
        protein = round((calories * 0.20)/4)
        carbs = round((calories * 0.50)/4)
        fats = round((calories * 0.30)/9)

    return protein, carbs, fats


# daily_calories = calculate_calories(user_info)
# daily_macro = calculate_macro(user_info)
# print("Dzienne zapotrzebowanie kaloryczne wynosi:", daily_calories, "kcal")
# print("Dzienne zapotrzebowanie protein:", daily_macro[0], "g")
# print("Dzienne zapotrzebowanie carbs:", daily_macro[1], "g")
# print("Dzienne zapotrzebowanie fats:", daily_macro[2], "g")