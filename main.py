import psycopg2

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

def fetch_fact_orders_data(conn):
    try:
        # Create a cursor object using the connection
        cur = conn.cursor()

        # Query to select data from the FactOrders table
        query = """SELECT * FROM public."FactOrders" LIMIT 10;"""  # Adjust LIMIT as needed

        # Execute the query
        cur.execute(query)

        # Fetch all rows from the result set
        rows = cur.fetchall()

        # Close the cursor
        cur.close()

        return rows

    except psycopg2.Error as e:
        print(f"Error retrieving data from FactOrders table: {e}")
        return []

def main():
    # Connect to the database
    connection = connect_to_database()

    if connection:
        # Fetch data from FactOrders table
        data = fetch_fact_orders_data(connection)

        # Close the database connection
        connection.close()

        return data

if __name__ == "__main__":
    main()
