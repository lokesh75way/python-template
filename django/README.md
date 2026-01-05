# Django Training Project

This is a Django project template designed for training purposes, covering Django basics, ORM, REST Framework, and more.

## Prerequisites

- **Python 3.8+**
- **pip**

## Setup and Installation

1.  **Navigate to the project directory:**
    ```bash
    cd django
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

4.  **Configuration (Environment Variables):**
    Navigate to the inner project directory where `manage.py` is located.
    ```bash
    cd template
    ```
    Copy the example environment file to create your own configuration.
    ```bash
    cp .env.example .env
    ```
    Open the `.env` file and update the database credentials if necessary:
    *   `DB_NAME`: Database name (default: `django`)
    *   `DB_USER`: Database user (default: `postgres`)
    *   `DB_PASSWORD`: Database password (default: `postgres`)
    *   `DB_HOST`: Database host (default: `localhost`)
    *   `DB_PORT`: Database port (default: `5432`)

5.  **Database Migrations:**
    Ensure you are in the `template` directory.
    ```bash
    python manage.py migrate
    ```

6.  **Create Superuser (Optional):**
    To access the Django Admin panel.
    ```bash
    python manage.py createsuperuser
    ```

## Running the Application

To start the development server, run the following command from the `template` directory:

```bash
python manage.py runserver
```

The server will start at `http://127.0.0.1:8000/`.

## Project Structure

-   `requirements.txt`: Python dependencies.
-   `template/`: Main project directory containing `manage.py`.
    -   `manage.py`: Django's command-line utility.
    -   `template/`: Project configuration settings.
    -   `mainapp/`: Main application logic.
