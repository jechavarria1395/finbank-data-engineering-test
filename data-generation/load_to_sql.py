import pandas as pd
import pyodbc

server = 'finbank-sql-server-demo.database.windows.net'
database = 'finbank-sql-db'
username = 'azureadmin'
password = 'Jhonatan1395'

connection_string = f"""
Driver={{ODBC Driver 17 for SQL Server}};
Server=tcp:{server},1433;
Database={database};
Uid={username};
Pwd={password};
Encrypt=yes;
TrustServerCertificate=no;
Connection Timeout=30;
"""

conn = pyodbc.connect(connection_string)
cursor = conn.cursor()

cursor.fast_executemany = True
cursor.setinputsizes([(pyodbc.SQL_VARCHAR, 255)] * 8)

print("Connected to Azure SQL")

tables = [
    "fact_transacciones",
    "fact_creditos"
]

chunk_size = 5000

for table in tables:

    print(f"\nLoading {table}")

    columns = None
    sql = None
    total_inserted = 0

    for chunk in pd.read_csv(f"{table}.csv", chunksize=chunk_size):

        for col in chunk.columns:
            if chunk[col].dtype == "object":
                chunk[col] = chunk[col].astype(str)

        if columns is None:
            columns = ",".join(chunk.columns)
            values = ",".join(["?"] * len(chunk.columns))
            sql = f"INSERT INTO {table} ({columns}) VALUES ({values})"

        cursor.executemany(sql, chunk.values.tolist())
        conn.commit()

        total_inserted += len(chunk)

        print(f"{table}: inserted {total_inserted}")

    print(f"{table} loaded successfully")

conn.close()

print("\nAll data loaded successfully")