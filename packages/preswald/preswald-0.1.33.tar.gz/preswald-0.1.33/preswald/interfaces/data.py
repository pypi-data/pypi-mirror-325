import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.sql import text as sql_text
import toml
import os
import json
from typing import Dict, Any, Optional
import logging
from preswald.interfaces.components import table
from preswald.core import get_connection

# Configure logging
logger = logging.getLogger(__name__)

def load_connection_config(config_path: str = "preswald.toml", secrets_path: str = "secrets.toml") -> Dict[str, Any]:
    """
    Load connection configuration from preswald.toml and secrets.toml.
    
    The configuration format should be:
    [data.my_connection]
    type = "postgres"  # or "mysql", "csv", "json", "parquet"
    host = "localhost"
    port = 5432
    dbname = "mydb"
    user = "user"
    # password comes from secrets.toml
    
    [data.my_csv]
    type = "csv"
    path = "data/myfile.csv"
    """
    config = {}
    
    # Load main config
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            config = toml.load(f)
    
    # Load and merge secrets
    if os.path.exists(secrets_path):
        with open(secrets_path, 'r') as f:
            secrets = toml.load(f)
            # Get connections section from secrets
            secret_connections = secrets.get('data', {})
            config_connections = config.get('data', {})
            
            # Merge secrets into each connection config
            for conn_name, conn_secrets in secret_connections.items():
                if conn_name in config_connections:
                    config_connections[conn_name].update(conn_secrets)
    
    return config.get('connections', {})

def view(data_or_connection_name, limit: int = 100):
    """
    Render a preview of the data using the table component.
    
    Args:
        data_or_connection_name: Either a pandas DataFrame or a connection name string.
        limit (int): Maximum number of rows to display in the table.
    """
    try:
        if isinstance(data_or_connection_name, pd.DataFrame):
            return table(data_or_connection_name.head(limit))
        # If it's a connection name string
        connection = get_connection(data_or_connection_name)
        
        if isinstance(connection, pd.DataFrame):
            return table(connection.head(limit))
            
        elif hasattr(connection, 'connect'):  # SQLAlchemy engine
            # Get list of tables
            with connection.connect() as conn:
                # First try to get all tables
                try:
                    query = sql_text("""
                        SELECT table_name 
                        FROM information_schema.tables 
                        WHERE table_schema = 'public'
                    """)
                    tables_df = pd.read_sql_query(query, conn)
                    
                    if len(tables_df) == 0:
                        return table([], title="No tables found in the database.")
                    
                    # Create table components for each table
                    for table_name in tables_df['table_name']:
                        query = sql_text(f"SELECT * FROM {table_name} LIMIT {limit}")
                        try:
                            table_df = pd.read_sql_query(query, conn)
                            table(table_df, title=table_name)
                        except Exception as e:
                            logger.error(f"Error fetching data from table {table_name}: {e}")
                            table([], title=f"{table_name} - Error: {str(e)}")
                    
                except Exception as e:
                    logger.error(f"Error listing tables: {e}")
                    # If we can't list tables, try a simple SELECT
                    try:
                        query = sql_text("SELECT 1")
                        test_df = pd.read_sql_query(query, conn)
                        return table([], title="Connected to database successfully, but no data to display.")
                    except Exception as e:
                        logger.error(f"Error testing connection: {e}")
                        return table([], title=f"Error connecting to database: {str(e)}")
        else:
            raise TypeError(f"Input does not contain viewable data")
    except Exception as e:
        logger.error(f"Error viewing data: {e}")
        return table([], title=f"Error: {str(e)}")

def query(connection_name: str, sql_query: str) -> pd.DataFrame:
    """
    Execute a SQL query on a database connection and return the result as a DataFrame.
    
    Args:
        connection_name (str): The name of the database connection.
        sql_query (str): The SQL query to execute.
    Returns:
        pd.DataFrame: Query results as a pandas DataFrame.
    """
    connection = get_connection(connection_name)
    
    if not hasattr(connection, 'connect'):
        raise TypeError(f"Connection '{connection_name}' is not a database connection")
    
    try:
        with connection.connect() as conn:
            # Convert the query string to a SQLAlchemy text object
            query_obj = sql_text(sql_query)
            return pd.read_sql_query(query_obj, conn)
    except Exception as e:
        logger.error(f"Error executing query on '{connection_name}': {e}")
        raise

def summary(connection_name: str):
    """
    Generate a summary of the data from a connection.
    
    Args:
        connection_name (str): The name of the data connection.
    Returns:
        dict: Table component containing the data summary.
    """
    connection = get_connection(connection_name)
    
    if isinstance(connection, pd.DataFrame):
        summary_df = connection.describe(include='all')
        return table(summary_df, title="Data Summary")
    else:
        raise TypeError(f"Connection '{connection_name}' does not contain tabular data")

def save(connection_name: str, file_path: str, format: str = "csv") -> str:
    """
    Save data from a connection to a file.
    
    Args:
        connection_name (str): The name of the data connection.
        file_path (str): Path to save the file.
        format (str): Format to save the data in ('csv', 'json', 'parquet').
    Returns:
        str: Success message.
    """
    connection = get_connection(connection_name)
    
    if not isinstance(connection, pd.DataFrame):
        raise TypeError(f"Connection '{connection_name}' does not contain tabular data")
    
    try:
        if format == "csv":
            connection.to_csv(file_path, index=False)
        elif format == "json":
            connection.to_json(file_path, orient="records")
        elif format == "parquet":
            connection.to_parquet(file_path, index=False)
        else:
            raise ValueError(f"Unsupported format: {format}")
        
        return f"Data saved to {file_path} in {format} format"
    except Exception as e:
        logger.error(f"Error saving data from '{connection_name}' to {file_path}: {e}")
        raise
