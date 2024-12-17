from tkinter import *
from student import StudentInfo
from add_student import AddStudent
from search_student import SearchStudent
from print_all_students import PrintAllStudent
import pygame

stu = StudentInfo()
addstud = AddStudent(stu)
search = SearchStudent(stu)
print_all = PrintAllStudent(stu)

stu.read()
pygame.mixer.init()
login_sound = pygame.mixer.Sound("D:\\VISUAL_STUDIO_COD\Python_Codes\OOP\BomboF.mp3")
invalid_sound = pygame.mixer.Sound("D:\\VISUAL_STUDIO_COD\Python_Codes\OOP\OOF_MCF.mp3")
click_sound = pygame.mixer.Sound("D:\\VISUAL_STUDIO_COD\Python_Codes\OOP\ClickF.mp3")
menu_sound = pygame.mixer.Sound("D:\\VISUAL_STUDIO_COD\Python_Codes\OOP\MenuF.mp3")
logout_sound = pygame.mixer.Sound("D:\\VISUAL_STUDIO_COD\Python_Codes\OOP\GoodByeF.mp3")
bg_sound = pygame.mixer.Sound("D:\\VISUAL_STUDIO_COD\Python_Codes\OOP\MCBG.mp3")

def show_frame(frame):
    #Show the Frames
    for frm in all_frames:
        frm.pack_forget()
    frame.pack(fill="both", expand=True)


def switch_frame(new_frame):
    # Swticher ng Contents
    if new_frame == "My Information":
        my_information()
    elif new_frame == "Search Student":
        search_student()
    elif new_frame == "Register New Student":
        register_student()
    elif new_frame == "Student List":
        view_student_list()
    elif new_frame == "Logout":
        logout_confirm()


def login_confirm():
    student_id = login_entry.get()
    global attempts
    user = search.verify_login(student_id)

    if user:
        stu.current_user = user
        first_frame.pack_forget()
        main_frame.pack(fill="both", expand=True)
        home_label.config(text=f"Welcome back, {user}!")
        show_frame(home_frame)
        login_sound.play()
    else:
        invalid_sound.play()
        attempts -= 1
        status_label.config(text=f"Invalid ID. Attempts left: {attempts}", fg="red")
        if attempts == 0:
            win.quit()


def logout_confirm():
    logout_sound.play()
    stu.current_user = None
    main_frame.pack_forget()
    first_frame.pack(fill="both", expand=True)
    login_entry.delete(0, END)
    status_label.config(text="")
    global attempts
    attempts = 3


def my_information():
    # Display the Information
    menu_sound.play()
    show_frame(my_info_frame)
    info_text.config(state="normal")
    info_text.delete("1.0", END)

    if stu.current_user:
        for student in stu.allstudents:
            if student[0] == stu.current_user:
                formatted_info = f"""

            \t===========================
            \t    STUDENT INFORMATION
            \t===========================
            \tName        : \t{student[0]}
            \tAge         : \t{student[1]}
            \tID Number   : \t{student[2]}
            \tEmail       : \t{student[3]}
            \tPhone       : \t{student[4]}
            \t===========================
"""
                break
        else:
            formatted_info = "No information found for the current user."
    else:
        formatted_info = "No student is currently logged in."

    info_text.insert(END, formatted_info)
    info_text.config(state="disabled")


def search_student():
    #Search ka Student 
    menu_sound.play()
    show_frame(search_frame)
    search_result_label.config(text="")

    def perform_search():
        student_id = search_entry.get()
        search_text.config(state="normal")
        search_text.delete("1.0", END)

        found = False
        for student in stu.allstudents:
            if student[2] == student_id:
                click_sound.play()
                formatted_info = f"""
        ===========================
            STUDENT INFORMATION
        ===========================
        Name        : {student[0]}
        Age         : {student[1]}
        ID Number   : {student[2]}
        Email       : {student[3]}
        Phone       : {student[4]}
        ===========================
"""

                search_text.insert(END, formatted_info)
                found = True
                break
        if not found:
            invalid_sound.play()
            search_text.insert(END, f"No Student found with ID {student_id}.")
        search_text.config(state="disabled")          

    search_button.config(command=perform_search)


def register_student():
    #Registration to
    menu_sound.play()
    show_frame(register_frame)
    registration_status_label.config(text="")

    def submit_registration():
        student_data = {field: entries[field].get() for field in entries}
        if all(student_data.values()):
            try:
                addstud.add_student(
                    student_data["Name"],
                    int(student_data["Age"]),
                    student_data["ID Number"],
                    student_data["Email"],
                    student_data["Phone"],
                )
                registration_status_label.config(text="Student registered successfully!", fg="green")
                click_sound.play()
                for entry in entries.values():
                    entry.delete(0, END)
            except ValueError:
                registration_status_label.config(text="Invalid data! Ensure Age is a number.", fg="red")
        else:
            invalid_sound.play()
            registration_status_label.config(text="All fields must be filled.", fg="red")

    submit_button.config(command=submit_registration)


def view_student_list():
    #Print all Studs
    menu_sound.play()
    show_frame(list_frame)
    student_list_text.config(state="normal")  # Enable editing of the text box
    student_list_text.delete("1.0", END)  # Clear previous content

    if stu.allstudents:
        student_list_text.insert(END, f"{'='*25} STUDENT LIST {'='*25}\n\n")
        for student in stu.allstudents:
            formatted_info = f"""
Name        : {student[0]}
Age         : {student[1]}
ID Number   : {student[2]}
Email       : {student[3]}
Phone       : {student[4]}
{'-'*120}
"""
            student_list_text.insert(END, formatted_info)
        student_list_text.insert(END, f"\t\t\tNothing Follows\n{'='*65}\n")
    else:
        student_list_text.insert(END, "No students found in the list.\n")

    student_list_text.config(state="disabled")  # Disable editing again

