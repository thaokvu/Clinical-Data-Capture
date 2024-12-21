from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuration for the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clinical_data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Patient model
class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    condition = db.Column(db.String(100), nullable=False)
    trial_status = db.Column(db.String(100), nullable=False)

# Route to display the patient table and add patients
@app.route('/')
def index():
    patients = Patient.query.all()
    return render_template('index.html', patients=patients)

# Route to add a new patient
@app.route('/add_patient', methods=['GET', 'POST'])
def add_patient():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        condition = request.form['condition']
        trial_status = request.form['trial_status']

        new_patient = Patient(
            name=name,
            age=age,
            condition=condition,
            trial_status=trial_status
        )
        db.session.add(new_patient)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_patient.html')

# Route to edit a patient's details
@app.route('/edit_patient/<int:id>', methods=['GET', 'POST'])
def edit_patient(id):
    patient = Patient.query.get_or_404(id)
    if request.method == 'POST':
        patient.name = request.form['name']
        patient.age = request.form['age']
        patient.condition = request.form['condition']
        patient.trial_status = request.form['trial_status']

        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit_patient.html', patient=patient)

# Route to delete a patient
@app.route('/delete_patient/<int:id>', methods=['POST'])
def delete_patient(id):
    patient = Patient.query.get_or_404(id)
    db.session.delete(patient)
    db.session.commit()
    return redirect('/')

# Run the Flask application
if __name__ == '__main__':
    # Ensure the database is created
    with app.app_context():
        db.create_all()
    app.run(debug=True)

