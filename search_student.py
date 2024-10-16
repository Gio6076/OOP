class SearchStudent:
    def __init__(self, student_data):
        self.student_data = student_data

    def verify_login(self, student_id):
        for student in self.student_data.allstudents:
            if student[2] == student_id: 
                print(f"Welcome, {student[0]}!") 
                return student[0] 
        return False

    def search_by_id(self, student_id):
        for student in self.student_data.allstudents:
            if student[2] == student_id:
                print(f"="*20," Student Found ","="*20)
                print(f"Name: \t\t{student[0]}")
                print(f"Age: \t\t{student[1]}")
                print(f"Student ID: \t{student[2]}")
                print(f"Email: \t\t{student[3]}")
                print(f"Phone Number: \t{student[4]}")
                print("="*55)
                return True
        print(f"No student found with ID {student_id}.")
        return False
