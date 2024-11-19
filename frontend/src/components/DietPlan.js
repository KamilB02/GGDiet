import { useLocation } from 'react-router-dom';

function DietResult() {
    const location = useLocation();
    const { diet } = location.state || {}; // Pobieramy dane diety

    console.log('Received diet:', diet); // Debugowanie danych

    // Mapowanie posiłków na przyjazne nazwy
    const mealNames = {
        breakfast1: 'Pierwsze Śniadanie',
        breakfast2: 'Drugie Śniadanie',
        lunch: 'Obiad',
        tea: 'Podwieczorek',
        dinner: 'Kolacja'
    };

    // Sprawdzamy, czy dane diety są kompletne
    if (!diet || !diet.breakfast1 || !diet.breakfast2 || !diet.lunch || !diet.tea || !diet.dinner) {
        return <div>Nie wygenerowano diety lub dane są niekompletne</div>;
    }

    return (
        <div>
            <h2>Wyniki diety</h2>
            <div>Całkowite kalorie: {diet.calories_total}</div>
            <div>Makroskładniki: Białko: {diet.macros.protein}, Węglowodany: {diet.macros.carbs}, Tłuszcze: {diet.macros.fats}</div>

            <h3>Posiłki:</h3>
            {['breakfast1', 'breakfast2', 'lunch', 'tea', 'dinner'].map((mealType) => (
                <div key={mealType}>
                    <h4>{mealNames[mealType]}</h4> {/* Używamy mapowania nazw posiłków */}
                    {diet[mealType] && diet[mealType].length > 0 ? ( // Sprawdzamy, czy posiłek istnieje i ma jakieś przepisy
                        diet[mealType].map((meal, index) => (
                            <div key={index}>
                                <p>{meal.name}</p>
                                <p>Kalorie: {meal.calories}</p>
                                <p>Składniki: {meal.ingredients.join(', ')}</p>
                            </div>
                        ))
                    ) : (
                        <p>Brak przepisów dla tego posiłku.</p> // Jeśli brak przepisów, wyświetlamy komunikat
                    )}
                </div>
            ))}
        </div>
    );
}

export default DietResult;
