from app import app, db

def init_db():
    with app.app_context():
        db.drop_all()  # Clear existing tables
        db.create_all()  # Create new tables
        
if __name__ == '__main__':
    init_db()