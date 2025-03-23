# Use the official Python image
FROM python:3.8-slim

# Set a writable working directory (Dataproc containers have write access to /tmp)
WORKDIR /tmp

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Ensure /tmp is used for temporary files
ENV PYSPARK_PYTHON=/usr/local/bin/python
ENV SPARK_HOME=/usr/local/spark

# Run the PySpark job
CMD ["python", "jobs/dataproc_astra_job.py"]
