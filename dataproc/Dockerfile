# Use the official Python image
FROM python:3.8-slim

# Set writable working directory
WORKDIR /tmp

# Set the home directory to /tmp (avoids permission issues)
ENV HOME=/tmp

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Run the PySpark job
CMD ["python", "jobs/dataproc_astra_job.py"]
