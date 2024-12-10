import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import { Box, Button, Typography, TextField, Chip, List, ListItemButton, ListItemText, Grid, Paper, CircularProgress } from '@mui/material';
import Navbar from './Navbar'; // Import Navbar

function DietPlanForm() {
    const navigate = useNavigate();
    const [allRecipes, setAllRecipes] = useState([]);
    const [avoidedIngredients, setAvoidedIngredients] = useState([]);
    const [ingredientInput, setIngredientInput] = useState('');
    const [mealPreferences1, setMealPreferences1] = useState({
        breakfast: '',
        secondBreakfast: '',
        lunch: '',
        tea: '',
        dinner: '',
    });
    const [mealPreferences2, setMealPreferences2] = useState({
        breakfast: '',
        secondBreakfast: '',
        lunch: '',
        tea: '',
        dinner: '',
    });
    const [mealPreferences3, setMealPreferences3] = useState({
        breakfast: '',
        secondBreakfast: '',
        lunch: '',
        tea: '',
        dinner: '',
    });
    const [mealInput, setMealInput] = useState('');
    const [focusedMeal1, setFocusedMeal1] = useState(null);
    const [focusedMeal2, setFocusedMeal2] = useState(null);
    const [focusedMeal3, setFocusedMeal3] = useState(null);
    const [username, setUsername] = useState('');
    const [loading, setLoading] = useState(false);  // Stan ładowania

    // Mapa tłumaczeń posiłków
    const mealTranslations = {
        breakfast: 'Śniadanie',
        secondBreakfast: 'Drugie śniadanie',
        lunch: 'Obiad',
        tea: 'Podwieczorek',
        dinner: 'Kolacja',
    };

    useEffect(() => {
        const token = localStorage.getItem('access_token');
        const storedUsername = localStorage.getItem('username');

        if (!token) {
            navigate('/login');
        } else {
            setUsername(storedUsername);
        }
    }, [navigate]);

    useEffect(() => {
        const fetchRecipes = async () => {
            try {
                const response = await axios.get('http://localhost:8000/api/all_recipes/');
                setAllRecipes(response.data);
            } catch (error) {
                console.error('Error fetching recipes:', error);
            }
        };

        fetchRecipes();
    }, []);

    const allIngredients = Array.from(new Set(allRecipes.flatMap((recipe) => recipe.ingredients)));

    const filteredIngredients = allIngredients.filter((ingredient) =>
        ingredient.toLowerCase().includes(ingredientInput.toLowerCase())
    );

    const filteredMeals = (mealType) => {
        // Znajdź wybrane snacki w innych mealType
        const selectedSnacks = Object.entries(mealPreferences1)
            .filter(([key, value]) => key !== mealType && value && isSnack(value)) // Wyklucz bieżący mealType i sprawdź, czy to snack
            .map(([, value]) => value); // Pobierz nazwy wybranych snacków

        const meals = allRecipes.filter(
            (recipe) =>
                (recipe.meal_type.includes(mealType) ||
                    (mealType === 'secondBreakfast' && recipe.meal_type.includes('breakfast') &&
                !selectedSnacks.includes(recipe.name)) ||
                    (mealType === 'tea' && recipe.meal_type.includes('breakfast'))) &&
                !selectedSnacks.includes(recipe.name) // Wyklucz już wybrane snacki
        );

        return meals.filter((recipe) =>
            recipe.name.toLowerCase().includes(mealInput.toLowerCase())
        );
    };

    const isSnack = (mealName) => {
    const meal = allRecipes.find((recipe) => recipe.name === mealName);
    return meal && meal.meal_type.includes('snack'); // Zakładamy, że posiłki mają pole 'meal_type'
    };



    const handleAddIngredient = (ingredient) => {
        if (ingredient && !avoidedIngredients.includes(ingredient) && avoidedIngredients.length < 4) {
            setAvoidedIngredients([...avoidedIngredients, ingredient]);
            setIngredientInput('');
        } else if (avoidedIngredients.length >= 5) {
            alert('Możesz dodać maksymalnie 5 składniki do unikania.');
        }
    };


    const countSelectedMeals = (mealPreferences) => {
        return Object.values(mealPreferences).filter((meal) => meal !== '').length;
    };

    const handleIngredientRemove = (ingredientToRemove) => {
        setAvoidedIngredients(avoidedIngredients.filter((ingredient) => ingredient !== ingredientToRemove));
    };

    const handleMealPreferenceChange = (mealType, mealName, mealSet) => {
        const mealPreferences =
            mealSet === 1 ? mealPreferences1 :
            mealSet === 2 ? mealPreferences2 :
            mealPreferences3;

        const setMealPreferences =
            mealSet === 1 ? setMealPreferences1 :
            mealSet === 2 ? setMealPreferences2 :
            setMealPreferences3;

        const selectedMeals = Object.values(mealPreferences);

        // Sprawdzenie, czy posiłek już został wybrany w tym zestawie
        if (selectedMeals.includes(mealName) && mealPreferences[mealType] !== mealName) {
            alert('To danie zostało już wybrane w tym zestawie. Wybierz inne danie.');
            return;  // Zatrzymanie dalszego działania
        }

        const selectedCount = countSelectedMeals(mealPreferences);

        if (selectedCount < 2 || mealPreferences[mealType] === mealName) {
            setMealPreferences((prev) => ({
                ...prev,
                [mealType]: prev[mealType] === mealName ? '' : mealName
            }));
            setMealInput('');
            if (mealSet === 1) setFocusedMeal1(null);
            else if (mealSet === 2) setFocusedMeal2(null);
            else setFocusedMeal3(null);
        } else {
            alert('Możesz wybrać maksymalnie dwa posiłki w tym zestawie.');
        }
    };


    const handleMealClear = (mealType, mealSet) => {
        const setMealPreferences = (mealSet === 1) ? setMealPreferences1 :
                              (mealSet === 2) ? setMealPreferences2 : setMealPreferences3;

        setMealPreferences((prev) => ({
            ...prev,
            [mealType]: ''
        }));
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);  // Rozpoczęcie ładowania

        const preferences = {
            mealPreferences1,
            mealPreferences2,
            mealPreferences3,
            avoidedIngredients,
        };

        try {
            const token = localStorage.getItem('access_token');
            const response = await axios.post('http://localhost:8000/api/generate-diet/', preferences, {
                headers: { Authorization: `Bearer ${token}` },
            });
            localStorage.removeItem('dietPlans');
            const dietPlans = response.data.diet_plans;
            localStorage.setItem('dietPlans', JSON.stringify(dietPlans));

            navigate('/diet-result');
        } catch (error) {
            console.error('Error generating diet:', error);
            alert('Wystąpił błąd podczas generowania diety.');
        } finally {
            setLoading(false);  // Zakończenie ładowania
        }
    };

    return (
        <Box>
            <Navbar username={username} />
            <Box sx={{ display: 'flex', justifyContent: 'center', alignItems: 'center', minHeight: '100vh', backgroundColor: '#f4f4f9', padding: 3 }}>
                <Paper elevation={3} sx={{ maxWidth: 600, width: '100%', padding: 4 }}>
                    <Typography variant="h4" align="center" gutterBottom>Planowanie diety</Typography>
                    <Typography variant="h6" align="center" sx={{ color: 'blue', marginBottom: 4 }}  gutterBottom>Podczas generowania diety pamiętaj, dając za dużo ograniczeń jest szansa że algorytm nie zadziała  </Typography>
                    <form onSubmit={handleSubmit}>
                        <Box sx={{ mb: 3 }}>
                            <Typography variant="h6" gutterBottom>Produkty do unikania (maksymalnie 5):</Typography>
                            <Box sx={{ display: 'flex', flexDirection: 'column', gap: 2 }}>
                                <TextField
                                    value={ingredientInput}
                                    onChange={(e) => setIngredientInput(e.target.value)}
                                    placeholder="Wpisz składnik do unikania"
                                    variant="outlined"
                                    fullWidth
                                />
                                {ingredientInput && (
                                    <List sx={{ maxHeight: 200, overflowY: 'auto', border: '1px solid #ddd' }}>
                                        {filteredIngredients.map((ingredient, index) => (
                                            <ListItemButton key={index} onClick={() => handleAddIngredient(ingredient)}>
                                                <ListItemText primary={ingredient} />
                                            </ListItemButton>
                                        ))}
                                    </List>
                                )}
                            </Box>
                            <Box sx={{ mt: 2, display: 'flex', flexWrap: 'wrap', gap: 1 }}>
                                {avoidedIngredients.map((ingredient, index) => (
                                    <Chip key={index} label={ingredient} onDelete={() => handleIngredientRemove(ingredient)} />
                                ))}
                            </Box>
                        </Box>

                        {/* Zestaw 1 */}
                        <Box sx={{ mb: 3 }}>
                            <Typography variant="h6" gutterBottom>Preferencje posiłków (Zestaw 1):</Typography>
                            <Typography
                                variant="h9"
                                gutterBottom
                                sx={{ color: 'blue'}} // kolor niebieski
                            >
                                Możesz wybrać maksymalnie 2 posiłki na zestaw
                            </Typography>
                            <Grid container spacing={2} sx={{ marginTop: 2 }}>
                                {['breakfast', 'secondBreakfast', 'lunch', 'tea', 'dinner'].map((mealType) => (
                                    <Grid item xs={15} sm={6} key={mealType}>
                                        <Box>
                                            <Typography>
                                            {mealTranslations[mealType]}
                                            </Typography>
                                            <TextField
                                                value={
                                                    mealPreferences1[mealType]
                                                        ? `${mealPreferences1[mealType]} (${filteredMeals(mealType).find(meal => meal.name === mealPreferences1[mealType])?.calories} kcal)`
                                                        : ''
                                                }
                                                onClick={() => setFocusedMeal1(mealType)}
                                                placeholder={`Wybierz ${mealTranslations[mealType]}`}
                                                InputProps={{ readOnly: true }}
                                                fullWidth
                                            />
                                            {countSelectedMeals(mealPreferences1) < 2 && focusedMeal1 === mealType && (
                                                <List sx={{ maxHeight: 200, overflowY: 'auto', border: '1px solid #ddd' }}>
                                                    {filteredMeals(mealType).map((meal) => (
                                                        <ListItemButton key={meal.name} onClick={() => handleMealPreferenceChange(mealType, meal.name, 1)} disabled={isSnack(meal.name) && Object.values(mealPreferences1).includes(meal.name)}>
                                                            <ListItemText primary={`${meal.name} (${meal.calories} kcal)`} />
                                                        </ListItemButton>
                                                    ))}
                                                </List>
                                            )}

                                            {mealPreferences1[mealType] && (
                                                <Button variant="contained" color="secondary" onClick={() => handleMealClear(mealType, 1)}>
                                                    Wyczyść
                                                </Button>
                                            )}
                                        </Box>
                                    </Grid>
                                ))}
                            </Grid>
                        </Box>

                        {/* Zestaw 2 */}
                        <Box sx={{ mb: 3 }}>
                            <Typography variant="h6" gutterBottom>Preferencje posiłków (Zestaw 2):</Typography>
                            <Grid container spacing={2}>
                                {['breakfast', 'secondBreakfast', 'lunch', 'tea', 'dinner'].map((mealType) => (
                                    <Grid item xs={12} sm={6} key={mealType}>
                                        <Box>
                                            <Typography>{mealTranslations[mealType]}</Typography>
                                            <TextField
                                                value={
                                                    mealPreferences2[mealType]
                                                        ? `${mealPreferences2[mealType]} (${filteredMeals(mealType).find(meal => meal.name === mealPreferences2[mealType])?.calories} kcal)`
                                                        : ''
                                                }
                                                onClick={() => setFocusedMeal2(mealType)}
                                                placeholder={`Wybierz ${mealTranslations[mealType]}`}
                                                InputProps={{ readOnly: true }}
                                                fullWidth
                                            />
                                            {countSelectedMeals(mealPreferences2) < 2 && focusedMeal2 === mealType && (
                                                <List sx={{ maxHeight: 200, overflowY: 'auto', border: '1px solid #ddd' }}>
                                                    {filteredMeals(mealType).map((meal) => (
                                                        <ListItemButton key={meal.name} onClick={() => handleMealPreferenceChange(mealType, meal.name, 2)} disabled={Object.values(mealPreferences2).includes(meal.name)}>
                                                            <ListItemText primary={`${meal.name} (${meal.calories} kcal)`} />
                                                        </ListItemButton>
                                                    ))}
                                                </List>
                                            )}
                                            {mealPreferences2[mealType] && (
                                                <Button variant="contained" color="secondary" onClick={() => handleMealClear(mealType, 2)}>
                                                    Wyczyść
                                                </Button>
                                            )}
                                        </Box>
                                    </Grid>
                                ))}
                            </Grid>
                        </Box>

                        {/* Zestaw 3 */}
                        <Box sx={{ mb: 3 }}>
                            <Typography variant="h6" gutterBottom>Preferencje posiłków (Zestaw 3):</Typography>
                            <Grid container spacing={2}>
                                {['breakfast', 'secondBreakfast', 'lunch', 'tea', 'dinner'].map((mealType) => (
                                    <Grid item xs={12} sm={6} key={mealType}>
                                        <Box>
                                            <Typography>{mealTranslations[mealType]}</Typography>
                                            <TextField
                                                value={
                                                    mealPreferences3[mealType]
                                                        ? `${mealPreferences3[mealType]} (${filteredMeals(mealType).find(meal => meal.name === mealPreferences3[mealType])?.calories} kcal)`
                                                        : ''
                                                }
                                                onClick={() => setFocusedMeal3(mealType)}
                                                placeholder={`Wybierz ${mealTranslations[mealType]}`}
                                                InputProps={{ readOnly: true }}
                                                fullWidth
                                            />
                                            {countSelectedMeals(mealPreferences3) < 2 && focusedMeal3 === mealType && (
                                                <List sx={{ maxHeight: 200, overflowY: 'auto', border: '1px solid #ddd' }}>
                                                    {filteredMeals(mealType).map((meal) => (
                                                        <ListItemButton key={meal.name} onClick={() => handleMealPreferenceChange(mealType, meal.name, 3)} disabled={Object.values(mealPreferences3).includes(meal.name)}>
                                                            <ListItemText primary={`${meal.name} (${meal.calories} kcal)`} />
                                                        </ListItemButton>
                                                    ))}
                                                </List>
                                            )}
                                            {mealPreferences3[mealType] && (
                                                <Button variant="contained" color="secondary" onClick={() => handleMealClear(mealType, 3)}>
                                                    Wyczyść
                                                </Button>
                                            )}
                                        </Box>
                                    </Grid>
                                ))}
                            </Grid>
                        </Box>

                        <Box sx={{ display: 'flex', justifyContent: 'center', mt: 2 }}>
                            <Button variant="contained" color="primary" type="submit" disabled={loading}>
                                {loading ? <CircularProgress size={24} color="secondary" /> : 'Generuj Dietę'}
                            </Button>
                        </Box>
                    </form>
                </Paper>
            </Box>
        </Box>
    );
}

export default DietPlanForm;
