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
```

---



5. SQLAlchemy Models

The following models were created:

Department
Student
Course
Enrollment

Relationships were created using SQLAlchemy's relationship() and back_populates.

Foreign keys were used to connect the related tables.

The main relationships are:

One Department can have many Students.
One Student can have many Enrollments.
One Course can have many Enrollments.
6. Creating Database Tables

After defining the models, the database tables were created using:

Base.metadata.create_all(engine)

This creates the required tables in the SQLite database.

The tables were created successfully when the program was executed.

7. CRUD Operations

CRUD stands for:

Create
Read
Update
Delete

CRUD operations were performed on the Student Management System using SQLAlchemy.

Create Operation

A department and a student were created and stored in the database.

Student details:

Name: Aarav
Email: aarav@upes.ac.in
Branch: CSE
Date of Birth: 2026-10-01

The changes were saved using:

session.commit()
Read Operation

The database was queried to retrieve students belonging to the CSE branch.

The retrieved student information was displayed in the terminal.

Update Operation

The student's branch was updated from:

CSE

to:

ECE

The updated information was saved using:

session.commit()
Delete Operation

The student was deleted from the database using SQLAlchemy.

After deleting the student, the database was queried again to verify the deletion.

The output confirmed that the student no longer existed in the database.

CRUD Result
Operation	Result
Create	Student created successfully
Read	Student information retrieved successfully
Update	Branch updated from CSE to ECE
Delete	Student deleted successfully
Verification	Deletion verified successfully
8. SQLAlchemy Session

A SQLAlchemy session was used to communicate with the database.

The session was responsible for:

Adding new records
Reading records
Updating records
Deleting records
Committing changes to the database

Changes were saved using:

session.commit()
9. Mongoose

Mongoose is an Object Data Modeling (ODM) library for MongoDB and Node.js.

It provides a structured way to work with MongoDB databases.

Mongoose was installed using:

npm install mongoose

A separate Node.js project was created for the Mongoose implementation.

10. MongoDB Connection

MongoDB was connected using the following connection string:

mongodb://127.0.0.1:27017/blog_database

The connection was tested successfully.

The program displayed:

MongoDB connected successfully!
11. Blog Application Models

A simple Blog Application was created using Mongoose.

Two main models were created:

Post
Comment
Post

The Post model contains fields such as:

title
content
author
createdAt
Comment

The Comment model contains:

postId
author
text
createdAt

The postId field connects a comment with a particular post.

12. Mongoose Schema

A schema defines the structure of documents stored in MongoDB.

A Post schema was created with fields such as title, content, author and createdAt.

A Comment schema was also created with postId, author, text and createdAt.

Models were created from these schemas using Mongoose.

13. Mongoose CRUD Operations

Mongoose was used to perform database operations.

The following operations were tested:

Creating a Post
Creating a Comment
Reading database information
Validating data

A valid post and comment were successfully created in MongoDB.

14. Mongoose Validation

Validation is used to make sure that the data entered into the database follows the required rules.

The following validation features were studied:

required
unique
enum
minlength
maxlength
match
min
max

For example:

title: {
    type: String,
    required: true
}

This means that the title field must be provided.

15. Testing Validation

Invalid data was tested to check whether Mongoose validation works correctly.

When invalid data was provided, Mongoose generated a validation error.

Valid data was then provided.

The valid Post and Comment were successfully created.

Example output:

MongoDB connected successfully!

Valid post created successfully!

Valid comment created successfully!

MongoDB connection closed.

This confirmed that the Mongoose connection, models and validation were working correctly.

16. Files Created

The Lecture 15 folder contains the following files:

Lecture15/
│
├── README.md
├── .gitignore
├── student_management.py
│
└── Lecture15_Mongoose/
    ├── blog.js
    ├── package.json
    └── package-lock.json

The .gitignore file was used to prevent unnecessary files such as the SQLite database and node_modules from being uploaded to GitHub.

17. Lab Exercise

The lecture also included a conceptual data modeling exercise for an E-Commerce system.

The entities mentioned in the exercise are:

Product
Order
Customer
Cart

These entities can be used to design a conceptual data model showing how customers, products, orders and carts are related.

18. What I Learned

From this lecture, I learned:

How to create database models using SQLAlchemy.
How to connect Python applications with SQLite.
How to create tables using SQLAlchemy.
How to define relationships between database tables.
How to perform CRUD operations.
How to connect Node.js with MongoDB using Mongoose.
How to create Mongoose schemas and models.
How to create and store documents in MongoDB.
How to apply validation rules to MongoDB documents.
How to test valid and invalid data.
19. Result

The SQLAlchemy Student Management System was successfully implemented and tested.

The following operations were successfully performed:

Database connection
Table creation
Student creation
Student retrieval
Student branch update
Student deletion
Verification of deletion

The Mongoose Blog Application was also successfully implemented.

The following were successfully tested:

MongoDB connection
Post creation
Comment creation
Mongoose schema
Data validation

Therefore, the main practical concepts of Lecture 15 were successfully implemented.