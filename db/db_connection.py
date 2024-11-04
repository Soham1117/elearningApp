import mysql.connector

# Setup DB connection
def get_db_connection():
    return mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="Soham123!",
    database="sys"
)
