# README

## Wymagania
- Python 3.10 lub nowszy
- Virtualenv (opcjonalnie, ale zalecane)
- Node.js 16+ (zalecane)
- npm lub yarn

---

## Instalacja

### 1. Klonowanie projektu

Rozpakuj plik ZIP.

---

### 2. Backend (Django)

#### a) Przejdź do folderu GGDiet

```bash
cd GGDiet
```
#### b) Utwórz środowisko wirtualne (opcjonalne, ale zalecane)

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

#### c) Zainstaluj zależności

```bash
pip install -r requirements.txt
```

#### d) Wykonaj migracje bazy danych

```bash
python manage.py migrate
```

#### e) Uruchom serwer backendu

```bash
python manage.py runserver
```

Backend będzie dostępny pod adresem [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

### 3. Frontend (React)

#### a) Przejdź do folderu frontend

```bash
cd frontend
```

#### b) Zainstaluj zależności

```bash
npm install
```

#### c) Uruchom serwer deweloperski frontendu

```bash
npm start
```

Frontend będzie dostępny pod adresem [http://localhost:3000](http://localhost:3000).

---



