from datetime import datetime
class UserDAO:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def create_faculty(self, first_name, last_name, email, password):
        try:
            cursor = self.db_connection.cursor()
            query = """
            INSERT INTO Faculty (faculty_id, first_name, last_name, email, password, created_at, updated_at)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """

            current_date = datetime.now()
            created_at = current_date.strftime("%Y-%m-%d %H:%M:%S")
            updated_at = current_date.strftime("%Y-%m-%d %H:%M:%S")
            first_part = first_name[:2].lower()
            last_part = last_name[:2].lower()
            month = current_date.strftime("%m")
            year = current_date.strftime("%y")
            faculty_id = f"{first_part}{last_part}{month}{year}"

            values = (faculty_id, first_name, last_name, email, password, created_at, updated_at)
            cursor.execute(query, values)
            self.db_connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print(f"Error creating user: {e}")
            return False
    
    def create_student(self, first_name, last_name, email, password):
        try:
            cursor = self.db_connection.cursor()
            query = """
            INSERT INTO Student (student_id, full_name, email, password, created_at, updated_at)
            VALUES (%s, %s, %s, %s, %s, %s)
            """

            current_date = datetime.now()
            first_part = first_name[:1].upper() + first_name[1:2].lower()
            last_part = last_name[:1].upper() + last_name[1:2].lower()
            month = current_date.strftime("%m")
            year = current_date.strftime("%y")

            student_id = f"{first_part}{last_part}{month}{year}"
            full_name = first_name + " " + last_name
            created_at = current_date.strftime("%Y-%m-%d %H:%M:%S")
            updated_at = current_date.strftime("%Y-%m-%d %H:%M:%S")

            values = (student_id, full_name, email, password, created_at, updated_at)
            cursor.execute(query, values)
            self.db_connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print(f"Error creating user: {e}")
            return False

    def create_ta(self, first_name, last_name, email, password, course_id, faculty_id):
        try:
            cursor = self.db_connection.cursor()
            query = """
            INSERT INTO TA (ta_id, first_name, last_name, email, password, course_id, faculty_id, created_at, updated_at)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """

            current_date = datetime.now()
            created_at = current_date.strftime("%Y-%m-%d %H:%M:%S")
            updated_at = current_date.strftime("%Y-%m-%d %H:%M:%S")
            first_part = first_name[:1].upper() + first_name[1:2].lower()
            last_part = last_name[:1].upper() + last_name[1:2].lower()
            month = current_date.strftime("%m")
            year = current_date.strftime("%y")
            ta_id = f"{first_part}{last_part}{month}{year}"

            values = (ta_id, first_name, last_name, email, password, course_id, faculty_id, created_at, updated_at)
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

    def validate_credentials(self, user_id, password):
        try:
            cursor = self.db_connection.cursor()
            query = "SELECT COUNT(*) FROM User WHERE user_id = %s AND password = %s"
            cursor.execute(query, (user_id, password))
            result = cursor.fetchone()
            cursor.close()
            return result[0] > 0
        except Exception as e:
            print(f"Error validating admin credentials: {e}")
            return False
			
    def validate_credentials_ta(self, ta_id, password):
        try:
            cursor = self.db_connection.cursor()
            query = "SELECT COUNT(*) FROM TA WHERE ta_id = %s AND password = %s"
            cursor.execute(query, (ta_id, password))
            result = cursor.fetchone()
            cursor.close()
            return result[0] > 0
        except Exception as e:
            print(f"Error validating TA credentials: {e}")
            return False
        
    def change_password_ta(self, ta_id, old_password, new_password):
        try:
            cursor = self.db_connection.cursor()
            query = "SELECT COUNT(*) FROM TA WHERE ta_id = %s AND password = %s"
            cursor.execute(query, (ta_id, old_password))
            result = cursor.fetchone()
            cursor.close()

            # query to check if old password matches
            if not result[0] > 0:
                return False
            
            # query to update password
            cursor = self.db_connection.cursor()
            query = "UPDATE TA SET password = %s WHERE ta_id = %s"
            cursor.execute(query, (new_password, ta_id))
            self.db_connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print(f"Error validating TA credentials: {e}")
            return False

    def view_courses_ta(self, ta_id):
        try:
            cursor = self.db_connection.cursor()
            query = "SELECT * FROM Course WHERE ta_id = %s"
            cursor.execute(query, (ta_id,))
            result = cursor.fetchall()
            cursor.close()

            # print(result)
            return result, True
        except Exception as e:
            print(f"Error validating ta credentials: {e}")
            return e, False
			
    def validate_faculty_credentials(self, faculty_id, password):
        try:
            cursor = self.db_connection.cursor()
            query = "SELECT COUNT(*) FROM Faculty WHERE faculty_id = %s AND password = %s"
            cursor.execute(query, (faculty_id, password))
            result = cursor.fetchone()
            cursor.close()
            return result[0] > 0
        except Exception as e:
            print(f"Error validating faculty credentials: {e}")
            return False
        
    def validate_student_credentials(self, student_id, password):
        try:
            cursor = self.db_connection.cursor()
            query = "SELECT * FROM Student WHERE student_id = %s AND password = %s"
            cursor.execute(query, (student_id, password))
            result = cursor.fetchone()
            cursor.close()
            return result
        except Exception as e:
            print(f"Error validating faculty credentials: {e}")
            return False
        
    def change_faculty_password(self, faculty_id, old_password, new_password):
        try:
            cursor = self.db_connection.cursor()
            query = "SELECT COUNT(*) FROM Faculty WHERE faculty_id = %s AND password = %s"
            cursor.execute(query, (faculty_id, old_password))
            result = cursor.fetchone()
            cursor.close()

            # query to check if old password matches
            if not result[0] > 0:
                return False
            
            # query to update password
            cursor = self.db_connection.cursor()
            query = "UPDATE Faculty SET password = %s WHERE faculty_id = %s"
            cursor.execute(query, (new_password, faculty_id))
            self.db_connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print(f"Error validating admin credentials: {e}")
            return False
        
    def view_faculty_courses(self, faculty_id):
        try:
            cursor = self.db_connection.cursor()
            query = "SELECT * FROM Course WHERE faculty_id = %s"
            cursor.execute(query, (faculty_id,))
            result = cursor.fetchall()
            cursor.close()

            # print(result)
            return result, True
        except Exception as e:
            print(f"Error validating admin credentials: {e}")
            return e, False
    
    def get_course_by_course_id(self, course_id):
        try:
            # cursor = self.db_connection.cursor(dictionary=True)
            cursor = self.db_connection.cursor()
            query = "SELECT course_name FROM Course WHERE course_id = %s"
            cursor.execute(query, (course_id,))
            course = cursor.fetchone()
            cursor.close()
            return course
        except Exception as e:
            print(f"Error fetching course: {e}")
            return None
        
    def get_course_type_by_course_id(self, course_id):
        try:
            # cursor = self.db_connection.cursor(dictionary=True)
            cursor = self.db_connection.cursor()
            query = "SELECT course_type FROM Course WHERE course_id = %s"
            cursor.execute(query, (course_id,))
            courseType = cursor.fetchone()
            cursor.close()
            return courseType
        except Exception as e:
            print(f"Error fetching course: {e}")
            return None
    
    def get_student_by_student_id(self, student_id):
        try:
            # cursor = self.db_connection.cursor(dictionary=True)
            cursor = self.db_connection.cursor()
            query = "SELECT * FROM Student WHERE student_id = %s"
            cursor.execute(query, (student_id,))
            student = cursor.fetchone()
            cursor.close()
            return student
        except Exception as e:
            print(f"Error fetching course: {e}")
            return None
    
    def get_students_by_course_id(self, course_id):
        try:
            # cursor = self.db_connection.cursor(dictionary=True)
            # query = "SELECT course_name FROM Course WHERE course_id = %s"
            cursor = self.db_connection.cursor()
            query = """
                SELECT student_id, full_name, email
                FROM student
                WHERE student_id IN (
                    SELECT student_id
                    FROM Student_Enrolls_Course
                    WHERE course_id = %s AND status = 'Enrolled'
                )
            """
            cursor.execute(query, (course_id,))
            students = cursor.fetchall()
            cursor.close()
            return students
        except Exception as e:
            print(f"Error fetching course: {e}")
            return None


    def get_textbook_by_course_id(self, course_id):
        try:
            cursor = self.db_connection.cursor()
            query = "SELECT textbook_id FROM Course WHERE course_id = %s"
            cursor.execute(query, (course_id,))
            textbook_id = cursor.fetchone()
            cursor.close()
            return textbook_id
        except Exception as e:
            print(f"Error fetching textbook: {e}")
            return None
	
    # get the waiting list of students for a course
    # Faculty: View Worklist
    def get_faculty_worklist_by_course_id(self, course_id):
        try:
            # cursor = self.db_connection.cursor(dictionary=True)
            # query = "SELECT course_name FROM Course WHERE course_id = %s"
            cursor = self.db_connection.cursor()
            query = """
                SELECT s.student_id, s.full_name, s.email, e.status
                FROM Student s
                JOIN Student_Enrolls_Course e ON s.student_id = e.student_id
                WHERE e.course_ID = %s AND e.status = 'Pending';
            """
            cursor.execute(query, (course_id,))
            students = cursor.fetchall()
            cursor.close()
            return students
        except Exception as e:
            print(f"Error fetching course: {e}")
            return None
        
    # Faculty: Approve Enrollment
    # Check if student is already enrolled in the course
    def get_enrollment_by_student_id_and_course_id(self, student_id, course_id):
        try:
            cursor = self.db_connection.cursor()
            query = "SELECT * FROM Student_Enrolls_Course WHERE student_id = %s AND course_id = %s AND status = 'Enrolled'"
            cursor.execute(query, (student_id, course_id))
            enrollment = cursor.fetchone()
            cursor.close()
            return enrollment
        except Exception as e:
            print(f"Error fetching course: {e}")
            return None

    # Faculty: Approve Enrollment
    # Check if student is already enrolled in the course
    def approve_enrollment(self, student_id, course_id):
        try:
            cursor = self.db_connection.cursor()
            query = "UPDATE Student_Enrolls_Course SET status = 'Enrolled' WHERE student_id = %s AND course_id = %s"
            cursor.execute(query, (student_id, course_id))
            self.db_connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print(f"Error approving enrollment: {e}")
            return False

    def add_new_etextbook(self, title, etextbook_id):
        try:
            cursor = self.db_connection.cursor()
            query = "INSERT INTO Textbook  (textbook_id, title) VALUES (%s, %s)"
            cursor.execute(query, (etextbook_id, title))
            self.db_connection.commit()
            cursor.close()
            return True, "Textbook added successfully"
        except Exception as e:
            print(f"Error adding new textbook: {e}")
            return False, e

    def hide_content_block(self, textbook_id, chapter_id, section_id, block_id):
            try:
                cursor = self.db_connection.cursor()
                
                # Check if the block is already hidden
                check_query = """
                    SELECT hidden FROM Blocks
                    WHERE textbook_id = %s AND chapter_id = %s AND section_id = %s AND block_id = %s
                """
                cursor.execute(check_query, (textbook_id, chapter_id, section_id, block_id))
                
                block = cursor.fetchone()
                
                if block:
                    # Toggle hidden status
                    hidden = block[0]
                    new_value = 'no' if hidden == 'yes' else 'yes'
                    
                    # Update hidden status
                    current_date = datetime.now()
                    updated_at = current_date.strftime("%Y-%m-%d %H:%M:%S")
                    update_query = """
                        UPDATE Blocks
                        SET hidden = %s, updated_at = %s
                        WHERE textbook_id = %s AND chapter_id = %s AND section_id = %s AND block_id = %s
                    """
                    cursor.execute(update_query, (new_value, updated_at, textbook_id, chapter_id, section_id, block_id))
                    
                    self.db_connection.commit()
                    cursor.close()
                    
                    return True, "Block hidden status updated successfully"
                else:
                    cursor.close()
                    return False, "Block not found"
            except Exception as e:
                print(f"Error updating block hidden status: {e}")
                return False, e
            
    def delete_content_block(self, textbook_id, chapter_id, section_id, block_id):
        try:
            cursor = self.db_connection.cursor()
            query = """
                DELETE FROM Blocks
                WHERE textbook_id = %s AND chapter_id = %s AND section_id = %s AND block_id = %s
            """
            cursor.execute(query, (textbook_id, chapter_id, section_id, block_id))
            
            # Commit the deletion
            self.db_connection.commit()
            cursor.close()
            return True, "Block deleted successfully"
        except Exception as e:
            print(f"Error deleting block: {e}")
            return False, e
    def add_new_chapter(self, textbook_id, chapter_id, chapter_title):
        try:
            cursor = self.db_connection.cursor()
            current_date = datetime.now()
            created_at = current_date.strftime("%Y-%m-%d %H:%M:%S")
            updated_at = current_date.strftime("%Y-%m-%d %H:%M:%S")
            query = "INSERT INTO Chapter (textbook_id, chapter_id, title, created_at, updated_at) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, (textbook_id, chapter_id, chapter_title, created_at, updated_at))
            self.db_connection.commit()
            cursor.close()
            return True, "Textbook added successfully"
        except Exception as e:
            print(f"Error adding new textbook: {e}")
            return False, e
    
    def add_new_content_block(self, textbook_id, chapter_id, section_id, section_title):
        try:
            cursor = self.db_connection.cursor()
            current_date = datetime.now()
            created_at = current_date.strftime("%Y-%m-%d %H:%M:%S")
            updated_at = current_date.strftime("%Y-%m-%d %H:%M:%S")
            query = "INSERT INTO Section (textbook_id, chapter_id, section_id, title, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (textbook_id, chapter_id, section_id, section_title, created_at, updated_at))
            self.db_connection.commit()
            cursor.close()
            return True, "Textbook added successfully"
        except Exception as e:
            print(f"Error adding new textbook: {e}")
            return False, e
	    
    def add_new_section(self, textbook_id, chapter_id, section_id, section_title):
        try:
            cursor = self.db_connection.cursor()
            current_date = datetime.now()
            created_at = current_date.strftime("%Y-%m-%d %H:%M:%S")
            updated_at = current_date.strftime("%Y-%m-%d %H:%M:%S")
            query = "INSERT INTO Section (textbook_id, chapter_id, section_id, title, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (textbook_id, chapter_id, section_id, section_title, created_at, updated_at))
            self.db_connection.commit()
            cursor.close()
            return True, "Textbook added successfully"
        except Exception as e:
            print(f"Error adding new textbook: {e}")
            return False, e
    
    def add_new_text(self, textbook_id, chapter_id, section_id, block_id, text):
        try:
            cursor = self.db_connection.cursor()
            current_date = datetime.now()
            created_at = current_date.strftime("%Y-%m-%d %H:%M:%S")
            updated_at = current_date.strftime("%Y-%m-%d %H:%M:%S")
            type_of_block = "text"
            hidden = "no"
            query = "INSERT INTO Blocks (textbook_id, chapter_id, section_id, block_id, type_of_block, content, hidden, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (textbook_id, chapter_id, section_id, block_id, type_of_block, text, hidden, created_at, updated_at))
            self.db_connection.commit()
            cursor.close()
            return True, "Text added successfully"
        except Exception as e:
            print(f"Error adding new textbook: {e}")
            return False, e

    def add_new_picture(self, textbook_id, chapter_id, section_id, block_id, content):
        try:
            cursor = self.db_connection.cursor()
            current_date = datetime.now()
            created_at = current_date.strftime("%Y-%m-%d %H:%M:%S")
            updated_at = current_date.strftime("%Y-%m-%d %H:%M:%S")
            type_of_block = "picture"
            hidden = "no"
            query = "INSERT INTO Blocks (textbook_id, chapter_id, section_id, block_id, type_of_block, content, hidden, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (textbook_id, chapter_id, section_id, block_id, type_of_block, content, hidden, created_at, updated_at))
            self.db_connection.commit()
            cursor.close()
            return True, "Text added successfully"
        except Exception as e:
            print(f"Error adding new textbook: {e}")
            return False, e

    def add_question(self, textbook_id, chapter_id, section_id, block_id, unique_activity_id, qa):
        try:
            cursor = self.db_connection.cursor()
            question_id = qa[0]
            question_text = qa[1]
            option1_text = qa[2]
            option1_explanation = qa[3]
            option2_text = qa[4]
            option2_explanation = qa[5]
            option3_text = qa[6]
            option3_explanation = qa[7]
            option4_text = qa[8]
            option4_explanation = qa[9]
            answer = qa[10]
            
            query = "INSERT INTO Question (textbook_id, chapter_id, section_id, block_id, unique_activity_id, question_id, question_text, option_1, explanation_1, option_2, explanation_2, option_3, explanation_3, option_4, explanation_4, answer) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (textbook_id, chapter_id, section_id, block_id, unique_activity_id, question_id, question_text, option1_text, option1_explanation, option2_text, option2_explanation, option3_text, option3_explanation, option4_text, option4_explanation, answer))
            self.db_connection.commit()
            cursor.close()            
            return True, "Question added successfully"  
        except Exception as e:  
            print(f"Error adding new question: {e}")
            return False, e
        
    
    def add_activity(self, textbook_id, chapter_id, section_id, block_id, unique_activity_id):
        try:
            cursor = self.db_connection.cursor()
            current_date = datetime.now()
            created_at = current_date.strftime("%Y-%m-%d %H:%M:%S")
            updated_at = current_date.strftime("%Y-%m-%d %H:%M:%S")
            hidden = "no"
            query = "INSERT INTO Activity (textbook_id, chapter_id, section_id, block_id, unique_activity_id, hidden, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (textbook_id, chapter_id, section_id, block_id, unique_activity_id, hidden, created_at, updated_at))
            self.db_connection.commit()
            cursor.close()
            return True, "Activity added successfully"
        except Exception as e:
            print(f"Error adding new activity: {e}")
            return False, e 
        
    def add_activityBlock(self, textbook_id, chapter_id, section_id, block_id, unique_activity_id):
        try:
            cursor = self.db_connection.cursor()
            current_date = datetime.now()
            created_at = current_date.strftime("%Y-%m-%d %H:%M:%S")
            updated_at = current_date.strftime("%Y-%m-%d %H:%M:%S")
            hidden = "no"
            content = unique_activity_id
            type_of_block = "activity"
            query = "INSERT INTO Blocks (textbook_id, chapter_id, section_id, block_id, type_of_block, content, hidden, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (textbook_id, chapter_id, section_id, block_id, type_of_block, content, hidden, created_at, updated_at))
            self.db_connection.commit()
            cursor.close()
            return True, "Activity block added successfully"
        except Exception as e:
            print(f"Error adding new activity block: {e}")
            return False, e 
    
    def checkTextbook(self, etextbook_id):
        try:
            cursor = self.db_connection.cursor()
            query = "SELECT * FROM Textbook WHERE textbook_id = %s"
            cursor.execute(query, (etextbook_id,))
            textbook = cursor.fetchone()
            cursor.close()
            if textbook:
                return True 
            else:
                return False
        except Exception as e:
            print(f"Error checking textbook: {e}")
            return False
    
    def checkChapter(self, textbook_id, chapter_id):
        try:
            cursor = self.db_connection.cursor()
            query = "SELECT * FROM Chapter WHERE textbook_id = %s AND chapter_id = %s"
            cursor.execute(query, (textbook_id, chapter_id,))
            chapter = cursor.fetchone()
            cursor.close()
            if chapter:
                return True
            else:
                return False
        except Exception as e:
            print(f"Error checking chapter: {e}")
            return False

    def checkSection(self, textbook_id, chapter_id, section_id):
        try:
            cursor = self.db_connection.cursor()
            query = "SELECT * FROM Section WHERE textbook_id = %s AND chapter_id = %s AND section_id = %s"
            cursor.execute(query, (textbook_id, chapter_id, section_id,))
            section = cursor.fetchone()
            cursor.close()
            if section:
                return True 
            else:
                return False
        except Exception as e:
            print(f"Error checking section: {e}")
            return False        
    
    def checkBlock(self, textbook_id, chapter_id, section_id, block_id):
        try:
            cursor = self.db_connection.cursor()
            query = "SELECT * FROM Blocks WHERE textbook_id = %s AND chapter_id = %s AND section_id = %s AND block_id = %s"
            cursor.execute(query, (textbook_id, chapter_id, section_id, block_id,))
            block = cursor.fetchone()
            cursor.close()
            if block:
                return True 
            else:
                return False
        except Exception as e:
            print(f"Error checking block: {e}")
            return False  
    
    def checkFaculty(self, faculty_id):
        try:
            cursor = self.db_connection.cursor()
            query = "SELECT * FROM Faculty WHERE faculty_id = %s"
            cursor.execute(query, (faculty_id,))
            textbook = cursor.fetchone()
            cursor.close()
            if textbook:
                return True 
            else:
                return False
        except Exception as e:
            print(f"Error checking faculty: {e}")
            return False  
    
    def add_active_course(self, course_id, course_name, etextbook_id, course_start_date, course_end_date, unique_token, course_capacity, faculty_id):
        try:
            cursor = self.db_connection.cursor()    
            current_date = datetime.now()           
            created_at = current_date.strftime("%Y-%m-%d %H:%M:%S")
            updated_at = current_date.strftime("%Y-%m-%d %H:%M:%S")
            course_type = "Active"
            query = "INSERT INTO Course (course_id, course_name, textbook_id, course_type, faculty_id, ta_id, start_date, end_date, unique_token, capacity, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (course_id, course_name, etextbook_id, course_type, faculty_id, None, course_start_date, course_end_date, unique_token, course_capacity, created_at, updated_at))
            self.db_connection.commit()
            cursor.close()
            return True, "Active Course added successfully"
        except Exception as e:
            print(f"Error adding active course: {e}")
            return False, e
    
    def add_evaluation_course(self, course_id, course_name, etextbook_id, course_start_date, course_end_date, faculty_id):
        try:
            cursor = self.db_connection.cursor()    
            current_date = datetime.now()           
            created_at = current_date.strftime("%Y-%m-%d %H:%M:%S")
            updated_at = current_date.strftime("%Y-%m-%d %H:%M:%S")
            course_type = "Evaluation"
            query = "INSERT INTO Course (course_id, course_name, textbook_id, course_type, faculty_id, ta_id, start_date, end_date, unique_token, capacity, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (course_id, course_name, etextbook_id, course_type, faculty_id, None, course_start_date, course_end_date, None, None, created_at, updated_at))
            self.db_connection.commit()
            cursor.close()
            return True, "Evaluation Course added successfully"
        except Exception as e:
            print(f"Error adding evaluation course: {e}")
            return False, e

    def hide_section(self, textbook_id, chapter_id, section_id):
        def check_section_is_hidden(textbook_id, chapter_id, section_id):
            try:
                cursor = self.db_connection.cursor()
                query = """
                    SELECT hidden FROM Section
                    WHERE textbook_id = %s AND chapter_id = %s AND section_id = %s
                """
                cursor.execute(query, (textbook_id, chapter_id, section_id))
                
                section = cursor.fetchone()
                cursor.close()
                
                if section:
                    hidden = section[0]  
                    print(hidden,'Hidden value')
                    return True, hidden
                else:
                    return False, None 
            except Exception as e:
                print(f"Error checking section: {e}")
                return False, e
                
        try:
            response, hidden_status = check_section_is_hidden(textbook_id, chapter_id, section_id)
            if response and hidden_status == 'yes':
                new_value = 'no'
            else:
                new_value = 'yes'    
            
            cursor = self.db_connection.cursor()
            current_date = datetime.now()
            updated_at = current_date.strftime("%Y-%m-%d %H:%M:%S")
            query = """
                UPDATE Section
                SET hidden = %s, updated_at = %s
                WHERE textbook_id = %s AND chapter_id = %s AND section_id = %s
            """
            cursor.execute(query, (new_value, updated_at, textbook_id, chapter_id, section_id))
            
            self.db_connection.commit()
            cursor.close()
            return True, "Section hidden status updated successfully"
        except Exception as e:
            print(f"Error updating section hidden status: {e}")
            return False, e


    def delete_section(self, textbook_id, chapter_id, section_id):
        cursor = self.db_connection.cursor()
        try:
            
            print(textbook_id,section_id,chapter_id,'in delete section')
            query = """
                DELETE FROM Section
                WHERE textbook_id = %s AND chapter_id = %s AND section_id = %s
            """
            cursor.execute(query, (textbook_id, chapter_id, section_id))
            
            # Commit the deletion
            self.db_connection.commit()
            cursor.close()
            
            return True, "Section deleted successfully"
        except Exception as e:
            cursor.close()
            print(f"Error deleting section: {e}")
            return False, e


    def delete_content_block(self, textbook_id, chapter_id, section_id, block_id):
        cursor = self.db_connection.cursor()
        try:
            
            print(textbook_id,chapter_id,section_id,block_id)
            query = """
                DELETE FROM Blocks
                WHERE textbook_id = %s AND chapter_id = %s AND section_id = %s AND block_id = %s
            """
            cursor.execute(query, (textbook_id, chapter_id, section_id, block_id))
            
            # Commit the deletion
            self.db_connection.commit()
            cursor.close()
            
            return True, "Block deleted successfully"
        except Exception as e:
            cursor.close()
            print(f"Error deleting block: {e}")
            return False, e

    
    def hide_content_block(self, textbook_id, chapter_id, section_id, block_id):
        try:
            cursor = self.db_connection.cursor()
            
            # Check if the block is already hidden
            check_query = """
                SELECT hidden FROM Blocks
                WHERE textbook_id = %s AND chapter_id = %s AND section_id = %s AND block_id = %s
            """
            cursor.execute(check_query, (textbook_id, chapter_id, section_id, block_id))
            
            block = cursor.fetchone()
            
            if block:
                # Toggle hidden status
                hidden = block[0]
                print(hidden,'Hidden value')
                new_value = 'no' if hidden == 'yes' else 'yes'
                
                # Update hidden status
                current_date = datetime.now()
                updated_at = current_date.strftime("%Y-%m-%d %H:%M:%S")
                update_query = """
                    UPDATE Blocks
                    SET hidden = %s, updated_at = %s
                    WHERE textbook_id = %s AND chapter_id = %s AND section_id = %s AND block_id = %s
                """
                cursor.execute(update_query, (new_value, updated_at, textbook_id, chapter_id, section_id, block_id))
                
                self.db_connection.commit()
                cursor.close()
                
                return True, "Block hidden status updated successfully"
            else:
                cursor.close()
                return False, "Block not found"
        except Exception as e:
            print(f"Error updating block hidden status: {e}")
            return False, e 

    def hide_chapter(self, textbook_id, chapter_id):
        def check_chapter_is_hidden(textbook_id, chapter_id):
            try:
                cursor = self.db_connection.cursor()
                query = """
                    SELECT hidden FROM Chapter
                    WHERE textbook_id = %s AND chapter_id = %s
                """
                cursor.execute(query, (textbook_id, chapter_id))
                
                chapter = cursor.fetchone()
                cursor.close()
                
                if chapter:
                    hidden = chapter[0]  
                    return True, hidden
                else:
                    return False, None 
            except Exception as e:
                print(f"Error checking chapter: {e}")
                return False, e
                
        try:
            response, hidden_status = check_chapter_is_hidden(textbook_id, chapter_id)
            if response and hidden_status == 'yes':
                new_value = 'no'
            else:
                new_value = 'yes'    
            
            cursor = self.db_connection.cursor()
            current_date = datetime.now()
            updated_at = current_date.strftime("%Y-%m-%d %H:%M:%S")
            query = """
                UPDATE Chapter
                SET hidden = %s, updated_at = %s
                WHERE textbook_id = %s AND chapter_id = %s
            """
            cursor.execute(query, (new_value, updated_at, textbook_id, chapter_id))
            
            self.db_connection.commit()
            cursor.close()
            return True, "Chapter hidden status updated successfully"
        except Exception as e:
            print(f"Error updating chapter hidden status: {e}")
            return False, e


    def delete_chapter(self, textbook_id, chapter_id):
        cursor = self.db_connection.cursor()
        try:
            
            query = """
                DELETE FROM Chapter
                WHERE textbook_id = %s AND chapter_id = %s
            """
            cursor.execute(query, (textbook_id, chapter_id))
            
            # Commit the deletion
            self.db_connection.commit()
            cursor.close()
            
            return True, "Chapter deleted successfully"
        except Exception as e:
            cursor.close()
            print(f"Error deleting chapter: {e}")
            return False, e

    def delete_activity(self, textbook_id, chapter_id, section_id, block_id, unique_activity_id):
        cursor = self.db_connection.cursor()
        try:
            
            query = """
                DELETE FROM Activity
                WHERE textbook_id = %s AND chapter_id = %s AND section_id = %s AND block_id = %s AND unique_activity_id = %s
            """
            cursor.execute(query, (textbook_id, chapter_id, section_id, block_id, unique_activity_id))
            
            # Commit the deletion
            self.db_connection.commit()
            cursor.close()
            
            return True, "Activity deleted successfully"
        except Exception as e:
            cursor.close()
            print(f"Error deleting activity: {e}")
            return False, e        
       
    def hide_activity(self, textbook_id, chapter_id, section_id, block_id, unique_activity_id):
        def check_activity_is_hidden(textbook_id, chapter_id, section_id, block_id, unique_activity_id):
            try:
                cursor = self.db_connection.cursor()
                query = """
                    SELECT hidden FROM Activity
                    WHERE textbook_id = %s AND chapter_id = %s AND section_id = %s 
                        AND block_id = %s AND unique_activity_id = %s
                """
                cursor.execute(query, (textbook_id, chapter_id, section_id, block_id, unique_activity_id))
                
                activity = cursor.fetchone()
                cursor.close()
                
                if activity:
                    hidden = activity[0]
                    return True, hidden
                else:
                    return False, None
            except Exception as e:
                print(f"Error checking activity: {e}")
                return False, e
                
        try:
            response, hidden_status = check_activity_is_hidden(textbook_id, chapter_id, section_id, block_id, unique_activity_id)
            if response and hidden_status == 'yes':
                new_value = 'no'
            else:
                new_value = 'yes'
            
            cursor = self.db_connection.cursor()
            current_date = datetime.now()
            updated_at = current_date.strftime("%Y-%m-%d %H:%M:%S")
            query = """
                UPDATE Activity
                SET hidden = %s, updated_at = %s
                WHERE textbook_id = %s AND chapter_id = %s AND section_id = %s 
                    AND block_id = %s AND unique_activity_id = %s
            """
            cursor.execute(query, (new_value, updated_at, textbook_id, chapter_id, section_id, block_id, unique_activity_id))
            
            self.db_connection.commit()
            cursor.close()
            return True, "Activity hidden status updated successfully"
        except Exception as e:
            print(f"Error updating activity hidden status: {e}")
            return False, e
        
    
    ## STUDENT RELATED QUERIES ##

    def is_valid_active_course_token(self, course_token):
        try:
            cursor = self.db_connection.cursor()
            query = "SELECT * FROM Course WHERE unique_token = %s AND course_type = 'Active'"
            cursor.execute(query, (course_token,))
            result = cursor.fetchone()
            cursor.close()
            if result:
                return True
            else:
                return False
        except Exception as e:
            print(f"Error during enrollment: {e}")
            return False
        
    def check_student_in_enrolls(self, first_name, last_name, email):
        try:
            cursor = self.db_connection.cursor()
            query = "SELECT * FROM Student WHERE full_name = %s AND email = %s"
            cursor.execute(query, (first_name + " " + last_name, email,))
            result = cursor.fetchone()
            cursor.close()
            if result:
                return True, True
            else:
                return True, False
        except Exception as e:
            print(f"Error during enrollment: {e}")
            return False, False

    def enroll(self, first_name, last_name, email, course_token):
        try:
            cursor = self.db_connection.cursor()

            # Get student_id
            query = "SELECT student_id FROM Student WHERE full_name = %s AND email = %s"
            cursor.execute(query, (first_name + " " + last_name, email,))
            student_id = cursor.fetchone()[0]

            # Get course_id
            query = "SELECT course_id FROM Course WHERE unique_token = %s AND course_type = 'Active'"
            cursor.execute(query, (course_token,))
            course_id = cursor.fetchone()[0]

            if not student_id or not course_id:
                cursor.close()
                return False

            current_date = datetime.now()           
            created_at = current_date.strftime("%Y-%m-%d %H:%M:%S")
            updated_at = current_date.strftime("%Y-%m-%d %H:%M:%S")

            # Enroll student in course
            query = '''
                INSERT INTO Student_Enrolls_Course
                (student_id, course_id, status, created_at, updated_at)
                VALUES  (%s, %s, %s, %s, %s)
            '''
            cursor.execute(query, (student_id, course_id, "Pending", created_at, updated_at,))
            self.db_connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print(f"Error during enrollment: {e}")
            return False
        
    # Student: View Participation Activity Points
    def view_student_participation_activity_points_by_course(self, student_id):
        try:
            cursor = self.db_connection.cursor()
            query = """
                SELECT *
                FROM Student_Overall_Score
                WHERE student_id = %s;
            """
            cursor.execute(query, (student_id,))
            students = cursor.fetchall()
            cursor.close()
            return students
        except Exception as e:
            print(f"Error fetching course: {e}")
            return None
            return False, e        
    
    def get_textbook_id_from_course_id(self, course_id):
        cursor = self.db_connection.cursor()
        try:
            query = "SELECT textbook_id FROM Course WHERE course_id = %s"
            
            cursor.execute(query, (course_id,))
            
            result = cursor.fetchone()
            
            if result:
                return True, result[0] 
            else:
                return False, "No textbook found for the given course_id"
        
        except Exception as e:
            print(f"Error fetching textbook_id: {e}")
            return False, str(e)
        
        finally:
            cursor.close()

    def gettreeviewdata(self, student_id):
        try:
            cursor = self.db_connection.cursor()
            query = "SELECT course_id FROM Student_Enrolls_Course WHERE student_id = %s AND status = 'Enrolled'"
            cursor.execute(query, (student_id,))
            result = cursor.fetchall()
            cursor.close()
            return result
        except Exception as e:
            print(f"Error fetching course: {e}")
            return None
    
    def getTextbookDetails(self, course_id):
        try:
            cursor = self.db_connection.cursor()
            # Query to fetch textbook detaails from course id using join between course and textbook table
            query = "SELECT textbook_id, title FROM Textbook WHERE textbook_id IN (SELECT textbook_id FROM Course WHERE course_id = %s)"
            cursor.execute(query, (course_id,))
            course = cursor.fetchall()
            cursor.close()
            return course
        except Exception as e:
            print(f"Error fetching textbook: {e}")
            return None
    
    def getChapterDetails(self, textbook_id):
        try:
            cursor = self.db_connection.cursor()
            query = "SELECT chapter_id, title FROM Chapter WHERE textbook_id = %s AND hidden = 'no'"
            cursor.execute(query, (textbook_id,))
            chapter = cursor.fetchall()
            cursor.close()
            return chapter
        except Exception as e:
            print(f"Error fetching chapter: {e}")
            return None
        
    def getSectionDetails(self, textbook_id, chapter_id):
        try:
            cursor = self.db_connection.cursor()
            query = "SELECT section_id, title FROM Section WHERE chapter_id = %s AND textbook_id = %s AND hidden = 'no'"
            cursor.execute(query, (chapter_id, textbook_id))
            section = cursor.fetchall()
            cursor.close()
            return section
        except Exception as e:
            print(f"Error fetching section: {e}")
            return None
    
    def getBlockDetails(self, textbook_id, chapter_id, section_id):
        try:
            cursor = self.db_connection.cursor()
            query = "SELECT block_id FROM Blocks WHERE chapter_id = %s AND textbook_id = %s AND section_id = %s AND hidden = 'no'"
            cursor.execute(query, (chapter_id, textbook_id, section_id))
            block = cursor.fetchall()
            cursor.close()
            return block
        except Exception as e:
            print(f"Error fetching block: {e}")
            return None     
    
        
    def get_blocks(self, textbook_id, chapter_id, section_id):
        try:
            cursor = self.db_connection.cursor()
            query = """
                SELECT *
                FROM Blocks
                WHERE textbook_id = %s AND chapter_id = %s AND section_id = %s AND hidden = 'no';
            """
            cursor.execute(query, (textbook_id, chapter_id, section_id))
            blocks = cursor.fetchall()
            cursor.close()
            return blocks
        except Exception as e:
            print(f"Error fetching blocks: {e}")
            return None   

    def get_questions(self, textbook_id, chapter_id, section_id, block_id):
        try:    
            cursor = self.db_connection.cursor()
            query = """
                SELECT *    
                FROM Question
                WHERE textbook_id = %s AND chapter_id = %s AND section_id = %s AND unique_activity_id = %s;
            """
            cursor.execute(query, (textbook_id, chapter_id, section_id, block_id))
            question = cursor.fetchall()
            cursor.close()
            return question
        except Exception as e:  
            print(f"Error fetching question: {e}")
            return None 
        
    # Student Scoring Functions
    def check_question_score_entry(self, student_id, question):
        try:
            cursor = self.db_connection.cursor()
            query = """
                SELECT *
                FROM Student_Activity_Points
                WHERE student_id = %s AND textbook_id = %s AND chapter_id = %s AND section_id =%s AND block_id = %s AND unique_activity_id = %s AND question_id = %s;
            """
            cursor.execute(query, (student_id, question[0], question[1], question[2], question[3], question[4], question[5],))            
            result = cursor.fetchall()
            cursor.close()            
            if result:
                return True 
            else:
                return False    
        except Exception as e:
            print(f"Error fetching question: {e}")
            return False
        
    def insert_question_score_entry(self, student_id, course_id, question, score):
        try:
            cursor = self.db_connection.cursor()
            query = """
                INSERT INTO Student_Activity_Points (
                student_id, course_id, textbook_id, chapter_id, section_id, block_id, unique_activity_id, question_id, points) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
            """
            cursor.execute(query, (student_id, course_id, question[0], question[1], question[2], question[3], question[4], question[5], score))
            self.db_connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print(f"Error inserting question: {e}")
            return False
        
    def update_question_score_entry(self, student_id, question, score):
        try:
            cursor = self.db_connection.cursor()
            query = """
                UPDATE Student_Activity_Points
                SET points = %s
                WHERE student_id = %s AND textbook_id = %s AND chapter_id = %s AND section_id =%s AND block_id = %s AND unique_activity_id = %s AND question_id = %s;
            """
            cursor.execute(query, (score, student_id, question[0], question[1], question[2], question[3], question[4], question[5],))
            self.db_connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print(f"Error updating question: {e}")
            return False
        
    def get_course_id_from_textbook_id(self, textbook_id):
        try:
            cursor = self.db_connection.cursor()
            query = """
                SELECT course_id
                FROM Course
                WHERE textbook_id = %s AND course_type = 'Active';
            """
            cursor.execute(query, (textbook_id,))
            course = cursor.fetchall()
            cursor.close()
            return course
        except Exception as e:
            print(f"Error fetching course: {e}")
            return None
        
        