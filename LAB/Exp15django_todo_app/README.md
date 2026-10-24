# Experiment 15: Django To-Do Application

## 1. Aim

To develop a To-Do List web application using Django that allows users to create, view, update, and delete tasks. The experiment also demonstrates Django template inheritance, template inclusion, and static file management.

## 2. Introduction

Django is a high-level Python web framework used to develop secure and maintainable web applications. It follows the Model-View-Template (MVT) architectural pattern.

This project implements a simple To-Do List application in which users can add tasks, view existing tasks, mark tasks as completed or incomplete, and delete tasks.

The application uses Django for backend functionality, HTML for webpage structure, CSS for styling, and SQLite for data storage.

## 3. Objectives

- Understand Django project and application structure.
- Create and configure a Django application.
- Define database models using Django ORM.
- Perform CRUD (Create, Read, Update, Delete) operations.
- Configure URL routing and views.
- Use Django templates to display dynamic data.
- Implement template inheritance using `extends`.
- Reuse common components using `include`.
- Serve CSS files using Django's static file system.
- Store task information in an SQLite database.

## 4. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming language |
| Django | Web application framework |
| HTML | Structure of web pages |
| CSS | Styling and layout |
| SQLite | Database for storing tasks |
| VS Code | Code editor |
| Django Template Language | Dynamic content rendering and template reuse |

## 5. Project Structure

```text
Exp15django_todo_app/
│
├── manage.py
├── db.sqlite3
│
├── todo_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
└── todo/
    ├── migrations/
    ├── static/
    │   └── todo/
    │       └── style.css
    │
    ├── templates/
    │   └── todo/
    │       ├── base.html
    │       ├── header.html
    │       ├── footer.html
    │       ├── task_list.html
    │       └── add_task.html
    │
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── urls.py
    ├── views.py
    └── tests.py
```

*Note: The `venv` virtual environment folder is not shown above. The SQLite database file is created after database migrations are applied.*

## 6. Implementation Details

### A. Django Project and Application

The Django project is named `todo_project`, and the application is named `todo`.

The project configuration is maintained in `settings.py`, while application-specific functionality is implemented inside the `todo` directory.

### B. Database Model

The `Task` model is defined in `models.py`.

It contains the following fields:

- `title`: Stores the task description.
- `completed`: Stores whether the task is completed. Its default value is `False`.
- `created_at`: Stores the date and time when the task is created.

Django ORM is used to interact with the SQLite database.

### C. Views and CRUD Operations

The application uses the following view functions:

- `task_list`: Retrieves and displays all tasks.
- `add_task`: Displays the task creation form and saves new tasks.
- `toggle_task`: Changes the completion status of a task.
- `delete_task`: Deletes a selected task.

These functions are defined in `views.py`.

### D. URL Routing

The application's URLs are configured in `todo/urls.py` and included in the main project URL configuration.

| URL | Function |
|---|---|
| `/` | Display the task list |
| `/add/` | Add a new task |
| `/toggle/<task_id>/` | Toggle task completion status |
| `/delete/<task_id>/` | Delete a task |
| `/admin/` | Access the Django administration panel |

### E. Templates and Template Inheritance

The application uses Django templates to render HTML pages.

- `base.html`: Defines the common page layout and loads the CSS file.
- `task_list.html`: Displays tasks and their available actions.
- `add_task.html`: Provides a form to create new tasks.
- `header.html`: Contains the reusable header.
- `footer.html`: Contains the reusable footer.

The `{% extends %}` tag allows `task_list.html` and `add_task.html` to inherit the common layout from `base.html`.

The `{% include %}` tag allows the header and footer to be reused across multiple pages.

### F. Static File Management

The stylesheet is stored at:

```text
todo/static/todo/style.css
```

The `base.html` template uses `{% load static %}` and the `{% static %}` template tag to load the stylesheet.

The CSS file controls the page background, typography, colours, spacing, and other visual properties.

## 7. Installation and Execution

### Prerequisites

- Python 3 installed.
- pip available.
- Visual Studio Code or another code editor.

### Step 1: Open the Project Directory

Open the project folder in VS Code and open a terminal in the project root.

### Step 2: Create a Virtual Environment

```powershell
python -m venv venv
```

### Step 3: Activate the Virtual Environment

On Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### Step 4: Install Django

```powershell
python -m pip install django
```

### Step 5: Apply Database Migrations

```powershell
python manage.py makemigrations
python manage.py migrate
```

### Step 6: Start the Development Server

```powershell
python manage.py runserver
```

Open the following URL in a browser:

http://127.0.0.1:8000/

**Note:** The project was developed using Django. If you are setting it up on another computer, install the required dependencies before running it.

## 8. Testing

The following operations can be tested through the web interface:

1. **Create:** Add a new task using the task creation form.
2. **Read:** Verify that the task appears in the task list.
3. **Update:** Use the Toggle link to mark a task as completed or incomplete.
4. **Delete:** Use the Delete link to remove a task.

Additional checks:

- Verify that the CSS stylesheet loads correctly.
- Verify that the header and footer appear on both pages.
- Verify that the application displays an appropriate message when no tasks exist.
- Verify that tasks remain stored after refreshing the page.

## 9. Result

A Django-based To-Do List web application was developed successfully. The application supports task creation, task listing, completion-status updates, and deletion. Django ORM, SQLite, template inheritance, reusable template components, and static CSS files were used to implement the application.

## 10. Conclusion

This experiment demonstrates the fundamentals of Django web application development, including project configuration, application structure, database modelling, URL routing, views, CRUD operations, template inheritance, template inclusion, and static file handling.

## 11. Learning Outcomes

After completing this experiment, the following concepts were practised:

- Django project and app creation.
- Database operations using Django ORM.
- Request handling through views and URL patterns.
- Dynamic HTML rendering with Django templates.
- Reusable page layouts using `extends` and `include`.
- CSS integration through the static files system.
- Testing CRUD functionality in a web application.

---

**Experiment:** 15  
**Project:** Django To-Do Application  
**Framework:** Django  
**Database:** SQLite  
**Status:** Successfully implemented and tested locally.
