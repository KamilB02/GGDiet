import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const Login = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.post('http://localhost:8000/api/token/', {
        username,
        password
      });

      if (response.status === 200) {
        // Zapisz token w localStorage
        localStorage.setItem("username", response.data.username);
        localStorage.setItem('access_token', response.data.access);

        // Przekieruj na stronę formularza
        navigate('/dietplan');
      } else {
        alert('Błąd logowania');
      }
    } catch (error) {
      console.error('Błąd logowania', error);
      alert('Nie udało się zalogować');
    }
  };

  return (
    <div>
      <h2>Login</h2>
      <form onSubmit={handleSubmit}>
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
        <button type="submit">Login</button>
      </form>
      <p>Nie masz konta?</p>
      <button onClick={() => navigate('/register')}>Zarejestruj się</button>
    </div>
  );
};

export default Login;
