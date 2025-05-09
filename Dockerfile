FROM ghcr.io/mlflow/mlflow:v2.22.0

# Install psycopg2-binary
RUN pip install psycopg2-binary==2.9.10
