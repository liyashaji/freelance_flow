from sqlalchemy import create_engine, text
import os

# Load the password from the Repository Secret
password = os.getenv("DB_CONNECTION_STRING")

# Service URI provided by Aiven
service_uri = f"mysql://avnadmin:{password}@mysql-19bbe057-freelanceflow.i.aivencloud.com:17897/defaultdb"

# Custom SSL parameters
ssl_args = {
    "ssl": {
        "ca": r"F:\desktop\freelance_flow\certs\ca.pem",
        "check_hostname": False
    }
}

# Create engine using the service URI and SSL parameters
engine = create_engine(service_uri, connect_args=ssl_args, pool_pre_ping=True)

# Test connection
try:
    with engine.connect() as conn:
        # Create a text object for the SQL query
        query = text("select * from jobs")
        
        # Execute the query
        result = conn.execute(query)
        
        # Get the column names
        column_names = [desc[0] for desc in result.cursor.description]
        
        # Convert the result rows to dictionaries
        result_dicts = [dict(zip(column_names, row)) for row in result]
        
        print(result_dicts)    
except Exception as e:
    print(f"An error occurred while connecting to the database: {e}")