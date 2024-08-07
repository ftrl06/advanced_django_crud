# Advanced Django CRUD Interface

This project is an advanced Django application with PostgreSQL database integration. It allows performing CRUD (Create, Read, Update, Delete) operations with a user-friendly interface.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/ftrl06/advanced_django_crud.git
    ```

2. Navigate to the project directory:
    ```bash
    cd advanced_django_crud
    ```

3. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

5. Configure the PostgreSQL database in `myproject/settings.py`.

6. Apply the migrations:
    ```bash
    python manage.py migrate
    ```

7. Run the server:
    ```bash
    python manage.py runserver
    ```

8. Open your browser and navigate to `http://127.0.0.1:8000/`.

## Testing

Run the tests:
```bash
python manage.py test


##project structure

advanced_django_crud/
├── myproject/
│   ├── myproject/
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── asgi.py
│   ├── myapp/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── templates/
│   │   │   └── myapp/
│   │   │       ├── index.html
│   │   │       ├── add_record.html
│   │   │       ├── update_record.html
│   │   │       └── delete_record.html
│   │   ├── static/
│   │   │   └── myapp/
│   │   │       └── styles.css
│   │   ├── forms.py
│   │   ├── migrations/
│   │   │   └── __init__.py
│   ├── manage.py
├── .gitignore
├── README.md
└── requirements.txt
