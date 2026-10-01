# Lecture 15 - Data Modeling and Database Interaction

## 1. Objective

The objective of this lecture was to understand data modeling and database interaction using SQLAlchemy and Mongoose.

In this lecture, I learned:

- Data modeling concepts
- SQLAlchemy with SQLite
- Creating database models
- Relationships between tables
- CRUD operations
- Mongoose with MongoDB
- Creating schemas and models
- Data validation in Mongoose

---

## 2. Technologies Used

- Python
- SQLAlchemy
- SQLite
- Node.js
- MongoDB
- Mongoose
- JavaScript
- VS Code

---

## 3. Data Modeling

Data modeling is the process of designing how data is organized and related in a database.

The main levels of data modeling are:

1. Conceptual Data Model
2. Logical Data Model
3. Physical Data Model

In this lecture, database models were created using SQLAlchemy and Mongoose.

---

## 4. SQLAlchemy Database Connection

SQLite was used as the database for the Student Management System.

The database connection was created using SQLAlchemy:

```python
from sqlalchemy import create_engine

engine = create_engine("sqlite:///students.db")