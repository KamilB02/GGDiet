import logo from './logo.svg';
import './App.css';
import DietPlanForm from './components/DietPlanForm';

function App() {
  return (
    <div className="App">
      <h1>Plan dietetyczny</h1>
      <DietPlanForm />  {/* Używamy formularza */}
    </div>
  );
}

export default App;
