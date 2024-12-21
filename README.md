# Clinical Data Capture System

A lightweight web application for managing clinical trial data. This project provides a platform to add, edit, delete, and view patient information, including age, condition, and trial status.

## Features
- Add Patients - Input patient details such as name, age, medical condition, and trial status
- Edit Patient Data - Modify existing patient details
- Delete Patient - Remove patients from the database
- View Patient List - Display all patient records in a table format
- Responsive Design - Clean, user-friendly interface

## Technologies Used
### Backend
- **Python** - Programming Language
- **Flask** - Lightweight web framework for backend development
- **SQLALchemy** - Object-relational mapping (ORM) for handling database operations
- **SQLite** - Lightweight relational database

### Frontend
- **HTML5** - For structuring the web application
- **CSS3** - For styling and enhancing the design


## Getting Started
Follow these steps to set up and run the project locally.

### Prerequisites
- **Python 3.10+** installed on your machine
- **Python package manager (pip)** installed

### Installation
1. **Clone the Repository**
   - git clone https://github.com/thaokvu/clinical-data-capture.git
   - cd clinical-data-capture
2. **Install Dependencies** - Use the following command to install all required Python packages
   - pip install -r requirements.txt
3. **Set up the Database** - Run the following commands in a Python shell to create the database schema
   - from main import db, app
   - with app.app_context():
   - db.create_all()
4. **Start the application** - Run the Flask development server using the command
   - python main.py
5. **Access the Application** - Open your browser and navigate to: http://127.0.0.1:5000

