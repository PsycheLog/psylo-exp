FROM ghcr.io/mlflow/mlflow:v2.16.2

# Install psycopg2-binary for PostgreSQL backend
RUN pip install psycopg2-binary
