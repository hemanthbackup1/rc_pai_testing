from dataproc.jobs.utils.nv_db_connection import get_db_session
from  dataproc.config.config import Config

def test_db_connection():
    """Test if the database connection is established successfully."""
    try:
        session = get_db_session()
        print("Database connection established successfully.")
        session.shutdown()  # Clean up the session
    except Exception as e:
        print(f"Failed to connect to the database: {e}")
    

def test_db_query():
    """Test if a basic query can be executed on the database."""
    try:
        session = get_db_session()
        query = f"SELECT * FROM card_statement.fixed_statement_202406"  
        rows = session.execute(query)
        print("Query executed successfully. Results:")
        for row in rows:
            print(row)
        session.shutdown()  # Clean up the session
    except Exception as e:
        print(f"Failed to execute query: {e}")

if __name__ == "__main__":
    print("")
    print("Testing database connection...")
    test_db_connection()
    print("\nTesting database query...")
    test_db_query()
