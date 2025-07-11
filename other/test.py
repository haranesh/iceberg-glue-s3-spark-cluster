#  install first pip 
# pip install trino
from trino.dbapi import connect

conn = connect(
    host='localhost',
    port=8080,
    user='trino',
    catalog='iceberg',
    schema='default', # You can set a default schema here, or change it later
    # For a local Docker setup, http_scheme is usually 'http'
    http_scheme='http' 
)

cur = conn.cursor()

# Create a schema if it doesn't exist (replace with your desired path)
# Note: If your schema already exists, you can skip this.
# try:
#     # cur.execute(f"CREATE SCHEMA iceberg.my_python_db WITH (location = 's3://testh--aps1-az1--x-s3/')")
#     cur.execute(f"CREATE SCHEMA iceberg.project_s3 WITH (location = 's3://project-s3/')")
#     print("Schema 'project_s3' created successfully (or already exists).")
# except Exception as e:
#     # Catch the specific error if schema already exists, or print for other errors
#     if "Schema 'iceberg.project_s3' already exists" in str(e):
#         print("Schema 'project_s3' already exists.")
#     else:
#         print(f"Error creating schema: {e}")

# Use the schema
cur.execute("USE iceberg.project_s3")

# Create a simple table
# cur.execute("CREATE TABLE IF NOT EXISTS iceberg.project_s3.yr2 (id INT,name VARCHAR)")
# cur.execute("""
#     CREATE TABLE iceberg.project_s3.yr2 (
#         id INT,
#         name VARCHAR
#     )
#     WITH (
#         format = 'PARQUET',
#         location = 's3://project-s3/yr2/'
#     )
# """)
# cur.execute("CREATE TABLE iceberg.project_s3.test_table (id INT,name VARCHAR)")
# # print("Table 'test_table' created successfully (or already exists).")

# # Insert data
# cur.execute("INSERT INTO iceberg.project_s3.yr2 VALUES (1, 'Alice'), (2, 'Bob')")
# # cur.execute("INSERT INTO iceberg.project_s3.yr VALUES ('Alice'), ('Bob')")
# print(f"Inserted {cur.rowcount} rows.")

# Query data
cur.execute("SELECT * FROM iceberg.project_s3.yr")
# cur.execute("SELECT * FROM iceberg.my_python_db.yr")
rows = cur.fetchall()
for row in rows:
    print(row)

cur.close()
conn.close()