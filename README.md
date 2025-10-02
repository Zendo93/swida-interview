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


