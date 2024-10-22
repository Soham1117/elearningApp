# models/user_model.py
from mysql.connector import Error

class UserModel:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def create_user(self, user_id, first_name, last_name, email, password, role):
        try:
            cursor = self.db_connection.cursor()
            sql = """
            INSERT INTO User (user_id, first_name, last_name, email, password, role)
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            values = (user_id, first_name, last_name, email, password, role)
            cursor.execute(sql, values)
            self.db_connection.commit()
            return True
        except Error as e:
            print(f"Error creating user: {e}")
            return False

    def get_user_by_id(self, user_id):
        try:
            cursor = self.db_connection.cursor(dictionary=True)
            sql = "SELECT * FROM User WHERE user_id = %s"
            cursor.execute(sql, (user_id,))
            user = cursor.fetchone()
            return user
        except Error as e:
            print(f"Error retrieving user: {e}")
            return None

    def update_user(self, user_id, first_name=None, last_name=None, email=None, password=None, role=None):
        """Update user details"""
        try:
            cursor = self.db_connection.cursor()
            updates = []
            params = []

            if first_name:
                updates.append("first_name = %s")
                params.append(first_name)
            if last_name:
                updates.append("last_name = %s")
                params.append(last_name)
            if email:
                updates.append("email = %s")
                params.append(email)
            if password:
                updates.append("password = %s")
                params.append(password)
            if role:
                updates.append("role = %s")
                params.append(role)

            params.append(user_id)
            sql = f"UPDATE User SET {', '.join(updates)}, updated_at = CURRENT_TIMESTAMP WHERE user_id = %s"
            cursor.execute(sql, tuple(params))
            self.db_connection.commit()
            return True
        except Error as e:
            print(f"Error updating user: {e}")
            return False

    def delete_user(self, user_id):
        """Delete a user from the User table"""
        try:
            cursor = self.db_connection.cursor()
            sql = "DELETE FROM User WHERE user_id = %s"
            cursor.execute(sql, (user_id,))
            self.db_connection.commit()
            return True
        except Error as e:
            print(f"Error deleting user: {e}")
            return False

    def get_all_users(self):
        """Retrieve all users from the User table"""
        try:
            cursor = self.db_connection.cursor(dictionary=True)
            sql = "SELECT * FROM User"
            cursor.execute(sql)
            users = cursor.fetchall()
            return users
        except Error as e:
            print(f"Error retrieving all users: {e}")
            return []
