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
            <h2>Wyniki diety</h2>import React, { useState, useEffect } from 'react';
import { useLocation } from 'react-router-dom';

function DietResult() {
  const location = useLocation();
  const { diet_plans = [] } = location.state || {};  // Domyślnie pusta tablica
  const [dietPlans, setDietPlans] = useState([]);

  useEffect(() => {
    console.log('Received diet_plans:', diet_plans);  // Logowanie danych przy odbiorze

    if (diet_plans && diet_plans.length > 0) {
      const transformedDietPlans = diet_plans.map(plan => {
        return {
          id: plan.id,  // Dodanie id do każdego planu
          breakfast1: plan.breakfast1,
          breakfast2: plan.breakfast2,
          lunch: plan.lunch,
          tea: plan.tea,
          dinner: plan.dinner,
          calories_total: plan.calories_total,
          macros: plan.macros
        };
      });
      setDietPlans(transformedDietPlans);
    }
  }, [diet_plans]);

  return (
    <div>
      <h1>Wygenerowane diety</h1>
      {dietPlans.length === 0 ? (
        <p>Nie wygenerowano diet lub dane są niekompletne.</p>
      ) : (
        dietPlans.map((plan, index) => (
          <div key={plan.id}> {/* Użycie unikalnego id jako klucza */}
            <h2>Dieta {index + 1}</h2>
            <h3>Śniadanie 1</h3>
            <ul>
              {plan.breakfast1 && plan.breakfast1.map((meal, i) => (
                <li key={i}>
                  {meal.name} - {meal.calories} kcal
                  <ul>
                    {meal.ingredients && meal.ingredients.map((ingredient, j) => (
                      <li key={j}>{ingredient}</li>
                    ))}
                  </ul>
                </li>
              ))}
            </ul>

            <h3>Śniadanie 2</h3>
            <ul>
              {plan.breakfast2 && plan.breakfast2.map((meal, i) => (
                <li key={i}>
                  {meal.name} - {meal.calories} kcal
                  <ul>
                    {meal.ingredients && meal.ingredients.map((ingredient, j) => (
                      <li key={j}>{ingredient}</li>
                    ))}
                  </ul>
                </li>
              ))}
            </ul>

            <h3>Lunch</h3>
            <ul>
              {plan.lunch && plan.lunch.map((meal, i) => (
                <li key={i}>
                  {meal.name} - {meal.calories} kcal
                  <ul>
                    {meal.ingredients && meal.ingredients.map((ingredient, j) => (
                      <li key={j}>{ingredient}</li>
                    ))}
                  </ul>
                </li>
              ))}
            </ul>

            <h3>Herbata</h3>
            <ul>
              {plan.tea && plan.tea.map((meal, i) => (
                <li key={i}>
                  {meal.name} - {meal.calories} kcal
                  <ul>
                    {meal.ingredients && meal.ingredients.map((ingredient, j) => (
                      <li key={j}>{ingredient}</li>
                    ))}
                  </ul>
                </li>
              ))}
            </ul>

            <h3>Obiad</h3>
            <ul>
              {plan.dinner && plan.dinner.map((meal, i) => (
                <li key={i}>
                  {meal.name} - {meal.calories} kcal
                  <ul>
                    {meal.ingredients && meal.ingredients.map((ingredient, j) => (
                      <li key={j}>{ingredient}</li>
                    ))}
                  </ul>
                </li>
              ))}
            </ul>

            <h3>Podsumowanie</h3>
            <p>Całkowite kalorie: {plan.calories_total} kcal</p>
            <p>Makroskładniki:</p>
            <ul>
              <li>Białko: {plan.macros.protein} g</li>
              <li>Węglowodany: {plan.macros.carbs} g</li>
              <li>Tłuszcze: {plan.macros.fats} g</li>
            </ul>
          </div>
        ))
      )}
    </div>
  );
}

export default DietResult;
