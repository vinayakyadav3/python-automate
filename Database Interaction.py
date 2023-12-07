import sqlite3
from sqlalchemy import create_engine
import pandas as pd

# Connect to an SQLite database
conn = sqlite3.connect('database.db')

# Execute a query
cursor = conn.cursor()
cursor.execute("SELECT * FROM table_name")
result = cursor.fetchall()

# Close the database connection
conn.close()

# Connect to a database using SQLAlchemy
engine = create_engine('database://user:password@host:port/database_name')

# Execute a query and retrieve data using Pandas
query = "SELECT * FROM table_name"
data = pd.read_sql(query, engine)
