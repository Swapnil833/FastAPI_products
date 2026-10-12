# React + FastAPI CRUD Application

A full-stack web application built using React.js and FastAPI that supports basic CRUD (Create, Read, Update, Delete) operations, with search functionality and dependency injection for structured backend development.

## 🚀 Features

- **Create Records:** Add new records through the React frontend.
- **Read Records:** Retrieve and display stored records.
- **Update Records:** Modify existing records.
- **Delete Records:** Remove records when no longer needed.
- **Search Functionality:** Search and filter records efficiently.
- **Dependency Injection:** Use FastAPI's dependency injection system to improve code modularity, reusability, and maintainability.
- **REST API Integration:** Connect the React frontend with the FastAPI backend through HTTP requests.

## 🛠️ Tech Stack

- **Frontend:** React.js
- **Backend:** FastAPI
- **Language:** JavaScript, Python
- **API:** REST API
- **Server:** Uvicorn

## ⚙️ Installation and Setup

### Prerequisites

- Python 3.10+
- Node.js and npm
- Git

### 1. Clone the Repository

```bash
git clone https://github.com/Swapnil833/FastAPI_products
cd FastAPI_products
```

### 2. Set Up the Backend

Create and activate a virtual environment.

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

Install the dependencies:

```bash
pip install fastapi uvicorn
```

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

The backend will run at `http://127.0.0.1:8000`.

Access the interactive API documentation at:

`http://127.0.0.1:8000/docs`

### 3. Set Up the Frontend

Open a new terminal and navigate to the frontend directory:

```bash
cd frontend
npm install
npm start
```

The frontend will run at the local development URL displayed in the terminal.

## 🔌 API Functionality

The backend exposes endpoints for performing CRUD operations and searching records.

| Operation | HTTP Method | Purpose |
|---|---|---|
| Create | POST | Add a new record |
| Read | GET | Retrieve records |
| Update | PUT/PATCH | Update an existing record |
| Delete | DELETE | Delete a record |
| Search | GET | Find records using a search query |

*Endpoint paths and HTTP methods may vary depending on your implementation.*


## 📌 Future Improvements

- Integrate a database such as PostgreSQL or MongoDB.
- Add authentication and authorization.
- Implement input validation and improved error handling.
- Add pagination and advanced filtering.
- Deploy the frontend and backend to production.
