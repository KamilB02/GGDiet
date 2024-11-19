import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import { Box, Button, Typography, TextField, Chip, List, ListItemButton, ListItemText, Grid, Paper } from '@mui/material';
import Navbar from './Navbar'; // Import Navbar

function DietPlanForm() {
    const navigate = useNavigate();
    const [allRecipes, setAllRecipes] = useState([]);
    const [avoidedIngredients, setAvoidedIngredients] = useState([]);
    const [ingredientInput, setIngredientInput] = useState('');
    const [mealPreferences, setMealPreferences] = useState({
        breakfast: '',
        secondBreakfast: '',
        lunch: '',
        tea: '',
        dinner: '',
    });
    const [mealInput, setMealInput] = useState('');
    const [focusedMeal, setFocusedMeal] = useState(null);
    const [username, setUsername] = useState('');

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

    // Lista unikalnych składników
    const allIngredients = Array.from(new Set(allRecipes.flatMap((recipe) => recipe.ingredients)));

    // Lista składników przefiltrowana na podstawie wpisanego tekstu
    const filteredIngredients = allIngredients.filter((ingredient) =>
        ingredient.toLowerCase().includes(ingredientInput.toLowerCase())
    );

    // Lista dań przefiltrowana na podstawie wpisanego tekstu
    const filteredMeals = (mealType) => {
        const meals = allRecipes.filter(
            (recipe) =>
                recipe.meal_type.includes(mealType) ||
                (mealType === 'secondBreakfast' && recipe.meal_type.includes('breakfast')) ||
                (mealType === 'tea' && recipe.meal_type.includes('snack'))
        );
        return meals.filter((recipe) =>
            recipe.name.toLowerCase().includes(mealInput.toLowerCase())
        );
    };

    const handleAddIngredient = (ingredient) => {
        if (ingredient && !avoidedIngredients.includes(ingredient)) {
            setAvoidedIngredients([...avoidedIngredients, ingredient]);
            setIngredientInput(''); // Resetuj input
        }
    };

    const handleIngredientRemove = (ingredientToRemove) => {
        setAvoidedIngredients(avoidedIngredients.filter((ingredient) => ingredient !== ingredientToRemove));
    };

    const handleMealPreferenceChange = (mealType, mealName) => {
        setMealPreferences({ ...mealPreferences, [mealType]: mealName });
        setMealInput(''); // Resetuj input dla posiłku
        setFocusedMeal(null); // Ukryj listę
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        const preferences = {
            avoidedIngredients,
            mealPreferences,
        };

        try {
            const token = localStorage.getItem('access_token');
            const response = await axios.post('http://localhost:8000/api/generate-diet/', preferences, {
                headers: { Authorization: `Bearer ${token}` },
            });

            navigate('/diet-result', { state: { diet: response.data } });
        } catch (error) {
            console.error('Error generating diet:', error);
            alert('Wystąpił błąd podczas generowania diety.');
        }
    };

    return (
        <Box>
            <Navbar username={username} /> {/* Dodanie Navbar */}
            <Box
                sx={{
                    display: 'flex',
                    justifyContent: 'center',
                    alignItems: 'center',
                    minHeight: '100vh',
                    backgroundColor: '#f4f4f9',
                    padding: 3,
                }}
            >
                <Paper elevation={3} sx={{ maxWidth: 600, width: '100%', padding: 4 }}>
                    <Typography variant="h4" align="center" gutterBottom>
                        Planowanie diety
                    </Typography>

                    <form onSubmit={handleSubmit}>
                        <Box sx={{ mb: 3 }}>
                            <Typography variant="h6" gutterBottom>
                                Produkty do unikania:
                            </Typography>
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
                                            <ListItemButton
                                                key={index}
                                                onClick={() => handleAddIngredient(ingredient)}
                                            >
                                                <ListItemText primary={ingredient} />
                                            </ListItemButton>
                                        ))}
                                    </List>
                                )}
                            </Box>
                            <Box sx={{ mt: 2, display: 'flex', flexWrap: 'wrap', gap: 1 }}>
                                {avoidedIngredients.map((ingredient, index) => (
                                    <Chip
                                        key={index}
                                        label={ingredient}
                                        onDelete={() => handleIngredientRemove(ingredient)}
                                    />
                                ))}
                            </Box>
                        </Box>
                        <Box sx={{ mb: 3 }}>
                            <Typography variant="h6" gutterBottom>
                                Preferencje posiłków:
                            </Typography>
                            <Grid container spacing={2}>
                                {['breakfast', 'secondBreakfast', 'lunch', 'tea', 'dinner'].map((mealType) => (
                                    <Grid item xs={12} sm={6} key={mealType}>
                                        <Box>
                                            <TextField
                                                fullWidth
                                                placeholder={`Wybierz ${mealType}`}
                                                value={mealPreferences[mealType]}
                                                onFocus={() => setFocusedMeal(mealType)}
                                                onChange={(e) => setMealInput(e.target.value)}
                                                variant="outlined"
                                            />
                                            {focusedMeal === mealType && mealInput && (
                                                <List sx={{ maxHeight: 200, overflowY: 'auto', border: '1px solid #ddd' }}>
                                                    {filteredMeals(mealType).map((meal) => (
                                                        <ListItemButton
                                                            key={meal.name}
                                                            onClick={() => handleMealPreferenceChange(mealType, meal.name)}
                                                        >
                                                            <ListItemText primary={meal.name} />
                                                        </ListItemButton>
                                                    ))}
                                                </List>
                                            )}
                                        </Box>
                                    </Grid>
                                ))}
                            </Grid>
                        </Box>

                        <Button type="submit" variant="contained" fullWidth>
                            Generuj dietę
                        </Button>
                    </form>
                </Paper>
            </Box>
        </Box>
    );
}

export default DietPlanForm;
