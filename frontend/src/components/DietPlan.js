import React, { useEffect, useState } from "react";
import {
    Box,
    Card,
    CardContent,
    Typography,
    Grid,
    List,
    ListItem,
    ListItemText,
    Divider,
} from "@mui/material";

const DietResult = () => {
    const [dietPlans, setDietPlans] = useState([]);

    useEffect(() => {
        const storedDietPlans = localStorage.getItem("dietPlans");
        if (storedDietPlans) {
            setDietPlans(JSON.parse(storedDietPlans)); // Pobierz wszystkie plany
        } else {
            console.error("No diet plans found in Local Storage");
        }
    }, []);

    if (dietPlans.length === 0) {
        return (
            <Box sx={{ p: 3 }}>
                <Typography variant="h5">Brak wygenerowanych diet.</Typography>
            </Box>
        );
    }

    return (
        <Box sx={{ p: 3 }}>
            <Typography variant="h4" gutterBottom>
                Wyniki diety
            </Typography>
            {dietPlans.map((dietPlan, planIndex) => (
                <Box key={planIndex} sx={{ mb: 5 }}>
                    <Typography variant="h5" gutterBottom>
                        Plan diety {planIndex + 1}
                    </Typography>
                    <Grid container spacing={3}>
                        {/* Podsumowanie kalorii */}
                        <Grid item xs={12}>
                            <Card>
                                <CardContent>
                                    <Typography variant="h6" gutterBottom>
                                        Podsumowanie kalorii i makroskładników
                                    </Typography>
                                    <Typography>
                                        <strong>Całkowite kalorie:</strong> {dietPlan.calories_total} kcal
                                    </Typography>
                                    <Typography>
                                        <strong>Białko:</strong> {dietPlan.macros.protein} g
                                    </Typography>
                                    <Typography>
                                        <strong>Węglowodany:</strong> {dietPlan.macros.carbs} g
                                    </Typography>
                                    <Typography>
                                        <strong>Tłuszcze:</strong> {dietPlan.macros.fats} g
                                    </Typography>
                                </CardContent>
                            </Card>
                        </Grid>

                        {/* Szczegóły posiłków */}
                        {["breakfast1", "breakfast2", "lunch", "tea", "dinner"].map(
                            (mealKey, index) => (
                                <Grid item xs={12} sm={6} md={4} key={index}>
                                    <Card>
                                        <CardContent>
                                            <Typography variant="h6" gutterBottom>
                                                {mealKey === "breakfast1"
                                                    ? "Śniadanie 1"
                                                    : mealKey === "breakfast2"
                                                    ? "Śniadanie 2"
                                                    : mealKey === "lunch"
                                                    ? "Obiad"
                                                    : mealKey === "tea"
                                                    ? "Podwieczorek"
                                                    : "Kolacja"}
                                            </Typography>
                                            <List>
                                                {dietPlan[mealKey].map((meal, i) => (
                                                    <Box key={i}>
                                                        <ListItem>
                                                            <ListItemText
                                                                primary={meal.name}
                                                                secondary={`Kalorie: ${meal.calories} kcal`}
                                                            />
                                                        </ListItem>
                                                        <Typography variant="body2" sx={{ ml: 2 }}>
                                                            <strong>Makroskładniki:</strong> Białko:{" "}
                                                            {meal.macros.protein} g, Węglowodany:{" "}
                                                            {meal.macros.carbs} g, Tłuszcze: {meal.macros.fats} g
                                                        </Typography>
                                                        <Typography variant="body2" sx={{ ml: 2, mt: 1 }}>
                                                            <strong>Składniki:</strong> {meal.ingredients.join(", ")}
                                                        </Typography>
                                                        <Divider sx={{ my: 1 }} />
                                                    </Box>
                                                ))}
                                            </List>
                                        </CardContent>
                                    </Card>
                                </Grid>
                            )
                        )}
                    </Grid>
                </Box>
            ))}
        </Box>
    );
};

export default DietResult;
