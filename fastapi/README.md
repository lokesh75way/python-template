# FastAPI Training Project

A comprehensive FastAPI project designed for teaching and learning purposes. It covers FastAPI basics, Request/Response handling, Pydantic models, Database integration, and more.

## Prerequisites

- **Python 3.8+**
- **PostgreSQL** (Recommended) or SQLite

## Setup and Installation

1.  **Navigate to the project directory:**
    ```bash
    cd fastapi
    ```

2.  **Create a Virtual Environment:**
    ```bash
    python -m venv venv
    ```

3.  **Activate Virtual Environment:**
    *   **macOS / Linux:**
        ```bash
        source venv/bin/activate
        ```

4.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1.  **Environment Variables:**
    Copy the example environment file to create your own configuration.
    ```bash
    cp .env.example .env
    ```

2.  **Update `.env`:**
    Open the `.env` file and update the variables accordingly:
    *   `DATABASE_URL`: Your database connection string (e.g., `postgresql://user:password@localhost/dbname`).
    *   `SECRET_KEY`: A secret key for security (e.g., for JWT tokens).

## Database Migrations

This project uses **Alembic** for database migrations.

1.  **Apply Migrations:**
    ```bash
    alembic upgrade head
    ```

    *Note: The application also attempts to create tables on startup if they don't exist, using `models.Base.metadata.create_all(bind=engine)` in `app/main.py`.*

## Running the Application

Start the development server using Uvicorn:

```bash
uvicorn app.main:app --reload
```

-   **API Base URL:** `http://127.0.0.1:8000`
-   **Interactive Documentation (Swagger UI):** `http://127.0.0.1:8000/docs`
-   **Alternative Documentation (ReDoc):** `http://127.0.0.1:8000/redoc`

## Project Structure

-   `app/`: Main application source code.
    -   `main.py`: Entry point of the application.
    -   `models/`: SQLAlchemy database models.
    -   `routers/`: API route definitions.
    -   `dependencies.py`: Dependency injection logic.
-   `alembic/`: Database migration scripts.
-   `requirements.txt`: Python dependencies.
