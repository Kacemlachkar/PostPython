import psycopg2

# Database connection parameters
dbname = 'DWpi'
user = 'postgres'
password = '999'
host = 'localhost'
port = '5432'

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

    # Create a cursor object using the connection
    cur = conn.cursor()

    # Query to select data from the FactOrders table
    query = """SELECT * FROM public."FactOrders" LIMIT 10;"""  # Adjust LIMIT as needed

    # Execute the query
    cur.execute(query)

    # Fetch all rows from the result set
    rows = cur.fetchall()

    if rows:
        print("\nData in the FactOrders table:")
        for row in rows:
            print(row)  # Print each row
    else:
        print("No data found in the FactOrders table.")

    # Close cursor and connection
    cur.close()
    conn.close()

except psycopg2.Error as e:
    print(f"Unable to connect to the database or retrieve data: {e}")
