import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import { Box, TextField, Button, Typography, Link, Paper } from '@mui/material';

const Login = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.post('http://localhost:8000/api/token/', {
        username,
        password,
      });

      if (response.status === 200) {
        localStorage.setItem('username', response.data.username);
        localStorage.setItem('access_token', response.data.access);
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
        <Typography variant="h4" gutterBottom align="center">
          Logowanie
        </Typography>
        <form onSubmit={handleSubmit}>
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
          <Button
            type="submit"
            variant="contained"
            fullWidth
            sx={{ mt: 2 }}
          >
            Zaloguj się
          </Button>
        </form>
        <Typography align="center" sx={{ mt: 2 }}>
          Nie masz konta?{' '}
          <Link onClick={() => navigate('/register')} sx={{ cursor: 'pointer' }}>
            Zarejestruj się
          </Link>
        </Typography>
      </Paper>
    </Box>
  );
};

export default Login;
