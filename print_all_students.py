class PrintAllStudent:
    def __init__(self, student):
        self.student_data = student

    def print_all_students(self):
        print("="*15, "All Students' Information", "="*15)
        for i in self.student_data.allstudents:
            name, age, idnum, email, phone = i
            print (f"\nName: \t\t{name}\nAge: \t\t{age}\nID Number: \t{idnum}\nEmail: \t\t{email}\nPhone Number: \t{phone}\n")
        print("="*20,"Nothing Follows","="*20,"\n\n")
