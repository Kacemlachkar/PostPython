from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem
import sys

def show_fact_orders_data(data):
    # Create the application
    app = QApplication(sys.argv)

    # Create the main window
    window = QMainWindow()
    window.setWindowTitle("FactOrders Data")

    # Create a table widget
    tableWidget = QTableWidget()
    window.setCentralWidget(tableWidget)

    # Set row and column count based on data
    tableWidget.setRowCount(len(data))
    tableWidget.setColumnCount(len(data[0]))  # Assuming all rows have same number of columns

    # Populate the table with data
    for row_idx, row_data in enumerate(data):
        for col_idx, cell_data in enumerate(row_data):
            item = QTableWidgetItem(str(cell_data))
            tableWidget.setItem(row_idx, col_idx, item)

    # Auto-adjust column widths
    tableWidget.resizeColumnsToContents()

    # Show the main window
    window.show()

    # Execute the application
    sys.exit(app.exec_())
