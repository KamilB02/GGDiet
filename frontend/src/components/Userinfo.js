import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const UserInfoForm = () => {
    const [formData, setFormData] = useState({
        weight: '',
        height: '',
        age: '',
        gender: '',
        physical_activity_at_work: '',
        physical_activity_in_free_time: '',
        objective: '',
    });
    const navigate = useNavigate();

    useEffect(() => {
        // Pobranie danych użytkownika przy załadowaniu komponentu
        const fetchUserInfo = async () => {
            const token = localStorage.getItem('access_token');
            try {
                const response = await axios.get('http://localhost:8000/api/user-info/', {
                    headers: {
                        Authorization: `Bearer ${token}`, // Token w nagłówku
                    },
                });
                setFormData(response.data); // Ustawienie danych w formularzu
            } catch (error) {
                console.error('Błąd podczas pobierania danych użytkownika:', error);
            }
        };
        fetchUserInfo();
    }, []);

    // Obsługa zmian w formularzu
    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData((prevState) => ({
            ...prevState,
            [name]: value,
        }));
    };

    // Obsługa wysyłania formularza
    const handleSubmit = async (e) => {
        e.preventDefault();

        const token = localStorage.getItem('access_token');
        try {
            const response = await axios.post('http://localhost:8000/api/user-info/', formData, {
                headers: {
                    Authorization: `Bearer ${token}`, // Token w nagłówkach
                },
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
                    <label>Waga (kg):</label>
                    <input
                        type="number"
                        name="weight"
                        value={formData.weight}
                        onChange={handleChange}
                        required
                    />
                </div>
                <div>
                    <label>Wzrost (cm):</label>
                    <input
                        type="number"
                        name="height"
                        value={formData.height}
                        onChange={handleChange}
                        required
                    />
                </div>
                <div>
                    <label>Wiek:</label>
                    <input
                        type="number"
                        name="age"
                        value={formData.age}
                        onChange={handleChange}
                        required
                    />
                </div>
                <div>
                    <label>Płeć:</label>
                    <select
                        name="gender"
                        value={formData.gender}
                        onChange={handleChange}
                        required
                    >
                        <option value="">-- Wybierz płeć --</option>
                        <option value="man">Mężczyzna</option>
                        <option value="woman">Kobieta</option>
                    </select>
                </div>
                <div>
                    <label>Aktywność fizyczna w pracy:</label>
                    <select
                        name="physical_activity_at_work"
                        value={formData.physical_activity_at_work}
                        onChange={handleChange}
                        required
                    >
                        <option value="">-- Wybierz poziom --</option>
                        <option value="1">Niska</option>
                        <option value="2">Umiarkowana</option>
                        <option value="3">Wysoka</option>
                        <option value="4">Bardzo wysoka</option>
                    </select>
                </div>
                <div>
                    <label>Aktywność fizyczna w czasie wolnym:</label>
                    <select
                        name="physical_activity_in_free_time"
                        value={formData.physical_activity_in_free_time}
                        onChange={handleChange}
                        required
                    >
                        <option value="">-- Wybierz poziom --</option>
                        <option value="1">Niska</option>
                        <option value="2">Umiarkowana</option>
                        <option value="3">Aktywna</option>
                        <option value="4">Bardzo aktywna</option>
                        <option value="5">Ekstremalna</option>
                    </select>
                </div>
                <div>
                    <label>Cel:</label>
                    <select
                        name="objective"
                        value={formData.objective}
                        onChange={handleChange}
                        required
                    >
                        <option value="">-- Wybierz cel --</option>
                        <option value="less">Schudnąć</option>
                        <option value="same">Utrzymać wagę</option>
                        <option value="more">Przybrać na wadze</option>
                    </select>
                </div>
                <button type="submit">Zatwierdź</button>
            </form>
        </div>
    );
};

export default UserInfoForm;
