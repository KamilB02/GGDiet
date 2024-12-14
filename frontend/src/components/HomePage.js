import React, { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { jwtDecode } from 'jwt-decode';

function HomePage() {
  const navigate = useNavigate();

  useEffect(() => {
    const token = localStorage.getItem('access_token');

    if (token) {
      try {
        const decodedToken = jwtDecode(token);
        const currentTime = Date.now() / 1000;

        if (decodedToken.exp < currentTime) {
          localStorage.removeItem('access_token');
          alert('Twoja sesja wygasła. Zaloguj się ponownie.');
          navigate('/login');
        } else {
          navigate('/dietplan');
        }
      } catch (error) {
        console.error('Błąd podczas weryfikacji tokenu:', error);
        localStorage.removeItem('access_token');
        navigate('/login');
      }
    } else {
      navigate('/login');
    }
  }, [navigate]);

  return (
    <div>
      <h1>Witaj na stronie głównej!</h1>
      <p>Jeśli jesteś zalogowany, zostaniesz przekierowany na stronę z planem diety.</p>
    </div>
  );
}

export default HomePage;
