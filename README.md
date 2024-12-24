[## Overview
A web-based application for managing patient information in clinical trials. This system allows users to add, view, edit, and delete patient records while ensuring a user-friendly interface and robust backend functionality. Built using Flask, SQLAlchemy, and Jinja2, the project seamlessly integrates front-end design and back-end logic for managing clinical data efficiently.

## Features
- Add Patients - Input patient details such as name, age, medical condition, and trial status
- Edit Existing Patient Data - Modify existing patient details dynamically
- Delete Patient - Remove patient data with a confirmation prompt to prevent accidental deletion
- View Patient List - Display all patient records in a table format
- Responsive Design - User-friendly interface with a clean and modern design

## Technologies Used
### Frontend
- **HTML** - Structuring the web pages for displaying patient information and forms
- **CSS** - Styling the interface to make it visually appealing and user-friendly
- **JavaScript** - Adding interactivity, such as the confirmation dialog for deleting a patient
- **Jinja2** - Template engine for dynamically rendering HTML content based on backend data

### Backend
- **Python** - Core programming language for backend logic
- **Flask** - Framework for routing, handling HTTP requests, and managing server-side logic
- **SQLite** - Lightweight database for storing and managing patient data
- **SQLAlchemy** - Object-Relational Mapping (ORM) library for interacting with SQLite database

## Getting Started
Follow these steps to set up and run the project locally.
### Prerequisites
- **Python 3.10+** installed on your machine
- **Python package manager (pip)** installed

### Installation
1. **Clone the Repository**
   ```bash
   git clone https://github.com/thaokvu/clinical-data-capture.git
   cd clinical-data-capture
   ```
   
3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   
4. **Set up the Database**
   ```bash
   from main import db, app
   with app.app_context():
   db.create_all()
   ```
   
6. **Start the Application**
   ```bash
   python main.py
   ```
   
8. **Access the Application** - Open your browser and navigate to: http://127.0.0.1:5000

## Project Structure
This project follows a simple and organized structure to make the codebase easy to understand and maintain. 

### Layout
<img width="482" alt="image" src="https://github.com/user-attachments/assets/6e3cbb9d-85e2-4a83-8c64-896099aa645e" />

### Folder and File Description
- **`static/style.css`** - Contains custom CSS to style the web pages and improve the user interface
- **`templates/`** - Holds all the HTML templates for the web application
    - **`add_patient.html`** - Displays the form for adding a new patient
    - **`index_html`** - The main page that lists all patients in the database
    - **`edit_patient.html`** - Displays the form for editing patient details
- **`clinical_data.db`** - The SQLite database file where patient information is stored; it is auto-generated when the application is run for the first time
- **`main.py`** - The main Flask application file that contains the app routes and logic
- **`requirements.txt`** - Lists all the Python dependencies required to run the project
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
4. **View All Patient**
  - The homepage displays a list of all patients in a table format, including their details and actions

## Screenshots

### **Homepage - List of Patients**
`http://127.0.0.1:5000/`
- The table should display patient details (name, age, condition, trial status) with action buttons for "Edit" and "Delete".
<img width="959" alt="Clinical Data Capture System - Homepage (index html)" src="https://github.com/user-attachments/assets/65f1d6e3-1f0a-4cdd-8f04-c84f7dde3642" />
<img width="959" alt="Clinical Data Capture System - Homepage with Added Patient" src="https://github.com/user-attachments/assets/af0406f9-3ab3-4e0c-b649-4116cad81a50" />

### **Add Patient Page**
`http://127.0.0.1:5000/add_patient`
- Users can input details for a new patient.
<img width="959" alt="Clinical Data Capture System - Add Patient (add_patient html)" src="https://github.com/user-attachments/assets/5380d027-b2d4-4a4a-80f4-eabae06be7dd" />
<img width="959" alt="Clinical Data Capture System - Add Patient (John Doe)" src="https://github.com/user-attachments/assets/96333898-9629-42ed-b585-17462193c292" />

### **Edit Patient Page**
`http://127.0.0.1:5000/edit_patient/1`
- Users can update patient information. The form is pre-filled with existing patient details for easy editing.
<img width="959" alt="Clinical Data Capture System - Edit Patient (edit_patient html)" src="https://github.com/user-attachments/assets/e939f8db-b56e-4917-b63f-b4a0caa61b93" />

### **Delete Patient Confirmation Dialog**
- Confirmation dialog that appears when the "Delete" button is pressed. The dialog helps prevent accidental deletions by asking the user for confirmation before proceeding.
<img width="959" alt="Clinical Data Capture System - Delete Patient Confirmation" src="https://github.com/user-attachments/assets/5b6b16a1-979a-4993-827f-d827ff817c2f" />

### Clinical Data Capture System Demo
https://github.com/user-attachments/assets/23a67082-1c91-4942-888f-bba7465ab1e7



