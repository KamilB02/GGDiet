import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import { Box, TextField, Button, Typography, MenuItem, Grid, Paper } from '@mui/material';
import Navbar from './Navbar'; // Import Navbar

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
    const [username, setUsername] = useState('');
    const navigate = useNavigate();

    useEffect(() => {
        const token = localStorage.getItem('access_token');
        const storedUsername = localStorage.getItem('username');

        if (!token) {
            navigate('/login');
        } else {
            setUsername(storedUsername);
        }
    }, [navigate]);

    useEffect(() => {
        const fetchUserInfo = async () => {
            const token = localStorage.getItem('access_token');
            try {
                const response = await axios.get('http://localhost:8000/api/user-info/', {
                    headers: {
                        Authorization: `Bearer ${token}`,
                    },
                });
                setFormData(response.data); // Ustawienie danych w formularzu
            } catch (error) {
                console.error('Błąd podczas pobierania danych użytkownika:', error);
            }
        };
        fetchUserInfo();
    }, []);

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData((prevState) => ({
            ...prevState,
            [name]: value,
        }));
    };

    const handleSubmit = async (e) => {
        e.preventDefault();

        const token = localStorage.getItem('access_token');
        try {
            const response = await axios.post('http://localhost:8000/api/user-info/', formData, {
                headers: {
                    Authorization: `Bearer ${token}`,
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
        <Box>
            <Navbar username={username} /> {/* Dodanie Navbar */}
            <Box
                sx={{
                    display: 'flex',
                    justifyContent: 'center',
                    alignItems: 'center',
                    minHeight: '100vh',
                    backgroundColor: '#f4f4f9',
                    padding: 3,
                }}
            >
                <Paper elevation={3} sx={{ maxWidth: 600, width: '100%', padding: 4 }}>
                    <Typography variant="h4" align="center" gutterBottom>
                        Informacje o użytkowniku
                    </Typography>
                    <form onSubmit={handleSubmit}>
                        <Grid container spacing={3}>
                            <Grid item xs={12}>
                                <TextField
                                    label="Waga (kg)"
                                    type="number"
                                    name="weight"
                                    value={formData.weight}
                                    onChange={handleChange}
                                    fullWidth
                                    required
                                />
                            </Grid>
                            <Grid item xs={12}>
                                <TextField
                                    label="Wzrost (cm)"
                                    type="number"
                                    name="height"
                                    value={formData.height}
                                    onChange={handleChange}
                                    fullWidth
                                    required
                                />
                            </Grid>
                            <Grid item xs={12}>
                                <TextField
                                    label="Wiek"
                                    type="number"
                                    name="age"
                                    value={formData.age}
                                    onChange={handleChange}
                                    fullWidth
                                    required
                                />
                            </Grid>
                            <Grid item xs={12}>
                                <TextField
                                    label="Płeć"
                                    select
                                    name="gender"
                                    value={formData.gender}
                                    onChange={handleChange}
                                    fullWidth
                                    required
                                >
                                    <MenuItem value="man">Mężczyzna</MenuItem>
                                    <MenuItem value="woman">Kobieta</MenuItem>
                                </TextField>
                            </Grid>
                            <Grid item xs={12}>
                                <TextField
                                    label="Aktywność fizyczna w pracy"
                                    select
                                    name="physical_activity_at_work"
                                    value={formData.physical_activity_at_work}
                                    onChange={handleChange}
                                    fullWidth
                                    required
                                >
                                    <MenuItem value="1">Niska - Praca siedząca</MenuItem>
                                    <MenuItem value="2">Umiarkowana - Lekka praca (np. dostawca)</MenuItem>
                                    <MenuItem value="3">Wysoka - Praca fizyczna</MenuItem>
                                    <MenuItem value="4">Bardzo wysoka - Regularna ciężka praca fizyczna</MenuItem>
                                </TextField>
                            </Grid>
                            <Grid item xs={12}>
                                <TextField
                                    label="Aktywność fizyczna w czasie wolnym"
                                    select
                                    name="physical_activity_in_free_time"
                                    value={formData.physical_activity_in_free_time}
                                    onChange={handleChange}
                                    fullWidth
                                    required
                                >
                                    <MenuItem value="1">Brak dodatkowej aktywności fizycznej</MenuItem>
                                    <MenuItem value="2">Ćwiczenia raz w tygodniu</MenuItem>
                                    <MenuItem value="3">Ćwiczenia dwa/trzy razy tygodniu</MenuItem>
                                    <MenuItem value="4">Ciężkie treningi dwa/trzy razy tygodniu</MenuItem>
                                    <MenuItem value="5">Ciężkie treningi conajmniej cztery razy w tygodniu</MenuItem>
                                </TextField>
                            </Grid>
                            <Grid item xs={12}>
                                <TextField
                                    label="Cel"
                                    select
                                    name="objective"
                                    value={formData.objective}
                                    onChange={handleChange}
                                    fullWidth
                                    required
                                >
                                    <MenuItem value="less">Schudnąć</MenuItem>
                                    <MenuItem value="same">Utrzymać wagę</MenuItem>
                                    <MenuItem value="more">Przybrać na wadze</MenuItem>
                                </TextField>
                            </Grid>
                            <Grid item xs={12}>
                                <Button type="submit" variant="contained" color="primary" fullWidth>
                                    Zatwierdź
                                </Button>
                            </Grid>
                        </Grid>
                    </form>
                </Paper>
            </Box>
        </Box>
    );
};

export default UserInfoForm;
