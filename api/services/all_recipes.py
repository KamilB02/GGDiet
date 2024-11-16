from rest_framework.views import APIView
from rest_framework.response import Response

available_recipes = [
    {'name': 'Sałatka z kurczakiem', 'calories': 400, 'macros': {'protein': 30, 'carbs': 20, 'fats': 15},
     'meal_type': ['lunch', 'dinner'], 'ingredients': ['kurczak', 'sałata', 'ogórek', 'pomidor', 'sos vinaigrette']},

    {'name': 'Zupa jarzynowa', 'calories': 150, 'macros': {'protein': 5, 'carbs': 25, 'fats': 5},
     'meal_type': ['lunch', 'dinner'], 'ingredients': ['marchewka', 'pietruszka', 'ziemniaki', 'por', 'bulion warzywny']},

    {'name': 'Omlet warzywny', 'calories': 250, 'macros': {'protein': 18, 'carbs': 10, 'fats': 15},
     'meal_type': ['breakfast'], 'ingredients': ['jajka', 'papryka', 'szpinak', 'cebula', 'sól', 'pieprz']},

    {'name': 'Ryż z warzywami i tofu', 'calories': 320, 'macros': {'protein': 15, 'carbs': 50, 'fats': 8},
     'meal_type': ['lunch', 'dinner'], 'ingredients': ['ryż', 'tofu', 'papryka', 'cukinia', 'sos sojowy']},

    {'name': 'Kanapka z awokado i jajkiem', 'calories': 350, 'macros': {'protein': 12, 'carbs': 30, 'fats': 20},
     'meal_type': ['breakfast', 'lunch'], 'ingredients': ['chleb', 'awokado', 'jajko', 'szpinak', 'sól', 'pieprz']},

    {'name': 'Kurczak z kaszą bulgur', 'calories': 450, 'macros': {'protein': 35, 'carbs': 45, 'fats': 10},
     'meal_type': ['lunch', 'dinner'], 'ingredients': ['kurczak', 'kasza bulgur', 'papryka', 'cukinia', 'oliwa']},

    {'name': 'Pasta z soczewicą', 'calories': 400, 'macros': {'protein': 20, 'carbs': 60, 'fats': 8},
     'meal_type': ['lunch', 'dinner'], 'ingredients': ['makaron', 'soczewica', 'pomidory', 'czosnek', 'bazylia']},

    {'name': 'Łosoś z batatami', 'calories': 500, 'macros': {'protein': 35, 'carbs': 40, 'fats': 20},
     'meal_type': ['dinner'], 'ingredients': ['łosoś', 'bataty', 'szpinak', 'cytryna', 'przyprawy']},

    {'name': 'Sałatka grecka', 'calories': 220, 'macros': {'protein': 8, 'carbs': 10, 'fats': 15},
     'meal_type': ['lunch', 'dinner'], 'ingredients': ['sałata', 'pomidor', 'ogórek', 'ser feta', 'oliwki', 'oliwa']},

    {'name': 'Smoothie bananowo-szpinakowe', 'calories': 180, 'macros': {'protein': 5, 'carbs': 35, 'fats': 2},
     'meal_type': ['breakfast', 'snack'], 'ingredients': ['banan', 'szpinak', 'mleko', 'miód']},

    {'name': 'Indyk z ryżem i brokułami', 'calories': 450, 'macros': {'protein': 40, 'carbs': 50, 'fats': 8},
     'meal_type': ['lunch', 'dinner'], 'ingredients': ['indyk', 'ryż', 'brokuły', 'przyprawy']},

    {'name': 'Pieczone warzywa z komosą ryżową', 'calories': 300, 'macros': {'protein': 10, 'carbs': 45, 'fats': 8},
     'meal_type': ['lunch', 'dinner'], 'ingredients': ['komosa ryżowa', 'cukinia', 'papryka', 'oliwa', 'przyprawy']},

    {'name': 'Placuszki owsiane', 'calories': 290, 'macros': {'protein': 10, 'carbs': 40, 'fats': 10},
     'meal_type': ['breakfast'], 'ingredients': ['płatki owsiane', 'jajka', 'banan', 'cynamon']},

    {'name': 'Tortilla z hummusem i warzywami', 'calories': 350, 'macros': {'protein': 10, 'carbs': 50, 'fats': 12},
     'meal_type': ['lunch', 'dinner'], 'ingredients': ['tortilla', 'hummus', 'ogórek', 'papryka', 'szpinak']},

    {'name': 'Zapiekanka z batatem i kurczakiem', 'calories': 480, 'macros': {'protein': 30, 'carbs': 55, 'fats': 15},
     'meal_type': ['dinner'], 'ingredients': ['batat', 'kurczak', 'szpinak', 'czosnek', 'ser']},

    {'name': 'Makaron z warzywami i tofu', 'calories': 400, 'macros': {'protein': 15, 'carbs': 65, 'fats': 8},
     'meal_type': ['lunch', 'dinner'], 'ingredients': ['makaron', 'tofu', 'cukinia', 'pomidory', 'bazylia']},

    {'name': 'Gulasz warzywny z ciecierzycą', 'calories': 370, 'macros': {'protein': 20, 'carbs': 45, 'fats': 12},
     'meal_type': ['lunch', 'dinner'], 'ingredients': ['ciecierzyca', 'marchewka', 'papryka', 'pomidory', 'przyprawy']},

    {'name': 'Kanapka z masłem orzechowym', 'calories': 280, 'macros': {'protein': 8, 'carbs': 25, 'fats': 18},
     'meal_type': ['breakfast', 'snack'], 'ingredients': ['chleb', 'masło orzechowe', 'banan']},

    {'name': 'Budyń chia z owocami', 'calories': 200, 'macros': {'protein': 5, 'carbs': 30, 'fats': 8},
     'meal_type': ['breakfast', 'snack'], 'ingredients': ['chia', 'mleko', 'owoce', 'miód']},

    {'name': 'Ryż z fasolą i warzywami', 'calories': 350, 'macros': {'protein': 12, 'carbs': 60, 'fats': 6},
     'meal_type': ['lunch', 'dinner'], 'ingredients': ['ryż', 'fasola', 'papryka', 'cebula', 'przyprawy']},

    {'name': 'Kanapka z szynką i warzywami', 'calories': 300, 'macros': {'protein': 15, 'carbs': 35, 'fats': 10},
     'meal_type': ['breakfast', 'lunch'], 'ingredients': ['chleb', 'szynka', 'sałata', 'pomidor', 'ogórek']},

    {'name': 'Sałatka z tuńczykiem', 'calories': 250, 'macros': {'protein': 20, 'carbs': 10, 'fats': 15},
     'meal_type': ['lunch', 'dinner'], 'ingredients': ['tuńczyk', 'sałata', 'ogórek', 'papryka', 'oliwki']},

    {'name': 'Owsianka z owocami', 'calories': 320, 'macros': {'protein': 10, 'carbs': 50, 'fats': 8},
     'meal_type': ['breakfast'], 'ingredients': ['płatki owsiane', 'mleko', 'owoce', 'miód']},

    {'name': 'Kurczak z warzywami', 'calories': 380, 'macros': {'protein': 30, 'carbs': 20, 'fats': 15},
     'meal_type': ['lunch', 'dinner'], 'ingredients': ['kurczak', 'cukinia', 'marchewka', 'papryka', 'przyprawy']},

    {'name': 'Zupa krem z dyni', 'calories': 180, 'macros': {'protein': 4, 'carbs': 25, 'fats': 8},
     'meal_type': ['lunch', 'dinner'], 'ingredients': ['dynia', 'bulion', 'cebula', 'czosnek', 'przyprawy']},

    {'name': 'Makaron pełnoziarnisty z sosem pomidorowym', 'calories': 330,
     'macros': {'protein': 10, 'carbs': 60, 'fats': 6},
     'ingredients': ['makaron pełnoziarnisty', 'sos pomidorowy', 'czosnek', 'bazylia', 'oliwa z oliwek'],
     'meal_type': ['lunch', 'dinner']},

    {'name': 'Filet z dorsza z warzywami', 'calories': 300,
     'macros': {'protein': 25, 'carbs': 20, 'fats': 10},
     'ingredients': ['filet z dorsza', 'brokuły', 'marchew', 'ziemniaki', 'oliwa z oliwek'],
     'meal_type': ['lunch', 'dinner']},

    {'name': 'Omlet ze szpinakiem', 'calories': 270,
     'macros': {'protein': 20, 'carbs': 10, 'fats': 15},
     'ingredients': ['jajka', 'szpinak', 'ser feta', 'oliwa z oliwek', 'czosnek'],
     'meal_type': ['breakfast']},

    {'name': 'Curry z ciecierzycą', 'calories': 380,
     'macros': {'protein': 15, 'carbs': 50, 'fats': 15},
     'ingredients': ['ciecierzyca', 'mleko kokosowe', 'pomidory', 'cebula', 'przyprawy curry'],
     'meal_type': ['lunch', 'dinner']},

    {'name': 'Batony energetyczne owsiane', 'calories': 200,
     'macros': {'protein': 5, 'carbs': 30, 'fats': 8},
     'ingredients': ['płatki owsiane', 'miód', 'masło orzechowe', 'rodzynki', 'orzechy'],
     'meal_type': ['snack']},

    {'name': 'Zapiekanka makaronowa z serem', 'calories': 450,
     'macros': {'protein': 20, 'carbs': 60, 'fats': 15},
     'ingredients': ['makaron', 'ser mozzarella', 'sos pomidorowy', 'ser parmezan', 'szpinak'],
     'meal_type': ['dinner']},

    {'name': 'Kasza jaglana z pieczonymi warzywami', 'calories': 340,
     'macros': {'protein': 12, 'carbs': 55, 'fats': 6},
     'ingredients': ['kasza jaglana', 'papryka', 'cukinia', 'bakłażan', 'oliwa z oliwek'],
     'meal_type': ['lunch', 'dinner']},

    {'name': 'Smoothie truskawkowo-jogurtowe', 'calories': 220,
     'macros': {'protein': 8, 'carbs': 40, 'fats': 5},
     'ingredients': ['truskawki', 'jogurt naturalny', 'miód', 'banana'],
     'meal_type': ['breakfast', 'snack']},

    {'name': 'Chili z fasolą i warzywami', 'calories': 400,
     'macros': {'protein': 18, 'carbs': 50, 'fats': 12},
     'ingredients': ['fasola', 'papryka', 'pomidor', 'cebula', 'czosnek', 'przyprawy chili'],
     'meal_type': ['lunch', 'dinner']},

    {'name': 'Tosty z jajkiem i szpinakiem', 'calories': 310,
     'macros': {'protein': 15, 'carbs': 35, 'fats': 12},
     'ingredients': ['chleb pełnoziarnisty', 'jajka', 'szpinak', 'oliwa z oliwek'],
     'meal_type': ['breakfast', 'lunch']},

    {'name': 'Ryż z pieczarkami i brokułami', 'calories': 330,
     'macros': {'protein': 10, 'carbs': 50, 'fats': 8},
     'ingredients': ['ryż', 'pieczarki', 'brokuły', 'cebula', 'oliwa z oliwek'],
     'meal_type': ['lunch', 'dinner']},

    {'name': 'Zapiekanka z ziemniakami i szpinakiem', 'calories': 380,
     'macros': {'protein': 15, 'carbs': 45, 'fats': 10},
     'ingredients': ['ziemniaki', 'szpinak', 'ser feta', 'czosnek', 'cebula'],
     'meal_type': ['dinner']},

    {'name': 'Owsianka z masłem orzechowym i bananem', 'calories': 350,
     'macros': {'protein': 12, 'carbs': 55, 'fats': 12},
     'ingredients': ['płatki owsiane', 'masło orzechowe', 'banan', 'mleko'],
     'meal_type': ['breakfast']},

    {'name': 'Quinoa z pieczoną papryką i cukinią', 'calories': 300,
     'macros': {'protein': 10, 'carbs': 40, 'fats': 8},
     'ingredients': ['quinoa', 'papryka', 'cukinia', 'oliwa z oliwek', 'czosnek'],
     'meal_type': ['lunch', 'dinner']},

    {'name': 'Kanapka z hummusem i pomidorem', 'calories': 280,
     'macros': {'protein': 7, 'carbs': 35, 'fats': 10},
     'ingredients': ['chleb pełnoziarnisty', 'hummus', 'pomidory', 'rukola'],
     'meal_type': ['breakfast', 'lunch']},

    {'name': 'Koktajl białkowy z owocami leśnymi', 'calories': 250,
     'macros': {'protein': 20, 'carbs': 35, 'fats': 5},
     'ingredients': ['białko w proszku', 'jogurt naturalny', 'owoce leśne', 'mleko'],
     'meal_type': ['breakfast', 'snack']},

    {'name': 'Filet z kurczaka w sosie szpinakowym', 'calories': 400,
     'macros': {'protein': 30, 'carbs': 15, 'fats': 18},
     'ingredients': ['filet z kurczaka', 'szpinak', 'śmietana', 'czosnek', 'cebula'],
     'meal_type': ['lunch', 'dinner']},

    {'name': 'Makaron z pomidorami i bazylią', 'calories': 350,
     'macros': {'protein': 12, 'carbs': 55, 'fats': 10},
     'ingredients': ['makaron', 'pomidory', 'bazylia', 'czosnek', 'oliwa z oliwek'],
     'meal_type': ['lunch', 'dinner']},

    {'name': 'Budyń jaglany z owocami', 'calories': 240, 'macros': {'protein': 6, 'carbs': 35, 'fats': 8},
     'meal_type': ['breakfast', 'snack'],
     'ingredients': ['kasza jaglana', 'mleko', 'miód', 'owoce (np. truskawki, jagody)']},

    {'name': 'Szaszłyki warzywne z tofu', 'calories': 300, 'macros': {'protein': 15, 'carbs': 30, 'fats': 12},
     'meal_type': ['lunch', 'dinner'],
     'ingredients': ['tofu', 'papryka', 'cukinia', 'cebula', 'oliwa z oliwek', 'przyprawy (np. papryka, czosnek)']},

    {'name': 'Jajka sadzone z pomidorami i rukolą', 'calories': 250, 'macros': {'protein': 14, 'carbs': 5, 'fats': 18},
     'meal_type': ['breakfast'], 'ingredients': ['jajka', 'pomidory', 'rukola', 'oliwa z oliwek']},

    {'name': 'Placuszki z cukinii', 'calories': 280, 'macros': {'protein': 10, 'carbs': 30, 'fats': 12},
     'meal_type': ['breakfast', 'lunch'],
     'ingredients': ['cukinia', 'jajka', 'mąka', 'czosnek', 'przyprawy (np. sól, pieprz)', 'oliwa z oliwek']},

    {'name': 'Kurczak curry z warzywami', 'calories': 380, 'macros': {'protein': 30, 'carbs': 25, 'fats': 15},
     'meal_type': ['lunch', 'dinner'],
     'ingredients': ['pierś z kurczaka', 'mleko kokosowe', 'marchew', 'papryka', 'cebula', 'czosnek',
                     'przyprawy curry']},

    {'name': 'Owsianka z cynamonem i orzechami', 'calories': 320, 'macros': {'protein': 10, 'carbs': 40, 'fats': 10},
     'meal_type': ['breakfast'], 'ingredients': ['płatki owsiane', 'mleko', 'cynamon', 'orzechy', 'miód']},

    {'name': 'Pieczone bataty z fasolą i kukurydzą', 'calories': 350, 'macros': {'protein': 12, 'carbs': 60, 'fats': 8},
     'meal_type': ['lunch', 'dinner'],
     'ingredients': ['bataty', 'fasola', 'kukurydza', 'oliwa z oliwek', 'przyprawy (np. papryka, czosnek)']},

    {'name': 'Makaron z cukinią i suszonymi pomidorami', 'calories': 400,
     'macros': {'protein': 15, 'carbs': 65, 'fats': 8},
     'meal_type': ['lunch', 'dinner'],
     'ingredients': ['makaron', 'cukinia', 'suszony pomidor', 'czosnek', 'oliwa z oliwek', 'bazylia']},

    {'name': 'Shake proteinowy z masłem orzechowym i bananem', 'calories': 300,
     'macros': {'protein': 25, 'carbs': 30, 'fats': 10},
     'meal_type': ['breakfast', 'snack', 'dinner'],
     'ingredients': ['białko w proszku', 'masło orzechowe', 'banan', 'mleko']},

    {'name': 'Podwójna sałatka z kurczakiem', 'calories': 800, 'macros': {'protein': 60, 'carbs': 40, 'fats': 30},
     'meal_type': ['lunch', 'dinner'],
     'ingredients': ['pierś z kurczaka', 'rukola', 'pomidory', 'ogórek', 'oliwa z oliwek', 'ocet balsamiczny']},

    {'name': 'Podwójna zupa jarzynowa', 'calories': 300, 'macros': {'protein': 10, 'carbs': 50, 'fats': 10},
     'meal_type': ['lunch', 'dinner'],
     'ingredients': ['marchew', 'ziemniaki', 'por', 'seler', 'cebula', 'czosnek', 'przyprawy']},

    {'name': 'Podwójny omlet warzywny', 'calories': 500, 'macros': {'protein': 36, 'carbs': 20, 'fats': 30},
     'meal_type': ['breakfast'],
     'ingredients': ['jajka', 'szpinak', 'papryka', 'pomidor', 'cebula', 'ser feta', 'oliwa z oliwek']},

    {'name': 'Podwójna porcja ryżu z warzywami i tofu', 'calories': 640,
     'macros': {'protein': 30, 'carbs': 100, 'fats': 16},
     'meal_type': ['lunch', 'dinner'],
     'ingredients': ['tofu', 'ryż', 'marchew', 'brokuły', 'soja', 'czosnek', 'imbir']},

    {'name': 'Podwójna kanapka z awokado i jajkiem', 'calories': 700,
     'macros': {'protein': 24, 'carbs': 60, 'fats': 40},
     'meal_type': ['breakfast', 'lunch'],
     'ingredients': ['chleb pełnoziarnisty', 'awokado', 'jajka', 'rukola', 'pomidor', 'oliwa z oliwek']},

    {'name': 'Podwójny kurczak z kaszą bulgur', 'calories': 900, 'macros': {'protein': 70, 'carbs': 90, 'fats': 20},
     'meal_type': ['lunch', 'dinner'],
     'ingredients': ['pierś z kurczaka', 'kasza bulgur', 'cebula', 'czosnek', 'papryka', 'oliwa z oliwek']},

    {'name': 'Podwójna porcja pasty z soczewicą', 'calories': 800, 'macros': {'protein': 40, 'carbs': 120, 'fats': 16},
     'meal_type': ['lunch', 'dinner'],
     'ingredients': ['soczewica', 'makaron', 'pomidory', 'czosnek', 'cebula', 'przyprawy (np. oregano, tymianek)']},

    {'name': 'Podwójny łosoś z batatami', 'calories': 1000, 'macros': {'protein': 70, 'carbs': 80, 'fats': 40},
     'meal_type': ['dinner'], 'ingredients': ['łosoś', 'bataty', 'oliwa z oliwek', 'czosnek', 'rozmaryn']},

    {'name': 'Podwójna sałatka grecka', 'calories': 440, 'macros': {'protein': 16, 'carbs': 20, 'fats': 30},
     'meal_type': ['lunch', 'dinner'],
     'ingredients': ['ogórek', 'pomidory', 'ser feta', 'oliwki', 'cebula', 'oliwa z oliwek', 'oregano']},

    {'name': 'Podwójne smoothie bananowo-szpinakowe', 'calories': 360,
     'macros': {'protein': 10, 'carbs': 70, 'fats': 4},
     'meal_type': ['breakfast', 'snack'], 'ingredients': ['banan', 'szpinak', 'mleko', 'jogurt naturalny', 'miód']},

    {'name': 'Podwójny indyk z ryżem i brokułami', 'calories': 900, 'macros': {'protein': 80, 'carbs': 100, 'fats': 16},
     'meal_type': ['lunch', 'dinner'], 'ingredients': ['indyk', 'ryż', 'brokuły', 'czosnek', 'oliwa z oliwek']},

    {'name': 'Podwójna porcja pieczonych warzyw z komosą ryżową', 'calories': 600,
     'macros': {'protein': 20, 'carbs': 90, 'fats': 16},
     'meal_type': ['lunch', 'dinner'],
     'ingredients': ['warzywa (np. papryka, cukinia)', 'komosa ryżowa', 'oliwa z oliwek', 'czosnek', 'przyprawy']},

    {'name': 'Podwójne placuszki owsiane', 'calories': 580, 'macros': {'protein': 20, 'carbs': 80, 'fats': 20},
     'meal_type': ['breakfast'], 'ingredients': ['płatki owsiane', 'jajka', 'mleko', 'cynamon', 'orzechy']},

    {'name': 'Podwójna tortilla z hummusem i warzywami', 'calories': 700,
     'macros': {'protein': 20, 'carbs': 100, 'fats': 24},
     'meal_type': ['lunch', 'dinner'],
     'ingredients': ['tortilla', 'hummus', 'warzywa (np. papryka, sałata)', 'oliwa z oliwek']},

    {'name': 'Podwójna zapiekanka z batatem i kurczakiem', 'calories': 960,
     'macros': {'protein': 60, 'carbs': 110, 'fats': 30},
     'meal_type': ['dinner'], 'ingredients': ['bataty', 'kurczak', 'ser mozzarella', 'czosnek', 'oliwa z oliwek']},

    {'name': 'Podwójna porcja makaronu z warzywami i tofu', 'calories': 800,
     'macros': {'protein': 30, 'carbs': 130, 'fats': 16},
     'meal_type': ['lunch', 'dinner'],
     'ingredients': ['makaron', 'tofu', 'cukinia', 'papryka', 'czosnek', 'sos sojowy']},

    {'name': 'Podwójna porcja gulaszu warzywnego z ciecierzycą', 'calories': 740,
     'macros': {'protein': 40, 'carbs': 90, 'fats': 24},
     'meal_type': ['lunch', 'dinner'],
     'ingredients': ['ciecierzyca', 'marchew', 'papryka', 'pomidory', 'czosnek', 'przyprawy']},

    {'name': 'Podwójna kanapka z masłem orzechowym', 'calories': 560,
     'macros': {'protein': 16, 'carbs': 50, 'fats': 36},
     'meal_type': ['breakfast', 'snack'], 'ingredients': ['chleb pełnoziarnisty', 'masło orzechowe', 'banan']},

    {'name': 'Podwójna porcja budyniu chia z owocami', 'calories': 400,
     'macros': {'protein': 10, 'carbs': 60, 'fats': 16},
     'meal_type': ['breakfast', 'snack'],
     'ingredients': ['nasiona chia', 'mleko roślinne', 'miód', 'owoce (np. jagody, banan)']},

    {'name': 'Podwójna porcja ryżu z fasolą i warzywami', 'calories': 700,
     'macros': {'protein': 24, 'carbs': 120, 'fats': 12},
     'meal_type': ['lunch', 'dinner'], 'ingredients': ['ryż', 'fasola', 'marchew', 'papryka', 'czosnek', 'przyprawy']},

    {'name': 'Podwójna kanapka z szynką i warzywami', 'calories': 600,
     'macros': {'protein': 30, 'carbs': 70, 'fats': 20},
     'meal_type': ['breakfast', 'lunch'],
     'ingredients': ['chleb pełnoziarnisty', 'szynka', 'sałata', 'pomidor', 'ogórek']},

    {'name': 'Podwójna sałatka z tuńczykiem', 'calories': 500, 'macros': {'protein': 40, 'carbs': 20, 'fats': 30},
     'meal_type': ['lunch', 'dinner'],
     'ingredients': ['tuńczyk w puszce', 'sałata', 'oliwki', 'pomidor', 'oliwa z oliwek']},

    {'name': 'Podwójna owsianka z owocami', 'calories': 640, 'macros': {'protein': 20, 'carbs': 100, 'fats': 16},
     'meal_type': ['breakfast'],
     'ingredients': ['płatki owsiane', 'mleko roślinne', 'miód', 'owoce (np. jagody, banan)']},

    {'name': 'Podwójna porcja kurczaka z warzywami', 'calories': 760,
     'macros': {'protein': 60, 'carbs': 40, 'fats': 30},
     'meal_type': ['lunch', 'dinner'], 'ingredients': ['kurczak', 'brokuły', 'marchew', 'czosnek', 'oliwa z oliwek']},

    {'name': 'Podwójna zupa krem z dyni', 'calories': 360, 'macros': {'protein': 8, 'carbs': 50, 'fats': 16},
     'meal_type': ['lunch', 'dinner'], 'ingredients': ['dynia', 'marchew', 'ziemniaki', 'czosnek', 'bulion warzywny']},

    {'name': 'Podwójny makaron pełnoziarnisty z sosem pomidorowym', 'calories': 660,
     'macros': {'protein': 20, 'carbs': 120, 'fats': 12},
     'meal_type': ['lunch', 'dinner'], 'ingredients': ['makaron pełnoziarnisty', 'sos pomidorowy', 'czosnek', 'basil']},

    {'name': 'Podwójny filet z dorsza z warzywami', 'calories': 600, 'macros': {'protein': 50, 'carbs': 40, 'fats': 20},
     'meal_type': ['lunch', 'dinner'], 'ingredients': ['dorsz', 'brokuły', 'marchew', 'czosnek', 'oliwa z oliwek']},

    {'name': 'Podwójny omlet ze szpinakiem', 'calories': 540, 'macros': {'protein': 40, 'carbs': 20, 'fats': 30},
     'meal_type': ['breakfast'], 'ingredients': ['jajka', 'szpinak', 'ser feta', 'oliwa z oliwek']},

    {'name': 'Podwójne curry z ciecierzycą', 'calories': 760, 'macros': {'protein': 30, 'carbs': 100, 'fats': 30},
     'meal_type': ['lunch', 'dinner'],
     'ingredients': ['ciecierzyca', 'pomidory', 'czosnek', 'imbir', 'przyprawy curry']},

    {'name': 'Podwójne batony energetyczne owsiane', 'calories': 400,
     'macros': {'protein': 10, 'carbs': 60, 'fats': 16},
     'meal_type': ['snack'], 'ingredients': ['płatki owsiane', 'masło orzechowe', 'miód', 'orzechy', 'owoce suszone']},

    {'name': 'Podwójna zapiekanka makaronowa z serem', 'calories': 900,
     'macros': {'protein': 40, 'carbs': 120, 'fats': 30},
     'meal_type': ['dinner'], 'ingredients': ['makaron', 'ser żółty', 'ser mozzarella', 'czosnek', 'sos pomidorowy']},

    {'name': 'Podwójna kasza jaglana z pieczonymi warzywami', 'calories': 680,
     'macros': {'protein': 24, 'carbs': 110, 'fats': 12},
     'meal_type': ['lunch', 'dinner'],
     'ingredients': ['kasza jaglana', 'cukinia', 'papryka', 'bakłażan', 'oliwa z oliwek']},

    {'name': 'Podwójne smoothie truskawkowo-jogurtowe', 'calories': 440,
     'macros': {'protein': 16, 'carbs': 80, 'fats': 10},
     'meal_type': ['breakfast', 'snack'],
     'ingredients': ['truskawki', 'jogurt naturalny', 'miód', 'baza mleczna (np. mleko roślinne)']},

    {'name': 'Podwójny shake proteinowy z masłem orzechowym i bananem', 'calories': 600,
     'macros': {'protein': 50, 'carbs': 60, 'fats': 20},
     'meal_type': ['breakfast', 'snack', 'dinner'],
     'ingredients': ['białko w proszku', 'masło orzechowe', 'banan', 'mleko roślinne']},

    {'name': 'Tofu stir-fry z warzywami', 'calories': 300, 'macros': {'protein': 15, 'carbs': 40, 'fats': 10},
     'meal_type': ['lunch', 'dinner'], 'ingredients': ['tofu', 'papryka', 'cukinia', 'soja', 'czosnek', 'przyprawy']},

    {'name': 'Podwójne tofu stir-fry z warzywami', 'calories': 600, 'macros': {'protein': 30, 'carbs': 80, 'fats': 20},
     'meal_type': ['lunch', 'dinner'], 'ingredients': ['tofu', 'brokuły', 'marchew', 'soja', 'czosnek', 'imbir']},

    {'name': 'Pasta z pesto i pomidorkami', 'calories': 350, 'macros': {'protein': 10, 'carbs': 60, 'fats': 12},
     'meal_type': ['lunch', 'dinner'], 'ingredients': ['makaron', 'pesto', 'pomidorki koktajlowe', 'czosnek']},

    {'name': 'Podwójna pasta z pesto i pomidorkami', 'calories': 700,
     'macros': {'protein': 20, 'carbs': 120, 'fats': 24},
     'meal_type': ['lunch', 'dinner'], 'ingredients': ['makaron', 'pesto', 'pomidorki koktajlowe', 'czosnek']},

    {'name': 'Ryż z krewetkami i brokułami', 'calories': 400, 'macros': {'protein': 25, 'carbs': 50, 'fats': 12},
     'meal_type': ['lunch', 'dinner'], 'ingredients': ['ryż', 'krewetki', 'brokuły', 'czosnek', 'sos sojowy']},

    {'name': 'Podwójna porcja ryżu z krewetkami i brokułami', 'calories': 800,
     'macros': {'protein': 50, 'carbs': 100, 'fats': 24},
     'meal_type': ['lunch', 'dinner'], 'ingredients': ['ryż', 'krewetki', 'brokuły', 'czosnek', 'sos sojowy']},

    {'name': 'Frittata z warzywami', 'calories': 250, 'macros': {'protein': 18, 'carbs': 15, 'fats': 12},
     'meal_type': ['breakfast'], 'ingredients': ['jajka', 'papryka', 'szpinak', 'czosnek', 'ser']},

    {'name': 'Podwójna frittata z warzywami', 'calories': 500, 'macros': {'protein': 36, 'carbs': 30, 'fats': 24},
     'meal_type': ['breakfast'], 'ingredients': ['jajka', 'papryka', 'szpinak', 'czosnek', 'ser']},

    {'name': 'Chili con carne', 'calories': 450, 'macros': {'protein': 30, 'carbs': 55, 'fats': 15},
     'meal_type': ['lunch', 'dinner'],
     'ingredients': ['mielona wołowina', 'fasola czerwona', 'pomidory', 'czosnek', 'papryka']},

    {'name': 'Podwójne chili con carne', 'calories': 900, 'macros': {'protein': 60, 'carbs': 110, 'fats': 30},
     'meal_type': ['lunch', 'dinner'],
     'ingredients': ['mielona wołowina', 'fasola czerwona', 'pomidory', 'czosnek', 'papryka']},

    {'name': 'Smoothie z mango i jogurtem', 'calories': 200, 'macros': {'protein': 8, 'carbs': 35, 'fats': 4},
     'meal_type': ['breakfast', 'snack'],
     'ingredients': ['mango', 'jogurt naturalny', 'miód', 'baza mleczna (np. mleko roślinne)']},

    {'name': 'Podwójne smoothie z mango i jogurtem', 'calories': 400, 'macros': {'protein': 16, 'carbs': 70, 'fats': 8},
     'meal_type': ['breakfast', 'snack'],
     'ingredients': ['mango', 'jogurt naturalny', 'miód', 'baza mleczna (np. mleko roślinne)']},

    {'name': 'Kurczak tikka masala z ryżem', 'calories': 500, 'macros': {'protein': 35, 'carbs': 50, 'fats': 20},
     'meal_type': ['lunch', 'dinner'],
     'ingredients': ['kurczak', 'przyprawy tikka masala', 'ryż', 'mleko kokosowe', 'czosnek']},

    {'name': 'Podwójna porcja kurczaka tikka masala z ryżem', 'calories': 1000,
     'macros': {'protein': 70, 'carbs': 100, 'fats': 40},
     'meal_type': ['lunch', 'dinner'],
     'ingredients': ['kurczak', 'przyprawy tikka masala', 'ryż', 'mleko kokosowe', 'czosnek']},

    {'name': 'Wrap z warzywami i hummusem', 'calories': 350, 'macros': {'protein': 12, 'carbs': 50, 'fats': 10},
     'meal_type': ['lunch', 'snack'], 'ingredients': ['tortilla', 'hummus', 'papryka', 'ogórek', 'szpinak']},

    {'name': 'Podwójny wrap z warzywami i hummusem', 'calories': 700,
     'macros': {'protein': 24, 'carbs': 100, 'fats': 20},
     'meal_type': ['lunch', 'snack'], 'ingredients': ['tortilla', 'hummus', 'papryka', 'ogórek', 'szpinak']},

    {'name': 'Makaron z sosem pieczarkowym', 'calories': 400, 'macros': {'protein': 15, 'carbs': 60, 'fats': 10},
     'meal_type': ['lunch', 'dinner'], 'ingredients': ['makaron', 'pieczarki', 'czosnek', 'śmietana', 'pietruszka']},

    {'name': 'Podwójny makaron z sosem pieczarkowym', 'calories': 800,
     'macros': {'protein': 30, 'carbs': 120, 'fats': 20},
     'meal_type': ['lunch', 'dinner'], 'ingredients': ['makaron', 'pieczarki', 'czosnek', 'śmietana', 'pietruszka']},

    {'name': 'Sałatka owocowa', 'calories': 150, 'macros': {'protein': 3, 'carbs': 35, 'fats': 2},
     'meal_type': ['snack'], 'ingredients': ['owoce (np. jabłka, pomarańcze, winogrona)', 'miód']},

    {'name': 'Podwójna sałatka owocowa', 'calories': 300, 'macros': {'protein': 6, 'carbs': 70, 'fats': 4},
     'meal_type': ['snack'], 'ingredients': ['owoce (np. jabłka, pomarańcze, winogrona)', 'miód']},

    {'name': 'Quinoa z pieczonym kurczakiem i brokułami', 'calories': 450,
     'macros': {'protein': 30, 'carbs': 50, 'fats': 15},
     'meal_type': ['lunch', 'dinner'], 'ingredients': ['quinoa', 'kurczak', 'brokuły', 'oliwa z oliwek', 'czosnek']},

    {'name': 'Podwójna porcja quinoa z pieczonym kurczakiem i brokułami', 'calories': 900,
     'macros': {'protein': 60, 'carbs': 100, 'fats': 30},
     'meal_type': ['lunch', 'dinner'], 'ingredients': ['quinoa', 'kurczak', 'brokuły', 'oliwa z oliwek', 'czosnek']},

    {'name': 'Miso ramen z tofu', 'calories': 350, 'macros': {'protein': 12, 'carbs': 55, 'fats': 10},
     'meal_type': ['lunch', 'dinner'],
     'ingredients': ['miso pasta', 'tofu', 'makaron ramen', 'woda', 'zielona cebulka', 'marchew', 'szpinak']},
    {'name': 'Podwójna porcja miso ramen z tofu', 'calories': 700, 'macros': {'protein': 24, 'carbs': 110, 'fats': 20},
     'meal_type': ['lunch', 'dinner'],
     'ingredients': ['miso pasta', 'tofu', 'makaron ramen', 'woda', 'zielona cebulka', 'marchew', 'szpinak']},

    {'name': 'Owsianka z owocami i orzechami', 'calories': 300, 'macros': {'protein': 10, 'carbs': 50, 'fats': 10},
     'meal_type': ['breakfast'], 'ingredients': ['płatki owsiane', 'mleko', 'owoce (np. jagody, truskawki)',
                                                 'orzechy (np. migdały, orzechy włoskie)', 'miód']},
    {'name': 'Podwójna porcja owsianki z owocami i orzechami', 'calories': 600,
     'macros': {'protein': 20, 'carbs': 100, 'fats': 20}, 'meal_type': ['breakfast'],
     'ingredients': ['płatki owsiane', 'mleko', 'owoce (np. jagody, truskawki)',
                     'orzechy (np. migdały, orzechy włoskie)', 'miód']},

    {'name': 'Grillowana pierś z kurczaka z batatami', 'calories': 450,
     'macros': {'protein': 35, 'carbs': 40, 'fats': 15}, 'meal_type': ['lunch', 'dinner'],
     'ingredients': ['pierś z kurczaka', 'bataty', 'oliwa z oliwek', 'czosnek', 'sól', 'pieprz']},
    {'name': 'Podwójna porcja grillowanej piersi z kurczaka z batatami', 'calories': 900,
     'macros': {'protein': 70, 'carbs': 80, 'fats': 30}, 'meal_type': ['lunch', 'dinner'],
     'ingredients': ['pierś z kurczaka', 'bataty', 'oliwa z oliwek', 'czosnek', 'sól', 'pieprz']},

    {'name': 'Koktajl proteinowy z bananem', 'calories': 200, 'macros': {'protein': 20, 'carbs': 30, 'fats': 2},
     'meal_type': ['snack', 'breakfast'],
     'ingredients': ['proszek białkowy', 'banan', 'mleko roślinne', 'masło orzechowe']},
    {'name': 'Podwójna porcja koktajlu proteinowego z bananem', 'calories': 400,
     'macros': {'protein': 40, 'carbs': 60, 'fats': 4}, 'meal_type': ['snack', 'breakfast'],
     'ingredients': ['proszek białkowy', 'banan', 'mleko roślinne', 'masło orzechowe']},

    {'name': 'Makaron pełnoziarnisty z sosem bolońskim', 'calories': 500,
     'macros': {'protein': 25, 'carbs': 65, 'fats': 15}, 'meal_type': ['lunch', 'dinner'],
     'ingredients': ['makaron pełnoziarnisty', 'mielona wołowina', 'pomidory', 'czosnek', 'cebula',
                     'przyprawy (bazylia, oregano)', 'oliwa z oliwek']},
    {'name': 'Podwójny makaron pełnoziarnisty z sosem bolońskim', 'calories': 1000,
     'macros': {'protein': 50, 'carbs': 130, 'fats': 30}, 'meal_type': ['lunch', 'dinner'],
     'ingredients': ['makaron pełnoziarnisty', 'mielona wołowina', 'pomidory', 'czosnek', 'cebula',
                     'przyprawy (bazylia, oregano)', 'oliwa z oliwek']},

    {'name': 'Sałatka grecka', 'calories': 250, 'macros': {'protein': 7, 'carbs': 20, 'fats': 15},
     'meal_type': ['lunch', 'snack'],
     'ingredients': ['pomidor', 'ogórek', 'cebula', 'feta', 'oliwki', 'oliwa z oliwek', 'oregano']},
    {'name': 'Podwójna porcja sałatki greckiej', 'calories': 500, 'macros': {'protein': 14, 'carbs': 40, 'fats': 30},
     'meal_type': ['lunch', 'snack'],
     'ingredients': ['pomidor', 'ogórek', 'cebula', 'feta', 'oliwki', 'oliwa z oliwek', 'oregano']},

    {'name': 'Łosoś pieczony z kaszą bulgur', 'calories': 550, 'macros': {'protein': 35, 'carbs': 45, 'fats': 20},
     'meal_type': ['lunch', 'dinner'],
     'ingredients': ['łosoś', 'kasza bulgur', 'oliwa z oliwek', 'czosnek', 'cytryna', 'szpinak']},
    {'name': 'Podwójna porcja łososia pieczonego z kaszą bulgur', 'calories': 1100,
     'macros': {'protein': 70, 'carbs': 90, 'fats': 40}, 'meal_type': ['lunch', 'dinner'],
     'ingredients': ['łosoś', 'kasza bulgur', 'oliwa z oliwek', 'czosnek', 'cytryna', 'szpinak']},

    {'name': 'Placuszki bananowe', 'calories': 300, 'macros': {'protein': 8, 'carbs': 45, 'fats': 10},
     'meal_type': ['breakfast', 'snack'],
     'ingredients': ['banan', 'mąka', 'jajka', 'mleko roślinne', 'proszek do pieczenia', 'olej kokosowy']},
    {'name': 'Podwójna porcja placuszków bananowych', 'calories': 600,
     'macros': {'protein': 16, 'carbs': 90, 'fats': 20}, 'meal_type': ['breakfast', 'snack'],
     'ingredients': ['banan', 'mąka', 'jajka', 'mleko roślinne', 'proszek do pieczenia', 'olej kokosowy']},

    {'name': 'Ryż z ciecierzycą i warzywami', 'calories': 350, 'macros': {'protein': 12, 'carbs': 60, 'fats': 8},
     'meal_type': ['lunch', 'dinner'],
     'ingredients': ['ryż', 'ciecierzyca', 'papryka', 'cukinia', 'czosnek', 'oliwa z oliwek', 'sól', 'pieprz']},
    {'name': 'Podwójna porcja ryżu z ciecierzycą i warzywami', 'calories': 700,
     'macros': {'protein': 24, 'carbs': 120, 'fats': 16}, 'meal_type': ['lunch', 'dinner'],
     'ingredients': ['ryż', 'ciecierzyca', 'papryka', 'cukinia', 'czosnek', 'oliwa z oliwek', 'sól', 'pieprz']},

    {'name': 'Omlet z szynką i serem', 'calories': 250, 'macros': {'protein': 20, 'carbs': 5, 'fats': 15},
     'meal_type': ['breakfast'], 'ingredients': ['jajka', 'szynka', 'ser żółty', 'oliwa z oliwek', 'sól', 'pieprz']},
    {'name': 'Podwójna porcja omleta z szynką i serem', 'calories': 500,
     'macros': {'protein': 40, 'carbs': 10, 'fats': 30}, 'meal_type': ['breakfast'],
     'ingredients': ['jajka', 'szynka', 'ser żółty', 'oliwa z oliwek', 'sól', 'pieprz']},

    {'name': 'Budyń chia z mlekiem kokosowym i malinami', 'calories': 200,
     'macros': {'protein': 5, 'carbs': 25, 'fats': 10}, 'meal_type': ['snack'],
     'ingredients': ['nasiona chia', 'mleko kokosowe', 'maliny', 'miód']},
    {'name': 'Podwójna porcja budyniu chia z mlekiem kokosowym i malinami', 'calories': 400,
     'macros': {'protein': 10, 'carbs': 50, 'fats': 20}, 'meal_type': ['snack'],
     'ingredients': ['nasiona chia', 'mleko kokosowe', 'maliny', 'miód']},

    {'name': 'Wrap z tuńczykiem i warzywami', 'calories': 350, 'macros': {'protein': 25, 'carbs': 40, 'fats': 10},
     'meal_type': ['lunch', 'snack'],
     'ingredients': ['tortilla', 'tuńczyk', 'sałata', 'papryka', 'ogórek', 'oliwa z oliwek']},
    {'name': 'Podwójny wrap z tuńczykiem i warzywami', 'calories': 700,
     'macros': {'protein': 50, 'carbs': 80, 'fats': 20}, 'meal_type': ['lunch', 'snack'],
     'ingredients': ['tortilla', 'tuńczyk', 'sałata', 'papryka', 'ogórek', 'oliwa z oliwek']},

    {'name': 'Zupa krem z dyni', 'calories': 150, 'macros': {'protein': 3, 'carbs': 25, 'fats': 5},
     'meal_type': ['lunch', 'snack'],
     'ingredients': ['dynia', 'czosnek', 'cebula', 'bulion warzywny', 'śmietanka roślinna', 'sól', 'pieprz']},
    {'name': 'Podwójna porcja zupy krem z dyni', 'calories': 300, 'macros': {'protein': 6, 'carbs': 50, 'fats': 10},
     'meal_type': ['lunch', 'snack'],
     'ingredients': ['dynia', 'czosnek', 'cebula', 'bulion warzywny', 'śmietanka roślinna', 'sól', 'pieprz']},

    {'name': 'Sałatka z komosą ryżową, szpinakiem i fetą', 'calories': 250,
     'macros': {'protein': 8, 'carbs': 30, 'fats': 12}, 'meal_type': ['lunch', 'snack'],
     'ingredients': ['komosa ryżowa', 'szpinak', 'feta', 'pomidory', 'ogórek', 'oliwa z oliwek']},
    {'name': 'Podwójna porcja sałatki z komosą ryżową, szpinakiem i fetą', 'calories': 500,
     'macros': {'protein': 16, 'carbs': 60, 'fats': 24}, 'meal_type': ['lunch', 'snack'],
     'ingredients': ['komosa ryżowa', 'szpinak', 'feta', 'pomidory', 'ogórek', 'oliwa z oliwek']},

    {'name': 'Kanapka z jajkiem i awokado', 'calories': 300, 'macros': {'protein': 12, 'carbs': 35, 'fats': 15},
     'meal_type': ['breakfast', 'snack'],
     'ingredients': ['chleb pełnoziarnisty', 'jajko', 'awokado', 'oliwa z oliwek', 'sól', 'pieprz']},
    {'name': 'Podwójna kanapka z jajkiem i awokado', 'calories': 600,
     'macros': {'protein': 24, 'carbs': 70, 'fats': 30}, 'meal_type': ['breakfast', 'snack'],
     'ingredients': ['chleb pełnoziarnisty', 'jajko', 'awokado', 'oliwa z oliwek', 'sól', 'pieprz']},

]

class AllRecipesView(APIView):
    def get(self, request):
        return Response(available_recipes)