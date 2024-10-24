from student import StudentInfo
from add_student import AddStudent
from search_student import SearchStudent
from print_all_students import PrintAllStudent
import os

class MainMenu:
    def __init__ (self, addstud, printAll, search):
        self.addstud = addstud
        self.printAll = printAll
        self.search = search

    def main_menu(self, name):

        while True: 
            try:
                print(f"\nPlease choose from the following options:")
                print("1. View your information\n2. View other student's information\n3. Register a New Student\n4. Print all students in the list\n5. Exit")
                choice = int(input("\nEnter your choice: ")) 
                if choice == 1:
                    for student in self.search.student_data.allstudents:
                        if student[0] == name:
                            print("\n","="*20, f"{name}'s Information ", "="*20,"\n")
                            print(f"Name: \t\t{student[0]}")
                            print(f"Age: \t\t{student[1]}")
                            print(f"Student ID: \t{student[2]}")
                            print(f"Email: \t\t{student[3]}")
                            print(f"Phone Number: \t{student[4]}")
                            print("\n","="*69)
                            student_found = True
                            break
                    if not student_found:
                        print("Error: Your Information could not be found.")
                elif choice == 2:
                        student_id = (input("Please enter Student ID: "))
                        self.search.search_by_id(student_id)
                elif choice == 3:
                    self.addstud.input_add_student()
                elif choice == 4:
                    self.printAll.print_all_students()
                else:
                    print("Exiting program. Thank you.")
                    break
            except ValueError:
                print("Invalid Input. Please enter a valid option (1-5).")
                

stu = StudentInfo()
addstud, search, printAll = AddStudent(stu), SearchStudent(stu), PrintAllStudent(stu)
#Make sure na ung pagkakasunod nung 'menu', is same dun sa initialization
menu = MainMenu(addstud, printAll, search)



attempts = 0 
stu.read()
while attempts < 4:
    print ("\n","="*10, "Login - Student Info. System", "="*10)
    login_check = input("Student ID: ")
    user = search.verify_login(login_check)
    if user != False:
        menu.main_menu(user) 
        break
    else:
        os.system("cls")
        attempts += 1 
        print(f"\nThe student with the ID Number {login_check} does not exist.\nAttempts left {4 - attempts}")
    if attempts > 3:
        os.system("cls")
        print("="*7, "Login Error - Student Info. System","="*7)
        print("You have exceeded the number of attempts allowed.\nExiting the System. Goodbye")
        
