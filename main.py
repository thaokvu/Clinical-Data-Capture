'''
This Flask application is designed to manage patient data for a clinical trial system.
It provides a web interace for performing CRUD (Create, Read, Update, Delete) operations
on a SQLite database that stores patient information such as name, age, medical condition,
and trial status.

Features of the application - 
1. Displays a list of all patients in the system on the homepage
2. Add a new patient to the database using a form
3. Edit an existing patient's detail
4. Delete a patient's record from the database

The application uses Flask for web development and Flask-SQLAlchemy for database interaction.
The database is initialized with SQLite, and the application is designed to run locally in debug mode.
'''

from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy

# Initalize the Flask application 
app = Flask(__name__)
# Configure the database connection to use SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clinical_data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Patient model definition
class Patient(db.Model):
    # Define columns for the Patient table
    # Primary key (unique identifier for each patient)
    id = db.Column(db.Integer, primary_key=True)
    # Patient name
    name = db.Column(db.String(100), nullable=False)
    # Patient age
    age = db.Column(db.Integer, nullable=False)
    # Patient medical condition
    condition = db.Column(db.String(100), nullable=True)
    # Patient status in a clinical trial
    trial_status = db.Column(db.String(100), nullable=True)

# Define routes for the homepage
@app.route('/')
def index():
    # Query all patients from the database
    patients = Patient.query.all()  
    # Render the homepage template and pass the list of patients
    return render_template('index.html', patients=patients)

# Define route to add a new patient
@app.route('/add_patient', methods=['GET', 'POST'])
def add_patient():
    # Handle form submission
    if request.method == 'POST':
        # Extract form data
        name = request.form['name']
        age = request.form['age']
        condition = request.form['condition']
        trial_status = request.form['trial_status']

        # Create a new patient and add to the database
        new_patient = Patient(name=name, age=age, condition=condition, trial_status=trial_status)
        db.session.add(new_patient)
        db.session.commit()

        # Redirect to the homepage
        return redirect(url_for('index'))

    # Render the Add Patient form for GET requests
    return render_template('add_patient.html')

# Define route to edit an existing patient's details
@app.route('/edit_patient/<int:patient_id>', methods=['GET', 'POST'])
def edit_patient(patient_id):
    # Retrieve the patient by ID or return a 404 if not found
    patient = Patient.query.get_or_404(patient_id)

    # Handle form submission
    if request.method == 'POST':
        # Update patient details with form data
        patient.name = request.form['name']
        patient.age = request.form['age']
        patient.condition = request.form['condition']
        patient.trial_status = request.form['trial_status']

        # Save the updated details to the database
        db.session.commit()

        # Redirect to the homepage
        return redirect(url_for('index'))

    # Render the edit form with the current patient data for GET requests
    return render_template('edit_patient.html', patient=patient)

# Define route to delete a patient
@app.route('/delete_patient/<int:patient_id>', methods=['POST'])
def delete_patient(patient_id):
    # Retrieve the patient record by ID, or return a 404 error if not found
    patient = Patient.query.get_or_404(patient_id)
    # Delete the patient record from the database
    db.session.delete(patient)
    db.session.commit()
    
    # Redirect to the homepage
    return redirect(url_for('index'))

# Entry point for the Flask application
if __name__ == '__main__':
    with app.app_context():
        # Ensure database tables are created before the app runs
        db.create_all()  
    # Run the application in debug mode
    app.run(debug=True)
