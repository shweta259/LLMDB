import sqlite3

# Connect to the SQLite database (creates a new one if not existing)
conn = sqlite3.connect('tpch.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Open the part.tbl file for reading
file_name = "/Users/shweta/Downloads/TPC-HV3.0.1/dbgen/part.tbl"
with open(file_name, 'r') as file:
    # Iterate over each line in the file
    for line in file:
        # Split the line by '|'
        data = line.strip().split('|')
        
        # Insert data into the table
        cursor.execute('''
            INSERT INTO part (P_PARTKEY, P_NAME, P_MFGR, P_BRAND, P_TYPE, P_SIZE, P_CONTAINER, P_RETAILPRICE, P_COMMENT)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (int(data[0]), data[1], data[2], data[3], data[4], int(data[5]), data[6], float(data[7]), data[8]))

# Commit the changes
conn.commit()

# Close the connection
conn.close()
