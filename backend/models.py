from config import db

class Tasks(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    to_do = db.Column(db.String(200), nullable=False)
    in_progress = db.Column(db.String(200), nullable=False)
    done = db.Column(db.String(200), nullable=False)
    pending = db.Column(db.String(200), nullable=False)
    
    def to_json(self):
        return {
            "id": self.id,
            "email": self.email,
            "tasks": { # a dictionary of tasks of different columns
                "toDo": self.to_do, # a list of tasks
                "inProgress": self.in_progress, 
                "done": self.done,
                "pending": self.pending,
            }
        }