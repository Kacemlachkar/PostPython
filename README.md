# FactOrders Data Viewer

This project connects to a PostgreSQL database (`DWpi`), retrieves data from the `FactOrders` table, and displays the data in a PyQt5 table widget.

## Project Structure

project_folder/
│
├── main.py
├── Factorders.py
└── fact_orders_gui.py

- `main.py`: Contains database connection and data retrieval logic.
- `Factorders.py`: Contains function to display data in a PyQt5 table.
- `fact_orders_gui.py`: Integrates database connection and GUI display.

## Requirements

- Python 3.x
- `psycopg2`: PostgreSQL adapter for Python (`pip install psycopg2`)
- `PyQt5`: Python bindings for Qt5 GUI toolkit (`pip install PyQt5`)

## Usage

1. Install the required dependencies using pip:
  pip install psycopg2 PyQt5


2. Configure Database Connection:

Update the database connection parameters (`dbname`, `user`, `password`, `host`, `port`) in `main.py` to match your PostgreSQL database settings.

3. Run the Application:

Execute `fact_orders_gui.py` to connect to the database, fetch data from the `FactOrders` table, and display it in a PyQt5 table widget:

python fact_orders_gui.py


## Troubleshooting

- If you encounter connection issues or errors related to database access, check your PostgreSQL database settings and ensure that the required packages (`psycopg2`, `PyQt5`) are installed.

- Make sure that the `FactOrders` table exists in your database (`DWpi`) and contains data for the application to fetch.





