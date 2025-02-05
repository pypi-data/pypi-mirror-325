import pandas as pd
from flask import request, jsonify
from config.db_config import db
from apps.app1.models import WorkFlow, SimulatedData

# Function to get all workflow data
def get_data_workflow():
    workflows = WorkFlow.query.all()
    return jsonify([workflow.to_dict() for workflow in workflows])

# Function to get all simulated data
def get_data_simulated_data():
    simulated_data = SimulatedData.query.all()
    return jsonify([data.to_dict() for data in simulated_data])

# Function to validate workflow data against required fields
def validate_workflow_data(data):
    required_fields = [
        "WorkflowUID", "Workflow", "Step", "Mock_Factor", "Batch_Number", "Input_type",
        "REST_input", "Kafka_Input", "Input_Mock_type", "Output_type", "Output_Sample_Content",
        "Output_Mock_type", "Dependent_Rest_APIs", "Dependent_DBData", "total_expected_runs",
        "noOfExecutions_done", "Status"
    ]
    missing_fields = [field for field in required_fields if field not in data]
    return missing_fields

# Function to validate simulated data against required fields
def validate_simulated_data(data):
    required_fields = ["workflow_UID", "Input_SimulatedData", "Output_SimulatedData", "ValidationStatus", "Step_Number"]
    missing_fields = [field for field in required_fields if field not in data]
    return missing_fields

# Function to handle POST request for workflow data
# This function reads an XLSX file, validates the data, and inserts it into the WorkFlow table
def post_data_workflow():
    if 'file' not in request.files:
        return jsonify({"status": "error", "message": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"status": "error", "message": "No selected file"}), 400

    if not file.filename.endswith('.xlsx'):
        return jsonify({"status": "error", "message": "Invalid file format. Please upload an .xlsx file"}), 400

    try:
        df = pd.read_excel(file, engine='openpyxl')  # Specify the engine explicitly
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

    errors = []
    for index, row in df.iterrows():
        data = row.to_dict()
        missing_fields = validate_workflow_data(data)
        if missing_fields:
            errors.append({"row": index + 1, "missing_fields": missing_fields})
        else:
            existing_workflow = WorkFlow.query.filter_by(WorkflowUID=data['WorkflowUID']).first()
            if existing_workflow:
                errors.append({"row": index + 1, "error": f"WorkflowUID {data['WorkflowUID']} already exists"})
            else:
                new_workflow = WorkFlow(**data)
                db.session.add(new_workflow)
    if errors:
        return jsonify({"status": "error", "errors": errors}), 400
    db.session.commit()
    return jsonify({"status": "success"}), 201

# Function to handle POST request for simulated data
# This function reads an XLSX file, validates the data, and inserts it into the SimulatedData table
def post_data_simulated_data():
    if 'file' not in request.files:
        return jsonify({"status": "error", "message": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"status": "error", "message": "No selected file"}), 400

    if not file.filename.endswith('.xlsx'):
        return jsonify({"status": "error", "message": "Invalid file format. Please upload an .xlsx file"}), 400

    try:
        df = pd.read_excel(file, engine='openpyxl')  # Specify the engine explicitly
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

    errors = []
    for index, row in df.iterrows():
        data = row.to_dict()
        missing_fields = validate_simulated_data(data)
        if missing_fields:
            errors.append({"row": index + 1, "missing_fields": missing_fields})
        else:
            # Check if the workflow_UID exists in the WorkFlow table
            existing_workflow = WorkFlow.query.filter_by(WorkflowUID=data['workflow_UID']).first()
            if not existing_workflow:
                errors.append({"row": index + 1, "error": f"workflow_UID {data['workflow_UID']} does not exist in WorkFlow table"})
            else:
                existing_simulated_data = SimulatedData.query.filter_by(workflow_UID=data['workflow_UID'], Step_Number=data['Step_Number']).first()
                if existing_simulated_data:
                    errors.append({"row": index + 1, "error": f"Simulated data for workflow_UID {data['workflow_UID']} and Step_Number {data['Step_Number']} already exists"})
                else:
                    new_simulated_data = SimulatedData(**data)
                    db.session.add(new_simulated_data)
    if errors:
        return jsonify({"status": "error", "errors": errors}), 400
    db.session.commit()
    return jsonify({"status": "success"}), 201

# Helper method to convert SQLAlchemy objects to dictionaries
def to_dict(self):
    return {c.name: getattr(self, c.name) for c in self.__table__.columns}

# Add the to_dict method to the WorkFlow and SimulatedData models
WorkFlow.to_dict = to_dict
SimulatedData.to_dict = to_dict