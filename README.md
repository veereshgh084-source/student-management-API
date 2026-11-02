# student-management-API
A Student Management REST API built using Python and FastAPI. This project supports CRUD operations (Create, Read, Update, Delete), allowing users to add students, view all students, search students by ID, update student details, and delete student records. It also uses Pydantic for data validation and Swagger UI for interactive API testing.


🎓 Student Management API

A beginner-friendly REST API built using Python and FastAPI to manage student records through CRUD operations.

🚀 Features

* Add new students
* View all students
* Search students by ID
* Update student details
* Delete student records
* Automatic data validation using Pydantic
* Interactive API documentation using Swagger UI

🛠️ Technologies Used

* Python
* FastAPI
* Pydantic
* Uvicorn
* Git & GitHub

📁 Project Structure

student_management_api/
│
├── main.py
├── .gitignore
└── README.md

⚙️ Installation & Setup

1. Clone the repository

git clone YOUR_GITHUB_REPOSITORY_URL

2. Navigate to the project folder

cd student_management_api

3. Create a virtual environment

python -m venv venv

4. Activate the virtual environment

Windows:

venv\Scripts\activate

Mac/Linux:

source venv/bin/activate

5. Install dependencies

pip install fastapi uvicorn

6. Run the application

python -m uvicorn main:app --reload

🌐 API Documentation

Open the following URL in your browser:

http://127.0.0.1:8000/docs

Use Swagger UI to test all API endpoints.

📌 API Endpoints

Method	Endpoint	Description
GET	/	Home endpoint
POST	/students	Add a student
GET	/students	View all students
GET	/students/{student_id}	Get student by ID
PUT	/students/{student_id}	Update student
DELETE	/students/{student_id}	Delete student

📚 Concepts Learned

* REST API development
* HTTP methods
* CRUD operations
* Pydantic data validation
* FastAPI routing
* JSON request and response handling
* API testing with Swagger UI

⚠️ Note

This beginner version uses an in-memory Python list for storing student records. Data will reset when the application restarts.

👨‍💻 Author

Veeresh G H

Aspiring AI Engineer | Python Developer

⸻

⭐ If you find this project useful, consider giving it a star!
