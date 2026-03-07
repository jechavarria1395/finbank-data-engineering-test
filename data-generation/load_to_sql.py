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

# crear conexión
conn = pyodbc.connect(connection_string)
cursor = conn.cursor()

# optimización
cursor.fast_executemany = True

print("Connected to Azure SQL")

tables = [
    "dim_clientes",
    "dim_productos",
    "dim_sucursales",
    "fact_transacciones",
    "fact_creditos"
]

for table in tables:

    print(f"Loading {table}")

    df = pd.read_csv(f"{table}.csv")

    columns = ",".join(df.columns)
    values = ",".join(["?"] * len(df.columns))

    sql = f"INSERT INTO {table} ({columns}) VALUES ({values})"

    cursor.executemany(sql, df.values.tolist())

    conn.commit()

    print(f"{table} loaded")

conn.close()

print("All data loaded successfully")