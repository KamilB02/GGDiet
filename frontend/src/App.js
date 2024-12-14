import './App.css';
import DietPlanForm from './components/DietPlanForm';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Register from './components/Register';
import Login from './components/Login';
import UserInfo from './components/Userinfo';
import DietPlan from './components/DietPlan';
import HomePage from './components/HomePage';

function App() {
 return (
    <Router>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/dietplan" element={<DietPlanForm />} />
        <Route path="/register" element={<Register />} />
        <Route path="/login" element={<Login />} />
        <Route path="/userinfo" element={<UserInfo />} />
        <Route path="/diet-result" element={<DietPlan />} />
      </Routes>
    </Router>
  );
}

export default App;
