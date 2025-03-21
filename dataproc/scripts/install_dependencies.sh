#!/bin/bash

echo "Installing required Python packages..."

# Upgrade pip to the latest version
pip install --upgrade pip

# Install required dependencies
pip install \
    pyspark==3.1.2 \
    cassandra-driver==3.25.0 \
    python-dotenv==0.19.0 \
    google-cloud-storage \
    google-cloud-dataproc \
    requests==2.26.0 \
    numpy==1.21.2 \
    pandas==1.3.3 \
    astrapy==0.1.0 \
    flask==2.1.1

echo "✅ All dependencies installed successfully!"
