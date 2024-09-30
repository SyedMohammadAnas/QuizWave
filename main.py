from tkinter import*
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector

class Quiz:
    def __init__ (self,root):
        self.root = root
        self.root.title("QuizWave")
        self.root.geometry("800x700+0+0")

        self.studentName = StringVar()
        self.RNumber = StringVar()

        lbttitle = Label(self.root, bd = 23,
                        relief = RIDGE,
                        text = "QUIZWAVE",
                        fg = "red",
                        bg = "white",
                        font = ("jetbrains mono", 50, "bold"),
                        )
        lbttitle.pack(side = "top", fill=X)

        #AlreadyExists Option during REGISTERING
        self.alreadyExists = Label(self.root,
                                   text = "Already an Existing User? Click here -> ",
                                   font = ("jetbrains mono", 10, "bold"))
        self.hyperLink1 = Label(self.root,
                                   text = "LOGIN", fg="blue", cursor="hand2",
                                   font = ("jetbrains mono", 10, "bold"))
        #DoesntExist Option during LOGGING IN
        self.doesntExist = Label(self.root,
                                   text = "Not an Existing User? Click here -> ",
                                   font = ("jetbrains mono", 10, "bold"))
        self.hyperLink2 = Label(self.root,
                                   text = "REGISTER", fg="blue", cursor="hand2",
                                   font = ("jetbrains mono", 10, "bold"))

        #Login Area
        datFrame = Frame(self.root, bd = 20, relief=RIDGE)
        datFrame.place(x = 200, y = 240, width = 400, height = 360)

        #Teacher and Student Buttons
        self.teacherButton = Button(root, text="TEACHER",
                                    fg = 'white', bg = 'red',
                                    command=self.studentButtonPress,
                                    font = ("jetbrains mono", 25, "bold"))
        self.teacherButton.place(x=260, y=300, width=280, height=75)
        self.studentButton = Button(root, text="STUDENT",
                                  fg = 'white', bg = 'red',
                                  command=self.studentButtonPress,
                                  font = ("jetbrains mono", 25, "bold"))
        self.studentButton.place(x=260, y=460, width=280, height=75)

        #Register and Login Buttons
        self.reigsterButton = Button(root, text="REGISTER",
                                    fg = 'white', bg = 'red',
                                    command=self.regButtonPress,
                                    font = ("jetbrains mono", 25, "bold"))
        self.LoginButton = Button(root, text="LOGIN",
                                  fg = 'white', bg = 'red',
                                  command=self.logButtonPress,
                                  font = ("jetbrains mono", 25, "bold"))

        #NAME AND REGISTERED NUMBER
        self.nameFrame = LabelFrame(datFrame, bd = 10, padx=57,
                                    relief = RIDGE,
                                    font = ("jetbrains mono", 10, "bold"),
                                    text = 'NAME')
        self.RNumberFrame = LabelFrame(datFrame, bd = 10, padx=57,
                                    relief = RIDGE,
                                    font = ("jetbrains mono", 10, "bold"),
                                    text = 'Registered Number')

        #Entry Frames for Name and Registered Numeber
        self.nameBox = Entry(datFrame,
                             textvariable=self.studentName,
                             font = ("jetbrains mono", 10, "bold"))
        self.RNumberBox = Entry(datFrame,
                                textvariable=self.RNumber,
                                font = ("jetbrains mono", 10, "bold"))

        #Final LOGIN AND REGISTER Buttons
        self.finalLoginButton = Button(root, text="LOGIN",
                                  fg = 'white', bg = 'red',
                                  command=self.studentData,
                                  font = ("jetbrains mono", 25, "bold"))
        self.finalRegisterButton = Button(root, text="REGISTER",
                                    fg = 'white', bg = 'red',
                                    command=self.checkRegister,
                                    font = ("jetbrains mono", 25, "bold"))

    def studentButtonPress(self):
        self.teacherButton.place_forget()
        self.studentButton.place_forget()
        self.reigsterButton.place(x=260, y=300, width=280, height=75)
        self.LoginButton.place(x=260, y=460, width=280, height=75)



    def logButtonPress(self, event = None):
        # Hide both buttons when either is clicked
        self.reigsterButton.place_forget()
        self.LoginButton.place_forget()
        self.finalRegisterButton.place_forget()
        self.alreadyExists.place_forget()
        self.hyperLink1.place_forget()
        self.nameBox.place(x = 75, y = 85,width = 235, height = 30)
        self.RNumberBox.place(x = 75, y = 180,width = 235, height = 30)
        self.nameFrame.place(x = 57, y = 50, width = 265, height=90)
        self.RNumberFrame.place(x = 57, y = 146, width = 265, height=90)
        self.finalLoginButton.place(x=310, y=525, width=200, height=45)
        self.doesntExist.place(x = 120, y = 620, width = 480, height = 20)
        self.hyperLink2.place(x = 520, y = 620, width = 65, height = 20)
        self.hyperLink2.bind("<Button-1>", self.regButtonPress)

    def regButtonPress(self, event = None):
        # Hide both buttons when either is clicked
        self.reigsterButton.place_forget()
        self.LoginButton.place_forget()
        self.finalLoginButton.place_forget()
        self.doesntExist.place_forget()
        self.hyperLink2.place_forget()
        self.nameBox.place(x = 75, y = 85,width = 235, height = 30)
        self.RNumberBox.place(x = 75, y = 180,width = 235, height = 30)
        self.nameFrame.place(x = 57, y = 50, width = 265, height=90)
        self.RNumberFrame.place(x = 57, y = 146, width = 265, height=90)
        self.finalRegisterButton.place(x=310, y=525, width=200, height=45)
        self.alreadyExists.place(x = 120, y = 620, width = 480, height = 20)
        self.hyperLink1.place(x = 520, y = 620, width = 50, height = 20)
        self.hyperLink1.bind("<Button-1>", self.logButtonPress)

    #DATABASE FUNCTIONALITY
    def studentData(self):
        if self.studentName.get() == "" or self.RNumber.get() == "":
            messagebox.showerror("Error", "Fill ALL the Fields")
        else:
            try:
                # Establish a connection to the database
                connect = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="SergantSwagg@06",
                    database="quiz"
                )
                myCursor = connect.cursor()

                # Query to check if student exists
                query = "SELECT * FROM studentInformation WHERE Studentname = %s AND RegisteredNumber = %s"
                myCursor.execute(query, (self.studentName.get(), self.RNumber.get()))

                # Fetch the result
                result = myCursor.fetchone()

                # If a result is found, the student is logged in
                if result:
                    messagebox.showinfo("Success", "You are logged in!")
                else:
                    messagebox.showerror("Error", "Student not found. Please register first.")

            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Something went wrong: {err}")
            finally:
                connect.close()


    def checkRegister(self):
        if self.studentName.get() == "" or self.RNumber.get() == "":
            messagebox.showerror("Error", "Fill ALL the Fields")
        else:
            try:
                # Establish a connection to the database
                connect = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="SergantSwagg@06",
                    database="quiz"
                )
                myCursor = connect.cursor()

                # Execute a SELECT query to check if the registration number or student name exists
                query = "SELECT * FROM studentInformation WHERE Studentname = %s OR RegisteredNumber = %s"
                myCursor.execute(query, (self.studentName.get(), self.RNumber.get()))

                # Fetch all matching rows
                result = myCursor.fetchall()

                # Check if any matching record exists
                if result:
                    messagebox.showinfo("Info", "Student or Register Number already exists.")
                else:
                    # Proceed with inserting the new data
                    self.insert_student_data()
            except mysql.connector.Error as err:
                    messagebox.showerror("Error", f"Something went wrong: {err}")
            finally:
                connect.close()


    def insert_student_data(self):
        # Insert new student data after checking if it doesn't exist
        connect = mysql.connector.connect(
            host="localhost",
            username="root",
            password="SergantSwagg@06",
            database="quiz"
        )
        myCursor = connect.cursor()

        # Insert data into the database
        myCursor.execute("INSERT INTO studentInformation (StudentName, RegisteredNumber) VALUES (%s, %s)",
                         (self.studentName.get(), self.RNumber.get()))

        connect.commit()
        connect.close()
        messagebox.showinfo("Success", "You've Successfully Registered!")


root=Tk()
ob=Quiz(root)
root.mainloop()
