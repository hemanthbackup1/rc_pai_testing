# Use official Dataproc image as base
FROM us-docker.pkg.dev/cloud-dataproc/container/spark-py:2.2

# Set a writable directory as home
ENV HOME=/tmp
WORKDIR /tmp

# Copy the application code
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set Spark user to root to avoid permission errors
USER root

# Set the entrypoint
CMD ["python", "jobs/dataproc_astra_job.py"]
