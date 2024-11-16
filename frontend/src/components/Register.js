import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const Register = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const handleRegister = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.post('http://localhost:8000/api/register/', {
        username,
        password
      });

      if (response.status === 201) {
        alert('Rejestracja zakończona sukcesem!');
        navigate('/login'); // Przekierowanie na stronę logowania
      }
        } catch (error) {
      if (error.response) {
        if (error.response.status === 400) {
          // Wyświetl komunikat na podstawie informacji zwróconej przez serwer
          const errorData = error.response.data;
          if (errorData.username) {
            alert(`Błąd: ${errorData.username.join(' ')}`);
          } else {
            alert('Błąd walidacji: Upewnij się, że wszystkie pola są wypełnione poprawnie.');
          }
        } else {
          alert('Wystąpił błąd podczas rejestracji. Spróbuj ponownie.');
        }
      } else {
        console.error('Błąd rejestracji', error);
        alert('Nie udało się zarejestrować');
      }
    }
  };

  return (
    <div>
      <h2>Rejestracja</h2>
      <form onSubmit={handleRegister}>
        <div>
          <label>Username</label>
          <input
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />
        </div>
        <div>
          <label>Password</label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>
        <button type="submit">Zarejestruj się</button>
      </form>
    </div>
  );
};

export default Register;
