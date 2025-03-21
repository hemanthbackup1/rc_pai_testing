import os
import shutil
import logging
from pyspark.sql import SparkSession
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from dotenv import load_dotenv
from utils import get_env_var

# Load environment variables
load_dotenv()

# Fetch required variables
ASTRA_DB_SECURE_BUNDLE = get_env_var("ASTRA_DB_SECURE_BUNDLE")
ASTRA_DB_KEYSPACE = get_env_var("ASTRA_DB_KEYSPACE")
ASTRA_DB_TABLE = get_env_var("ASTRA_DB_TABLE")
GCS_OUTPUT_PATH = get_env_var("GCS_OUTPUT_PATH")

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("AstraDB-Dataproc-Extraction") \
    .config("spark.jars.packages", "com.datastax.spark:spark-cassandra-connector_2.12:3.2.0") \
    .getOrCreate()

# Download Secure Connect Bundle from GCS
sc = spark.sparkContext
secure_bundle_local_path = "/tmp/secure-connect-database.zip"
sc.addFile(ASTRA_DB_SECURE_BUNDLE)

# Copy file from Spark temp directory
shutil.copy(sc.addFile(secure_bundle_local_path), secure_bundle_local_path)

# Connect to Astra DB
cloud_config = {'secure_connect_bundle': secure_bundle_local_path}
auth_provider = PlainTextAuthProvider('', '')
cluster = Cluster(cloud=cloud_config)
session = cluster.connect()

# Load Data
session.set_keyspace(ASTRA_DB_KEYSPACE)
query = f"SELECT * FROM {ASTRA_DB_TABLE}"
rows = session.execute(query)

# Convert data to DataFrame
columns = rows.column_names
df = spark.createDataFrame(rows, columns)

# Write to GCS as TXT
df.write.mode("overwrite").format("text").save(GCS_OUTPUT_PATH)

logging.info(f"✅ Data successfully written to {GCS_OUTPUT_PATH}")

# Stop Spark session
spark.stop()
