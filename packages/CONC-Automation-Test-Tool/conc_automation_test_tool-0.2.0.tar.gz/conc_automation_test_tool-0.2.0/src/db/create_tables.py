from config.db_config import db
from config.settings import app
from apps.app1.models import WorkFlow, SimulatedData
from apps.app2.models import AnotherTable

def create_tables():
    with app.app_context():
        db.create_all()
        print("Tables created successfully.")

if __name__ == "__main__":
    create_tables()