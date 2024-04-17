import sys
from main import main
from Factorders import show_fact_orders_data

if __name__ == "__main__":
    # Fetch data from the database using main() from main.py
    data = main()

    # Display data in a PyQt5 table using show_fact_orders_data from Factorders.py
    show_fact_orders_data(data)
