import React, { useState } from 'react';
import axios from 'axios';

function DietPlanForm() {
    const [formData, setFormData] = useState({
        weight: '',
        height: '',
        target_weight: '',
        dietary_restrictions: '',
        speed_of_weight_loss: ''
    });

    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value
        });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('http://localhost:8000/api/diet-plan/', formData);
            console.log(response.data.message); // Wyświetli wiadomość na konsoli
            alert(response.data.message); // Możesz wyświetlić wiadomość użytkownikowi
        } catch (error) {
            console.error('Error:', error);
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <div>
                <label>Waga:</label>
                <input type="number" name="weight" value={formData.weight} onChange={handleChange} required />
            </div>
            <div>
                <label>Wzrost:</label>
                <input type="number" name="height" value={formData.height} onChange={handleChange} required />
            </div>
            <div>
                <label>Docelowa waga:</label>
                <input type="number" name="target_weight" value={formData.target_weight} onChange={handleChange} required />
            </div>
            <div>
                <label>Ograniczenia dietetyczne:</label>
                <input type="text" name="dietary_restrictions" value={formData.dietary_restrictions} onChange={handleChange} />
            </div>
            <div>
                <label>Jak szybko chcesz schudnąć?</label>
                <select name="speed_of_weight_loss" value={formData.speed_of_weight_loss} onChange={handleChange} required>
                    <option value="">Wybierz</option>
                    <option value="szybko">Szybko</option>
                    <option value="umiarkowanie">Umiarkowanie</option>
                    <option value="powoli">Powoli</option>
                </select>
            </div>
            <button type="submit">Zatwierdź</button>
        </form>
    );
}

export default DietPlanForm;
