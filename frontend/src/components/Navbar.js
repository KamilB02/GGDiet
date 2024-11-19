import React from 'react';
import { AppBar, Toolbar, Typography, Button, Box } from '@mui/material';
import { useNavigate } from 'react-router-dom';

const Navbar = ({ username }) => {
    const navigate = useNavigate();

    const handleLogout = () => {
        localStorage.removeItem('access_token');
        localStorage.removeItem('username');
        navigate('/login');
    };

    return (
        <AppBar position="sticky" sx={{ mb: 3 }}>
            <Toolbar>
                <Typography variant="h6" sx={{ flexGrow: 1 }}>
                    Witaj, {username || 'Gościu'}!
                </Typography>
                <Box sx={{ display: 'flex', gap: 2 }}>
                    <Button color="inherit" onClick={() => navigate('/dietplan')}>
                        Wygeneruj dietę
                    </Button>
                    <Button color="inherit" onClick={() => navigate('/userinfo')}>
                        Twoje dane
                    </Button>
                    <Button color="inherit" onClick={handleLogout}>
                        Wyloguj
                    </Button>
                </Box>
            </Toolbar>
        </AppBar>
    );
};

export default Navbar;
