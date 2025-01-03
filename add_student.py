class AddStudent:
    def __init__(self, student):
        self.student_data = student
        
    
    def add_student(self, name, age, idnum, email, phone):
        self.student_data.setName(name)
        self.student_data.setAge(age)
        self.student_data.setIDNum(idnum)
        self.student_data.setEmail(email)
        self.student_data.setPhoneNum(phone)
        student_written = [name, age, idnum, email, phone]
        self.student_data.allstudents.append(student_written)
        print(f"Added student {student_written[0]} to the list.")
        self.write(student_written)
        #student = [name, age, idnum, email, phone]
        

    def write(self, student_written):
        with open ("student.txt", "a+") as file:
            file.write(", ".join(map(str, student_written)) + "\n")
        print(f"Done adding to the list")


    def input_add_student(self):
        while True:
            print("\n","="*20, "Add New Student","="*20,"\n")
            name, age, idnum, email, phone = input("Enter Name: "), int(input("Enter Age: ")), input("Enter ID Number: "), input("Enter Email: "), input("Enter Phone Number: ")
            print("\n","="*20, "Nothing Follows", "="*20,"\n")
            self.add_student(name, age, idnum, email, phone)
            choice = input("Do you want to add another student? (Y/N): ")
            if choice.lower() != 'y':
                print("Returning to Main Menu...")
                break
