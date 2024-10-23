class StudentInfo:
    def __init__(self):
        self.name, self.age, self.idnum, self.email, self.phone = "","","","",""
        self.allstudents = []
        self.read()

    def setName(self, name):
        self.name = name

    def setAge(self, age):
        self.age = age

    def setIDNum(self, idnum):
        self.idnum = idnum
        
    def setEmail(self, email):
        self.email = email

    def setPhoneNum(self, phone):
        self.phone = phone

    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    
    def getIDNum(self):
        return self.idnum
    
    def getEmail(self):
        return self.email
    
    def getPhoneNum(self):
        return self.phone
    
    def __str__ (self):
        return f"\nName: {self.name}\nAge: {self.age}\nID Number {self.idnum}\nEmail {self.email}\n Phone Number: {self.phone}"
    
    def read(self):
        try:
            with open ("student.txt", "r") as file:
                linya = file.readlines()
                for line in linya[0:]:
                    linestrip = line.strip().split(", ")
                    self.allstudents.append(linestrip)
            print("Done reading...")
        except FileNotFoundError:
            print("File can't be found...")
