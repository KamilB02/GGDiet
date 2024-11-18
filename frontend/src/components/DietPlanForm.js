import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

function DietPlanForm() {
    const navigate = useNavigate();
    const [allRecipes, setAllRecipes] = useState([]);
    const [avoidedIngredients, setAvoidedIngredients] = useState([]);
    const [ingredientInput, setIngredientInput] = useState(''); // Nowy stan dla wpisywanego składnika
    const [mealPreferences, setMealPreferences] = useState({
        breakfast: '',
        secondBreakfast: '',
        lunch: '',
        tea: '',
        dinner: ''
    });
    const [username, setUsername] = useState('');

    // Sprawdź, czy użytkownik jest zalogowany
    useEffect(() => {
        const token = localStorage.getItem('access_token');
        const storedUsername = localStorage.getItem('username');

        if (!token) {
            navigate('/login'); // Przekieruj na stronę logowania, jeśli brak tokena
        } else {
            setUsername(storedUsername); // Ustaw nazwę użytkownika
        }
    }, [navigate]);

    // Pobieranie przepisów
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

    // Obsługa dodawania składnika do listy
    const handleAddIngredient = () => {
        const trimmedIngredient = ingredientInput.trim();
        if (trimmedIngredient && !avoidedIngredients.includes(trimmedIngredient)) {
            setAvoidedIngredients([...avoidedIngredients, trimmedIngredient]);
            setIngredientInput(''); // Wyczyść pole input
        }
    };

    // Obsługa usuwania składnika z listy
    const handleIngredientRemove = (ingredientToRemove) => {
        setAvoidedIngredients(
            avoidedIngredients.filter((ingredient) => ingredient !== ingredientToRemove)
        );
    };

    const handleMealPreferenceChange = (e) => {
        const { name, value } = e.target;
        setMealPreferences({ ...mealPreferences, [name]: value });
    };

const handleSubmit = async (e) => {
    e.preventDefault();
    const preferences = {
        avoidedIngredients,
        mealPreferences
    };

    try {
        const token = localStorage.getItem('access_token');
        const response = await axios.post('http://localhost:8000/api/generate-diet/', preferences, {
            headers: { Authorization: `Bearer ${token}` }
        });

        console.log('Diet generated:', response.data); // Sprawdzanie odpowiedzi
        navigate('/diet-result', { state: { diet: response.data } });
    } catch (error) {
        console.error('Error generating diet:', error);
        alert('Wystąpił błąd podczas generowania diety.');
    }
};


    // Generowanie listy składników i nazw potraw na podstawie `all_recipes`
    const allIngredients = Array.from(
        new Set(allRecipes.flatMap((recipe) => recipe.ingredients))
    );

const mealsByType = (type) => {
    if (type === 'secondBreakfast' || type === 'tea') {
        // Uwzględnij przepisy z kategorii 'breakfast' dla 'secondBreakfast' i 'snack'
        return allRecipes.filter(
            (recipe) => recipe.meal_type.includes(type) || recipe.meal_type.includes('breakfast')
        );
    }
    // Standardowe filtrowanie dla pozostałych typów
    return allRecipes.filter((recipe) => recipe.meal_type.includes(type));
};

    return (
        <div>
            <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                {username && <span>Cześć, {username}!</span>} {/* Powitanie z nazwą użytkownika */}
                <button onClick={() => {
                    localStorage.removeItem('access_token');
                    localStorage.removeItem('username');
                    navigate('/login');
                }}>Wyloguj</button> {/* Przycisk wylogowania */}
            </div>
            <form onSubmit={handleSubmit}>
                <div>
                    <label>Produkty do unikania:</label>
                    <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                        <input
                            list="ingredients-list"
                            placeholder="Wyszukaj lub wpisz produkt"
                            value={ingredientInput}
                            onChange={(e) => setIngredientInput(e.target.value)}
                        />
                        <datalist id="ingredients-list">
                            {allIngredients.map((ingredient, index) => (
                                <option key={index} value={ingredient} />
                            ))}
                        </datalist>
                        <button type="button" onClick={handleAddIngredient}>
                            Dodaj
                        </button>
                    </div>
                    <div>
                        Wybrane składniki:
                        <ul>
                            {avoidedIngredients.map((ingredient, index) => (
                                <li key={index}>
                                    {ingredient}{' '}
                                    <button
                                        type="button"
                                        onClick={() => handleIngredientRemove(ingredient)}
                                    >
                                        Usuń
                                    </button>
                                </li>
                            ))}
                        </ul>
                    </div>
                </div>

                    {['breakfast', 'secondBreakfast', 'lunch', 'tea', 'dinner'].map(
                        (meal) => (
                            <div key={meal}>
                                <label>{meal}:</label>
                                <select
                                    name={meal}
                                    value={mealPreferences[meal]}
                                    onChange={handleMealPreferenceChange}
                                >
                                    <option value="">-- Wybierz danie --</option>
                                    {mealsByType(meal).map((recipe) => (
                                        <option key={recipe.name} value={recipe.name}>
                                            {recipe.name}
                                        </option>
                                    ))}
                                </select>
                            </div>
                        )
                    )}

                <button type="submit">Generuj dietę</button>
            </form>
          <button onClick={() => navigate('/userinfo')}>Uzupełnij dane</button>
        </div>
    );
}

export default DietPlanForm;
