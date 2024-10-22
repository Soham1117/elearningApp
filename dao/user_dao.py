# user_dao.py

class UserDAO:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def create_user(self, user_id, first_name, last_name, email, password, role):
        try:
            cursor = self.db_connection.cursor()
            query = """
            INSERT INTO User (user_id, first_name, last_name, email, password, role)
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            values = (user_id, first_name, last_name, email, password, role)
            cursor.execute(query, values)
            self.db_connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print(f"Error creating user: {e}")
            return False

    def get_user_by_id(self, user_id):
        try:
            cursor = self.db_connection.cursor(dictionary=True)
            query = "SELECT * FROM User WHERE user_id = %s"
            cursor.execute(query, (user_id,))
            user = cursor.fetchone()
            cursor.close()
            return user
        except Exception as e:
            print(f"Error fetching user: {e}")
            return None

    def update_user(self, user_id, first_name, last_name, email, role):
        try:
            cursor = self.db_connection.cursor()
            query = """
            UPDATE User
            SET first_name = %s, last_name = %s, email = %s, role = %s
            WHERE user_id = %s
            """
            values = (first_name, last_name, email, role, user_id)
            cursor.execute(query, values)
            self.db_connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print(f"Error updating user: {e}")
            return False

    def delete_user(self, user_id):
        try:
            cursor = self.db_connection.cursor()
            query = "DELETE FROM User WHERE user_id = %s"
            cursor.execute(query, (user_id,))
            self.db_connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print(f"Error deleting user: {e}")
            return False

    def validate_credentials(self, role, user_id, password):
        try:
            cursor = self.db_connection.cursor()
            query = "SELECT COUNT(*) FROM User WHERE role = %s AND user_id = %s AND password = %s"
            cursor.execute(query, (role, user_id, password))
            result = cursor.fetchone()
            cursor.close()
            return result[0] > 0
        except Exception as e:
            print(f"Error validating admin credentials: {e}")
            return False

