import psycopg2
from Factorders import show_fact_orders_data

# Database connection parameters
dbname = 'DWpi'
user = 'postgres'
password = '999'
host = 'localhost'
port = '5432'

def connect_to_database():
    try:
        # Establish a connection to the PostgreSQL database
        conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        print("Connected to the database successfully!")
        return conn
    except psycopg2.Error as e:
        print(f"Unable to connect to the database: {e}")
        return None

if __name__ == "__main__":
    # Connect to the database
    connection = connect_to_database()
    
    if connection:
        # Call function to show data from FactOrders table
        show_fact_orders_data(connection)
        
        # Close the database connection
        connection.close()
