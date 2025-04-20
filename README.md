
# 🔖 Bookmarker API

A fully-featured, production-ready RESTful API built using **Flask** to manage and track web bookmarks. The API includes authentication, CRUD functionality, token management, link tracking, Swagger documentation, and deployment on **Vercel**.

---

## 📌 Key Features

- �� JWT Authentication (Access & Refresh Tokens)
- ✅ User Registration & Login
- 📚 Bookmark Creation, Retrieval, Update, and Deletion
- 📊 Link Click Tracking & Stats
- 📃 Pagination for Bookmark Lists
- ⚠️ Custom Error Handling
- 📄 Auto-generated Swagger API Docs
- 🚀 Vercel Deployment Ready

---

## 📂 Project Structure

```
bookmarker-api/
├── app/
│   ├── __init__.py
│   ├── auth/
│   ├── bookmarks/
│   ├── models/
│   ├── utils/
│   └── config.py
├── migrations/
├── requirements.txt
├── .flaskenv
├── Procfile
├── README.md
└── app.py
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/tevinsmark/bookmarker-api.git
cd bookmarker-api
```

### 2. Set Up the Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Environment Variables

Create a `.env` file and add:

```env
FLASK_APP=app
FLASK_ENV=development
SECRET_KEY=your_secret_key
JWT_SECRET_KEY=your_jwt_secret
DATABASE_URL=your_postgres_url
```

### 4. Migrate the Database

```bash
flask db init
flask db migrate
flask db upgrade
```

### 5. Start the Server

```bash
flask run
```

---

## 🔐 Authentication Flow

| Method | Endpoint      | Purpose              |
|--------|---------------|----------------------|
| POST   | /register     | Create user account  |
| POST   | /login        | Obtain tokens        |
| POST   | /token/refresh| Get new access token |

---

## 📘 Bookmarks API

| Method | Endpoint             | Function                  |
|--------|----------------------|---------------------------|
| GET    | /bookmarks           | List bookmarks (paginated)|
| POST   | /bookmarks           | Add new bookmark          |
| GET    | /bookmarks/:id       | Get single bookmark       |
| PUT    | /bookmarks/:id       | Update a bookmark         |
| DELETE | /bookmarks/:id       | Delete a bookmark         |
| GET    | /statistics          | View link tracking stats  |

---

## 🧪 Swagger API Docs

Access interactive documentation at:

```
/apidocs
```

## 🔧 Tech Stack

- Python 3.11+
- Flask
- Flask-JWT-Extended
- SQLAlchemy + Alembic
- PostgreSQL
- Flasgger (Swagger Docs)
- Vercel (Deployment)

---

## 📦 Deployment (Vercel)

Install Vercel CLI and run:

```bash
npm i -g vercel
vercel
```

> 🔗 Live URL: _coming soon_

---

## 🙋‍♂️ Author

**Tevin Mark Simiyu**  
📧 tevinsmark@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/mark-tevin/)  
🔗 [GitHub](https://github.com/tevinsmark)

---

## 🏁 License

This project is open-source under the MIT License.
```
---
