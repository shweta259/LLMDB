import sqlite3

# Connect to the SQLite database (creates a new one if not existing)
conn = sqlite3.connect('tpch.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Assuming your file is named orders.tbl, change it to your file's name
file_name = "/Users/shweta/Downloads/TPC-HV3.0.1/dbgen/orders.tbl"

# Open the orders.tbl file for reading
with open(file_name, 'r') as file:
    # Read each line from the file
    for line in file:
        # Split the line into fields based on the pipe character '|'
        fields = line.strip().split('|')

        # Insert records into the ORDERS table
        cursor.execute('''
            INSERT INTO ORDERS (O_ORDERKEY, O_CUSTKEY, O_ORDERSTATUS, O_TOTALPRICE, 
            O_ORDERDATE, O_ORDERPRIORITY, O_CLERK, O_SHIPPRIORITY, O_COMMENT)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (int(fields[0]), int(fields[1]), fields[2], float(fields[3]), 
              fields[4], fields[5], fields[6], int(fields[7]), fields[8]))

# Commit the changes
conn.commit()

# Close the connection
conn.close()
