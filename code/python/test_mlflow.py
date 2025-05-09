import mlflow
from mlflow.tracking import MlflowClient
import pandas as pd
import os

print(f"Current working directory: {os.getcwd()}")
mlflow.set_tracking_uri("http://psylomlflow.psylo-exp.orb.local:5001")
client = MlflowClient()
experiment_name = "psylo_test"
experiment = client.get_experiment_by_name(experiment_name)
if not experiment:
    experiment_id = client.create_experiment(
        experiment_name,
        artifact_location=os.path.abspath("mlflow_artifacts")
    )
else:
    experiment_id = experiment.experiment_id
    print(f"Experiment artifact location: {experiment.artifact_location}")

with mlflow.start_run(experiment_id=experiment_id):
    print(f"Tracking URI: {mlflow.get_tracking_uri()}")
    print(f"Run artifact URI: {mlflow.get_artifact_uri()}")
    df = pd.read_csv("data/my_raw_data.csv")
    mean_item_1 = df["item_1"].mean()
    mlflow.log_param("dataset", "my_raw_data.csv")
    mlflow.log_metric("mean_item_1", mean_item_1)
    artifact_path = os.path.abspath("data/my_raw_data.csv")
    print(f"Logging artifact: {artifact_path}")
    try:
        mlflow.log_artifact(artifact_path)
        print("Artifact logged successfully")
    except Exception as e:
        print(f"Failed to log artifact: {e}")
