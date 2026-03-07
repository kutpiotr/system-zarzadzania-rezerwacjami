# System Zarządzania Rezerwacjami

Aplikacja webowa umożliwiająca zarządzanie rezerwacjami zasobów takich jak sale konferencyjne lub sprzęt w organizacji.

Projekt powstał jako projekt portfolio pokazujący umiejętności w zakresie:

* tworzenia backendu REST API
* projektowania bazy danych
* implementacji logiki biznesowej
* integracji backendu z frontendem
* testowania API
* dokumentowania systemów informatycznych

---

# Status projektu

Aktualnie zaimplementowano:

* backend REST API
* obsługę użytkowników
* obsługę zasobów
* obsługę rezerwacji
* walidację konfliktów terminów
* frontend połączony z backendem
* formularz dodawania rezerwacji
* automatyczne testy backendu (pytest)

Planowane rozwinięcia projektu:

* role użytkowników (admin / user)
* panel administracyjny
* filtrowanie rezerwacji
* moduł rekomendacji zasobów

---

# Funkcjonalności

System umożliwia:

* tworzenie użytkowników
* zarządzanie zasobami (np. sale, sprzęt)
* tworzenie rezerwacji
* przeglądanie listy rezerwacji
* walidację konfliktów rezerwacji (blokowanie nakładających się terminów)

---

# Reguły biznesowe

System implementuje następujące reguły biznesowe:

* jeden zasób nie może być zarezerwowany w dwóch nakładających się terminach
* data zakończenia rezerwacji musi być późniejsza niż data rozpoczęcia
* jedna rezerwacja należy do jednego użytkownika
* jedna rezerwacja dotyczy jednego zasobu

---

# Architektura systemu

![Architektura systemu](docs/system_architecture.png)

System składa się z trzech głównych komponentów:

* **Frontend** – aplikacja webowa umożliwiająca interakcję użytkownika z systemem
* **Backend API** – logika biznesowa i obsługa żądań
* **Baza danych** – przechowywanie danych użytkowników, zasobów i rezerwacji

Frontend komunikuje się z backendem poprzez REST API, a backend zapisuje dane w bazie PostgreSQL.

---

# Diagram bazy danych

![Diagram ERD](docs/erd.png)

Diagram przedstawia strukturę bazy danych oraz relacje między tabelami:

* users
* resources
* reservations

---

# Zrzuty ekranu

## Interfejs aplikacji

![Frontend](docs/frontend.png)

## Dokumentacja API

![Swagger](docs/swagger.png)

---

# Technologie

## Backend

Backend odpowiada za:

* logikę biznesową
* komunikację z bazą danych
* walidację danych
* obsługę rezerwacji

Wykorzystane technologie:

* Python
* FastAPI
* SQLAlchemy
* PostgreSQL

---

## Frontend

Frontend odpowiada za interfejs użytkownika umożliwiający:

* przeglądanie zasobów
* tworzenie rezerwacji
* przeglądanie listy rezerwacji

Wykorzystane technologie:

* React
* Vite
* Axios

---

# Struktura projektu

```
system-rezerwacji
│
├── backend
│   ├── app
│   │   ├── routers
│   │   ├── models.py
│   │   ├── schemas.py
│   │   ├── crud.py
│   │   ├── database.py
│   │   └── main.py
│   │
│   ├── tests
│   │   ├── conftest.py
│   │   └── test_main.py
│   │
│   └── requirements.txt
│
├── frontend
│
├── docs
│   ├── erd.png
│   ├── system_architecture.png
│   ├── frontend.png
│   └── swagger.png
│
└── README.md
```

---

# Uruchomienie projektu

## Backend

Przejdź do katalogu backend:

```
cd backend
```

Utwórz środowisko wirtualne:

```
python -m venv venv
```

Aktywuj środowisko:

Windows CMD:

```
venv\Scripts\activate
```

Windows PowerShell:

```
venv\Scripts\Activate.ps1
```

Zainstaluj zależności:

```
pip install -r requirements.txt
```

Uruchom serwer:

```
uvicorn app.main:app --reload
```

API będzie dostępne pod adresem:

```
http://127.0.0.1:8000
```

Dokumentacja API:

```
http://127.0.0.1:8000/docs
```

---

## Frontend

Przejdź do katalogu frontend:

```
cd frontend
```

Zainstaluj zależności:

```
npm install
```

Uruchom aplikację:

```
npm run dev
```

Frontend będzie dostępny pod adresem:

```
http://localhost:5173
```

---

# Testy

Backend zawiera automatyczne testy API napisane przy użyciu **pytest**.

Testy obejmują:

* endpoint główny API
* tworzenie użytkownika
* tworzenie zasobu
* tworzenie rezerwacji
* walidację konfliktu rezerwacji

Uruchomienie testów:

```
cd backend
pytest
```

---

# Przykładowe endpointy API

## Dodanie użytkownika

```
POST /users/
```

```
{
"name": "Jan",
"email": "jan@example.com"
}
```

---

## Dodanie zasobu

```
POST /resources/
```

```
{
"name": "Sala A101",
"type": "sala"
}
```

---

## Dodanie rezerwacji

```
POST /reservations/
```

```
{
"start_time": "2026-03-08T10:00:00",
"end_time": "2026-03-08T12:00:00",
"user_id": 1,
"resource_id": 1
}
```

---

# Autor

**Piotr Kut**
Student kierunku Inżynieria i Analiza Danych.

GitHub: https://github.com/kutpiotr
