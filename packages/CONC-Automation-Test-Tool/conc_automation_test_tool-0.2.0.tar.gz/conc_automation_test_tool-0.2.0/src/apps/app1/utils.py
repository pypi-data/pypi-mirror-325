import pandas as pd

def create_workflow_xlsx(file_path):
    # Define columns based on the WorkFlow model
    columns = [
        "WorkflowUID", "Workflow", "Step", "Mock_Factor", "Batch_Number", "Input_type",
        "REST_input", "Kafka_Input", "Input_Mock_type", "Output_type", "Output_Sample_Content",
        "Output_Mock_type", "Dependent_Rest_APIs", "Dependent_DBData", "total_expected_runs",
        "noOfExecutions_done", "Status"
    ]
    
    # Create dummy data
    data = [
        {
            "WorkflowUID": "UID1", "Workflow": "Workflow1", "Step": 1, "Mock_Factor": 10, "Batch_Number": 1, "Input_type": "REST",
            "REST_input": "{}", "Kafka_Input": "{}", "Input_Mock_type": "{}", "Output_type": "REST", "Output_Sample_Content": "{}",
            "Output_Mock_type": "{}", "Dependent_Rest_APIs": "{}", "Dependent_DBData": "{}", "total_expected_runs": 100,
            "noOfExecutions_done": 0, "Status": "pending"
        },
        {
            "WorkflowUID": "UID2", "Workflow": "Workflow2", "Step": 2, "Mock_Factor": 20, "Batch_Number": 2, "Input_type": "REST",
            "REST_input": "{}", "Kafka_Input": "{}", "Input_Mock_type": "{}", "Output_type": "REST", "Output_Sample_Content": "{}",
            "Output_Mock_type": "{}", "Dependent_Rest_APIs": "{}", "Dependent_DBData": "{}", "total_expected_runs": 200,
            "noOfExecutions_done": 0, "Status": "pending"
        },
        {
            "WorkflowUID": "UID3", "Workflow": "Workflow3", "Step": 3, "Mock_Factor": 30, "Batch_Number": 3, "Input_type": "REST",
            "REST_input": "{}", "Kafka_Input": "{}", "Input_Mock_type": "{}", "Output_type": "REST", "Output_Sample_Content": "{}",
            "Output_Mock_type": "{}", "Dependent_Rest_APIs": "{}", "Dependent_DBData": "{}", "total_expected_runs": 300,
            "noOfExecutions_done": 0, "Status": "pending"
        },
        {
            "WorkflowUID": "UID4", "Workflow": "Workflow4", "Step": 4, "Mock_Factor": 40, "Batch_Number": 4, "Input_type": "REST",
            "REST_input": "{}", "Kafka_Input": "{}", "Input_Mock_type": "{}", "Output_type": "REST", "Output_Sample_Content": "{}",
            "Output_Mock_type": "{}", "Dependent_Rest_APIs": "{}", "Dependent_DBData": "{}", "total_expected_runs": 400,
            "noOfExecutions_done": 0, "Status": "pending"
        },
        {
            "WorkflowUID": "UID5", "Workflow": "Workflow5", "Step": 5, "Mock_Factor": 50, "Batch_Number": 5, "Input_type": "REST",
            "REST_input": "{}", "Kafka_Input": "{}", "Input_Mock_type": "{}", "Output_type": "REST", "Output_Sample_Content": "{}",
            "Output_Mock_type": "{}", "Dependent_Rest_APIs": "{}", "Dependent_DBData": "{}", "total_expected_runs": 500,
            "noOfExecutions_done": 0, "Status": "pending"
        }
    ]
    
    # Create DataFrame
    df = pd.DataFrame(data, columns=columns)
    
    # Write DataFrame to XLSX file
    df.to_excel(file_path, index=False)
    print(f"XLSX file created at {file_path}")

def create_simulated_data_xlsx(file_path):
    # Define columns based on the SimulatedData model
    columns = ["workflow_UID", "Input_SimulatedData", "Output_SimulatedData", "ValidationStatus", "Step_Number"]
    
    # Create dummy data
    data = [
        {"workflow_UID": "UID1", "Input_SimulatedData": "{}", "Output_SimulatedData": "{}", "ValidationStatus": "pending", "Step_Number": 1},
        {"workflow_UID": "UID2", "Input_SimulatedData": "{}", "Output_SimulatedData": "{}", "ValidationStatus": "pending", "Step_Number": 2},
        {"workflow_UID": "UID3", "Input_SimulatedData": "{}", "Output_SimulatedData": "{}", "ValidationStatus": "pending", "Step_Number": 3},
        {"workflow_UID": "UID4", "Input_SimulatedData": "{}", "Output_SimulatedData": "{}", "ValidationStatus": "pending", "Step_Number": 4},
        {"workflow_UID": "UID5", "Input_SimulatedData": "{}", "Output_SimulatedData": "{}", "ValidationStatus": "pending", "Step_Number": 5}
    ]
    
    # Create DataFrame
    df = pd.DataFrame(data, columns=columns)
    
    # Write DataFrame to XLSX file
    df.to_excel(file_path, index=False)
    print(f"XLSX file created at {file_path}")

if __name__ == "__main__":
    create_workflow_xlsx("workflow_data.xlsx")
    create_simulated_data_xlsx("simulated_data.xlsx")