def show_fact_orders_data(conn):
    try:
        # Create a cursor object using the connection
        cur = conn.cursor()

        # Query to select data from the FactOrders table
        query = """SELECT * FROM public."FactOrders" LIMIT 3;"""  # Adjust LIMIT as needed

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

        # Close the cursor
        cur.close()

    except psycopg2.Error as e:
        print(f"Error retrieving data from FactOrders table: {e}")
