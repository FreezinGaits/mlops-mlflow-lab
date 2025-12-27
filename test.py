import mlflow
# print("Printing tracking URI scheme below")
# print(mlflow.get_tracking_uri())
# print("\n")

# mlflow.set_tracking_uri("http://127.0.0.1:5000")
# print("Printing new tracking URI scheme below")
# print(mlflow.get_tracking_uri())
# print("\n")

from mlflow import get_experiment_by_name
exp = mlflow.get_experiment_by_name("MLOPS-Exp1")
print(exp.experiment_id)
print(exp.name)