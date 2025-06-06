from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")
db = SQLAlchemy(app)

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    eleve_id = db.Column(db.String(10))
    question1 = db.Column(db.String(100))
    question2 = db.Column(db.String(100))

@app.route('/', methods=['GET', 'POST'])
def qcm():
    eleve_id = request.args.get('eleve')
    if request.method == 'POST':
        q1 = request.form['question1']
        q2 = request.form['question2']
        answer = Answer(question1=q1, question2=q2, eleve_id=eleve_id)
        db.session.add(answer)
        db.session.commit()
        return redirect(f"/resultats/{eleve_id}")
    return render_template("qcm.html", eleve_id=eleve_id)

def corriger(q1, q2):
    note = 0
    if q1 == "finis": note += 1
    if q2 == "finissent": note += 1
    return note

@app.route('/resultats/<eleve_id>')
def resultats(eleve_id):
    reponses = Answer.query.filter_by(eleve_id=eleve_id).all()
    notes = [corriger(r.question1, r.question2) for r in reponses]
    return render_template("resultats.html", reponses=reponses, notes=notes, eleve_id=eleve_id)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
