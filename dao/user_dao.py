# user_dao.py
from datetime import datetime
class UserDAO:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def create_user(self, first_name, last_name, email, password, role):
        try:
            cursor = self.db_connection.cursor()
            query = """
            INSERT INTO User (user_id, first_name, last_name, email, password, role)
            VALUES (%s, %s, %s, %s, %s, %s)
            """

            current_date = datetime.now()
            first_part = first_name[:2].lower()
            last_part = last_name[:2].lower()
            month = current_date.strftime("%m")
            year = current_date.strftime("%y")
            user_id = f"{first_part}{last_part}{month}{year}"

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

    def enroll(self, first_name, last_name, email, course_token):
        try:
            cursor = self.db_connection.cursor()
            query = '''
            SELECT u.user_id
            FROM User u
            JOIN Student_Enrolls_ActiveCourse seac ON u.user_id = seac.user_id
            WHERE u.email = %s;
            '''
            cursor.execute(query, (email,))
            result = cursor.fetchone()
            cursor.close()

            if result:
                return True
            else:
                return False

        except Exception as e:
            print(f"Error during enrollment: {e}")
            return False



