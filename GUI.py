from tkinter import *

win = Tk()


# def login_confirm():
#     first_frame.pack_forget()
#     menu_frame.pack(fill="both", expand=True)


# first_frame = Frame(win, bg="black")
# first_frame.pack(fill="both", expand=True)

# Login_frame = Frame(first_frame, bg="white", padx=10, relief="solid")
# Login_frame.place(relx=0.5, rely=0.5, anchor="center")
# Label(Login_frame, text="Welcome to the GUI", font=("Times New Roman", 20), pady=20).pack()
# login_btn = Button(Login_frame, text="Login", width=20, font=("Times New Roman", 20), command=login_confirm)
# login_btn.pack()
# exit_btn = Button(Login_frame, text="Exit", width=20, font=("Times New Roman", 20))
# exit_btn.pack()

# menu_frame = Frame(win, height= 1080, width=400, bg="light blue")
# Label (menu_frame, text="User ID", font= ("Times New Roman", 20), pady=20, fg="blue").pack(anchor="w")



# win.geometry("1080x700+230+40")
# win.title("STUDENT INFO GUI")
# win.mainloop()




# Initialize the main window


# Define functions
def switch_frame(new_frame):
    """Switch the content in the main area to the new frame."""
    for widget in content_frame.winfo_children():
        widget.destroy()  # Remove all widgets from the current frame
    Label(content_frame, text=new_frame, font=("Times New Roman", 30), fg="blue").pack(expand=True)


def login_confirm():
    first_frame.pack_forget()
    main_frame.pack(fill="both", expand=True)

def logout_confirm():
    main_frame.pack_forget()
    first_frame.pack(fill="both", expand=True)

# First Frame (Login)
first_frame = Frame(win, bg="black")
first_frame.pack(fill="both", expand=True)

login_frame = Frame(first_frame, bg="white", padx=10, relief="solid")
login_frame.place(relx=0.5, rely=0.5, anchor="center")
Label(login_frame, text="Welcome to the GUI", font=("Times New Roman", 20), pady=20).pack()
Button(login_frame, text="Login", width=20, font=("Times New Roman", 20), command=login_confirm).pack()
Button(login_frame, text="Exit", width=20, font=("Times New Roman", 20), command=win.quit).pack()


main_frame = Frame(win)


sidebar_frame = Frame(main_frame, bg="light gray", width=200)
sidebar_frame.pack(side="left", fill="y")


content_frame = Frame(main_frame, bg="white")
content_frame.pack(side="right", fill="both", expand=True)


Label (sidebar_frame, text="User ID", font=("Times New Roman", 20), fg="blue").pack()

labels = ["View My Information", "Add Student", "Search for Student", "Logout", "Exit"]
for label in labels:
    Button(sidebar_frame,text=label,font=("Times New Roman", 16),width=20,
    command=lambda lbl=label: switch_frame(lbl)
    ).pack(pady=10)
if "Logout" == True:
    command = logout_confirm

win.geometry("1080x700+230+40")
win.title("STUDENT INFO GUI")
win.mainloop()
