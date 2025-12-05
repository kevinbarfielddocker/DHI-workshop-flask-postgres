import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the database connection using environment variables
# Format: postgresql://user:password@host:port/database_name
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define the Guest Model (The Table)
class Guest(db.Model):
    __tablename__ = 'guests'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    party_size = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Guest {self.name}>'

# Create tables if they don't exist
with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get data from form
        name = request.form['name']
        email = request.form['email']
        party_size = request.form['party_size']

        # Save to database
        new_guest = Guest(name=name, email=email, party_size=party_size)
        db.session.add(new_guest)
        db.session.commit()
        return redirect(url_for('index'))

    # Get all guests to display
    guests = Guest.query.all()
    return render_template('index.html', guests=guests)

if __name__ == '__main__':
    # host='0.0.0.0' is required for Docker containers to be accessible
    app.run(debug=True, host='0.0.0.0', port=5000)