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

## Project Structure
This project follows a simple and organized structure to make the codebase easy to understand and maintain. 

### Layout
<img width="482" alt="image" src="https://github.com/user-attachments/assets/6e3cbb9d-85e2-4a83-8c64-896099aa645e" />

### Folder and File Description
- **static/style.css** - Contains custom CSS to style the web pages and improve the user interface
- **templates/** - Holds all the HTML templates for the web application
    - **add_patient.html** - Displays the form for adding a new patient
    - **index_html** - The main page that lists all patients in the database
    - **edit_patient.html** - Displays the form for editing patient details
- **clinical_data.db** - The SQLite database file where patient information is stored; it is auto-generated when the application is run for the first time
- **main.py** - The main Flask application file that contains the app routes and logic
- **requirements.txt** - Lists all the Python dependencies required to run the project
- **README.md** - Project documentation that explains how to set up and use the application

### Usage
1. **Add a Patient**
  - Fill in the patient's name, age, medical condition, and trial status
  - Click the "Add Patient" button on the homepage to submit the form to add the patient to the database.
2. **Edit Patient Data**
  - Click the "Edit" button in the patient's row on the homepage
  - Update the details in the form and save changes
3. **Delete a Patient**
  - Click the "Delete" button in the patient's row on the homepage
  - Confirm the deletion to remove the patient from the database
4. **View All Patient**
  - The homepage displays a list of all patients in a table format, including their details and actions

## Screenshots

### **Homepage - Patient List**
A clean table displaying all patients
<img width="956" alt="Clinical Data Capture - index html" src="https://github.com/user-attachments/assets/db413c94-08db-4a81-a6a6-4e3b77c6fc1a" />

### **Add Patient Form**
Form to input new patient details
<img width="959" alt="Clinical Data Capture - add patient" src="https://github.com/user-attachments/assets/e50b3ee0-f043-4500-b17e-c7517a38e794" />

### **Edit Patient Form**
Form to update existing patient information
<img width="958" alt="Clinical Data Capture - edit patient" src="https://github.com/user-attachments/assets/b3af954f-507a-4805-8203-6033abc7a710" />

### **Customization**
- To change the styling of the application, edit the ```static/style.css``` file
- Update the database schema or models by modifying the

