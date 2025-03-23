from cassandra.cluster import Cluster, ExecutionProfile, EXEC_PROFILE_DEFAULT, ProtocolVersion
from cassandra.auth import PlainTextAuthProvider
from  dataproc.config.config import Config
import logging

logger = logging.getLogger("rc_pai")

def get_db_session():
    """Establish a connection to Astra DB and return a session."""
    try:
        cloud_config= {
        'secure_connect_bundle': Config.ASTRA_DB_SECURE_BUNDLE_PATH,
        'connect_timeout': 30
        }
        profile = ExecutionProfile(request_timeout=30)
        auth_provider = PlainTextAuthProvider(Config.ASTRA_DB_CLIENT_ID, Config.ASTRA_DB_CLIENT_SECRET)
        cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider, protocol_version=ProtocolVersion.V4, execution_profiles={EXEC_PROFILE_DEFAULT: profile})
        # Config=Config()
        # print(Config)
        # Set up the authentication provider
        
        print(Config.ASTRA_DB_SECURE_BUNDLE_PATH)
        
        # Create a cluster instance
        cluster = Cluster(cloud={'secure_connect_bundle': Config.ASTRA_DB_SECURE_BUNDLE_PATH}, auth_provider=auth_provider)

        # Connect to the cluster and specify the keyspace
        session = cluster.connect()
        logger.info("Connection to Astra DB established successfully.")
    
        
        print("Connection to Astra DB established successfully.")
        return session
    except Exception as e:
        logger.error(f"Failed to connect to Astra DB: {e}")
        print("Failed to connect to Astra DB.")
        raise