# Main window 
win = Tk()

# First Frame (Login)
attempts = 5
bg_sound.play(loops = 10)
first_frame = Frame(win, bg="#3C763D")
first_frame.pack(fill="both", expand=True)
login_frame = Frame(first_frame, bg="light yellow", padx=10, relief="raised")
login_frame.place(relx=0.5, rely=0.5, anchor="center")
Label(login_frame, text="Student Information of Joemama", font=("Minecraft", 20),width=40, pady=20, fg="#1B03A3").pack()
Label(login_frame, text="Enter your Student ID:", font=("Minecraft", 16), width=40).pack()
login_entry = Entry(login_frame, width=40, font=("Minecraft", 16))
login_entry.pack(pady=10)
Button(login_frame, text="Login", width=20, font=("Minecraft", 20), command=login_confirm, bg="#A5C847", relief="solid", fg="black").pack()
Button(login_frame, text="Exit", width=20, font=("Minecraft", 20), command=win.quit, bg="#A5C847", relief="solid", fg="black").pack(pady=10)
status_label = Label(login_frame, text="", font=("Minecraft", 14))
status_label.pack()

# Main Frame
main_frame = Frame(win, bg="#555555")

# Sidebar
sidebar_frame = Frame(main_frame, bg="dark green", width=200)
sidebar_frame.pack(side="left", fill="y")

content_frame = Frame(main_frame, bg="white")
content_frame.pack(side="right", fill="both", expand=True)

# Home Frame
home_frame = Frame(content_frame, bg="white")
home_label = Label(home_frame, text="", font=("Minecraft", 24), width=60, bg="lightgreen", pady=20, fg="black")
home_label.pack()

# My Information Frame
my_info_frame = Frame(content_frame, bg="white")
title = Label(my_info_frame, text="Student Information", font=("Minecraft", 20), width=60, bg="lightgreen", relief="flat", pady=20).pack()
info_text = Text(my_info_frame, font=("Minecraft", 20), width=60, height=15, bg="lightgreen", relief="flat", wrap="word")
info_text.pack(pady=20)
info_text.config(state="disabled")

# Search Student Frame
search_frame = Frame(content_frame, bg="white")
Label(search_frame, text="Search for a Student", font=("Minecraft", 20), width=60, bg="lightgreen", relief="flat",pady=20).pack()
search_entry = Entry(search_frame, width=30, font=("Minecraft", 16))
search_entry.pack(pady=10)
search_button = Button(search_frame, text="Search", font=("Minecraft", 16), bg="#A5C847", fg="black", relief="solid")
search_button.pack(pady=10)
search_text = Text(search_frame, font=("Minecraft", 20), width=60, height=15, bg="lightgreen", relief="flat", wrap="word")
search_text.pack(pady=20)
search_text.config(state="disabled")
search_result_label = Label(search_frame, text="", font=("Minecraft", 14), fg="red")
search_result_label.pack(pady=10)

# Register New Student Frame
register_frame = Frame(content_frame, bg="white")
Label(register_frame, text="Register a New Student", font=("Minecraft", 20), width=60, bg="lightgreen", relief="flat", pady=20).pack()
entries = {}
for field in ["Name", "Age", "ID Number", "Email", "Phone"]:
    Label(register_frame, text=f"Enter {field}:", font=("Minecraft", 16), bg="white", fg='black', width=20).pack(pady=5)
    entry = Entry(register_frame, width=30, font=("Minecraft", 16))
    entry.pack(pady=5)
    entries[field] = entry
submit_button = Button(register_frame, text="Submit", font=("Minecraft", 16), bg="#A5C847", fg="black", relief="solid")
submit_button.pack(pady=20)
registration_status_label = Label(register_frame, text="", font=("Minecraft", 16))
registration_status_label.pack()

# Student List Frame
list_frame = Frame(content_frame, bg="white")
Label(list_frame, text="Student List", font=("Minecraft", 20), width=60, bg="lightgreen", relief="flat", pady=20).pack()

# Scrollable text area for student list
student_list_text_frame = Frame(list_frame)
student_list_text_frame.pack(pady=5, padx=5)

student_list_text = Text(student_list_text_frame, font=("Minecraft", 14), width=70, height=20, bg="white", relief="flat", wrap="word")
student_list_text.pack(side=RIGHT, fill="both", expand=True)

# Add scrollbar to the text area
list_scrollbar = Scrollbar(student_list_text_frame, orient=VERTICAL, command=student_list_text.yview)
list_scrollbar.pack(side=RIGHT, fill=Y)
student_list_text.config(yscrollcommand=list_scrollbar.set)

# Initially disable editing
student_list_text.config(state="disabled")

# Keep track of all frames
all_frames = [home_frame, my_info_frame, search_frame, register_frame, list_frame]

# Sidebar Buttons
labels = ["My Information", "Search Student", "Register New Student", "Student List", "Logout"]
for label in labels:
    Button(sidebar_frame, text=label, font=("Minecraft", 16), width=25, height=2, fg="black", relief="solid", command=lambda lbl=label: switch_frame(lbl)).pack(padx=15, pady=5)

# Window Settings
win.geometry("1080x700+230+40")
win.title("Student Information ni Grinjoe")
win.mainloop()
