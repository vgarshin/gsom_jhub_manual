#!/bin/bash

# Home directory for MLflow
MLFLOW_PATH=/home/jovyan/${JUPYTERHUB_USER}_mlflow

# Install MLflow
pip install mlflow==2.19.0

# Start MLflow
cd ~ && mlflow server --host 0.0.0.0 --port 50000 \
  --backend-store-uri file://${MLFLOW_PATH} \
  --default-artifact-root file://${MLFLOW_PATH} \
  &>/dev/null & disown;

