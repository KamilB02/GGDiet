import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import { Box, TextField, Button, Typography, Paper } from '@mui/material';

const Register = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const navigate = useNavigate();

  const handleRegister = async (e) => {
    e.preventDefault();

    if (password !== confirmPassword) {
      alert('Hasła nie są zgodne. Spróbuj ponownie.');
      return;
    }

    try {
      const response = await axios.post('http://localhost:8000/api/register/', {
        username,
        password,
      });

      if (response.status === 201) {
        alert('Rejestracja zakończona sukcesem!');
        navigate('/login');
      }
    } catch (error) {
      if (error.response) {
        if (error.response.status === 400) {
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
    <Box
      sx={{
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        minHeight: '100vh',
        backgroundColor: '#f4f4f9',
      }}
    >
      <Paper elevation={3} sx={{ padding: 4, maxWidth: 400, width: '100%' }}>
        <Typography variant="h4" align="center" gutterBottom>
          Rejestracja
        </Typography>
        <form onSubmit={handleRegister}>
          <TextField
            label="Nazwa użytkownika"
            fullWidth
            margin="normal"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />
          <TextField
            label="Hasło"
            type="password"
            fullWidth
            margin="normal"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
          <TextField
            label="Potwierdź hasło"
            type="password"
            fullWidth
            margin="normal"
            value={confirmPassword}
            onChange={(e) => setConfirmPassword(e.target.value)}
            required
          />
          <Button
            type="submit"
            variant="contained"
            fullWidth
            sx={{ mt: 2 }}
          >
            Zarejestruj się
          </Button>
        </form>
        <Typography align="center" sx={{ mt: 2 }}>
          Masz już konto?{' '}
          <Button
            variant="text"
            onClick={() => navigate('/login')}
            sx={{ textTransform: 'none', padding: 0 }}
          >
            Zaloguj się
          </Button>
        </Typography>
      </Paper>
    </Box>
  );
};

export default Register;
