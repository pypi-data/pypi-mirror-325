from flask import Flask
from config.settings import config
from config.db_config import db
from apps.app1.routes import app1
from apps.app1.models import WorkFlow, SimulatedData
from apps.app2.models import AnotherTable

app = Flask(__name__)
app.config.from_object(config['development'])

# Initialize the database
db.init_app(app)

# Register blueprints
app.register_blueprint(app1, url_prefix='/api/v1')

def create_tables():
    with app.app_context():
        db.create_all()
        print("Tables created successfully.")

if __name__ == "__main__":
    # create_tables()
    app.run(debug=True)