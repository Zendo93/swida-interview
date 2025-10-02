# Backend  Django REST API framework
## 🚀 Features

- Serving delivery orders on GET /api/orders/
- Creating delivery orders on POST /api/orders/
- Django REST API
- Easily connectable to frontend frameworks like Vue or React

---

## 📦 Tech Stack

- Python 3.x
- Django 4.x
- Django REST Framework
- [Optional] django-cors-headers
- [Optional] PostgreSQL

## ⚙️ Assumptions and Decisions

- Backend-only (no templates or frontend rendering)

- CORS enabled for connecting with frontend

- Uses SQLite (replaceable with PostgreSQL or others)

- No authentication yet (future support: JWT/Token/Auth)

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```
### 2. Move to transport_api folder

```bash
cd transport_api
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Database & Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the App

```bash
python manage.py runserver
```
Access the app at: http://localhost:8000

Access the API documentation at:
http://localhost:8000/api/docs/swagger/
http://localhost:8000/api/docs/redoc/


# Frontend  Vue 3 + TypeScript
## 🚀 Features

- Serving delivery orders on GET /api/orders/
- Creating delivery orders on POST /api/orders/
- Django REST API
- Easily connectable to frontend frameworks like Vue or React

---

## 📦 Tech Stack

- Vue 3
- Composition API
- TypeScript
- Axios

## ⚙️ Assumptions and Decisions

- RESTful API: /api/orders/ supports both GET and POST

- Django CORS support: Uses django-cors-headers to allow frontend requests

- Trailing slash in API URLs is required (Django default)

- CSRF is not used for API authentication — assumed to be a public or dev-only API

- Frontend uses Axios for all HTTP requests, with proper camelCase mapping

- Waypoints are managed dynamically and included as nested objects on POST

## 🛠️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```
### 2. Instal Prerequisites

```bash
Node v22.20.2 with npm package manager
```

### 3. Install Dependencies

```bash
npm install
```

### 4. Run the App

```bash
npm run dev
```
Access the app at: http://localhost:5173
