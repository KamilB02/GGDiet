import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';



const UserInfoForm = () => {
    const [formData, setFormData] = useState({
        weight: '',
        height: '',
    });
    const navigate = useNavigate();

    // Obsługa zmian w formularzu
    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData(prevState => ({
            ...prevState,
            [name]: value
        }));
    };

    // Obsługa wysyłania formularza
    const handleSubmit = async (e) => {
        e.preventDefault();

        const token = localStorage.getItem('access_token');
        try {
            const response = await axios.post('http://localhost:8000/api/user-info/', formData, {
                headers: {
                    'Authorization': `Bearer ${token}`  // Wysyłanie tokenu w nagłówkach
                }
            });
            console.log(response.data);
            alert('Informacje zostały zapisane!');
            navigate('/dietplan');
        } catch (error) {
            console.error('Błąd:', error);
            alert('Wystąpił problem z zapisaniem danych!');
        }
    };

    return (
        <div>
            <h2>Informacje o użytkowniku</h2>
            <form onSubmit={handleSubmit}>
                <div>
                    <label>Waga:</label>
                    <input
                        type="number"
                        name="weight"
                        value={formData.weight}
                        onChange={handleChange}
                        required
                    />
                </div>
                <div>
                    <label>Wzrost:</label>
                    <input
                        type="number"
                        name="height"
                        value={formData.height}
                        onChange={handleChange}
                        required
                    />
                </div>
                <button type="submit">Zatwierdź</button>
                <button onClick={() => navigate('/dietplan')}>Anuluj</button>
            </form>
        </div>
    );
};

export default UserInfoForm;
