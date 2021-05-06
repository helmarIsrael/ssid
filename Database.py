import csv
import pandas
import os

column_names = ["Student ID","Name","Year Level","Gender","Course"] #the columns of the csv
filesize = os.path.getsize("student_database.csv") # checks if the file is empty
if filesize == 0:
      with open("student_database.csv", mode="w") as student_database: #if file is empty, it will create the columns first
            student_list = csv.writer(student_database, delimiter=",")
            student_list.writerow(column_names)

def cls():
      print("\n" * 100)

def view_student():                                                             #this function will show the list of students input by the user
      df = pandas.read_csv("student_database.csv", 'r', delimiter=",")
      df.to_csv("student_database.csv", header=column_names, index=False)
      df_csv = pandas.read_csv("student_database.csv")
      print(df_csv)
      input("Press enter to return to main menu...")


def add_student():                                                              #this function will allow user to add students
      with open("student_database.csv", mode="a") as student_database:
            student_list = csv.writer(student_database)
            df = pandas.read_csv("student_database.csv")
            df.to_csv("student_database.csv", index=None, header=column_names)

            print("Input student ID: ")
            id = input()
            print("Input name: ")
            name = input()
            print("Year level: ")
            year_level = input()
            print("Gender [M, F, LGBTQ]: ")
            gender = input().upper()
            print("Course: ")
            course = input().upper()

            student_list.writerow([id, name, year_level, gender, course])
            print("Student added!")
            input("Press enter to return to main menu...")

def edit_student():                                                     #this function allows the user to change the values of the student eg. name, gender, etc.
            print("Enter the student ID number to edit value: ")        #it does not support student id change so to change the student id, one must delete the student and create a new one.
            edit = input()

            with open("student_database.csv") as student_database:
                  student_list = csv.reader(student_database)
                  df = pandas.read_csv("student_database.csv", index_col="Student ID")
                  for row in student_list:
                        bool = True
                        if edit in row:
                              print("What value will you change?\n"
                                    "1. Name\n"
                                    "2. Year Level\n"
                                    "3. Gender\n"
                                    "4. Course\n"
                                    "Note: To change Student ID, delete the ID number and add a new one.")
                              value = int(input())
                              with open("student_database.csv") as student_database:
                                    student_list = csv.reader(student_database)
                                    df = pandas.read_csv("student_database.csv", index_col="Student ID")
                                    for row in student_list:
                                          if edit in row:
                                                if value == 1:
                                                      print(row)
                                                      print("Input a new name: ")
                                                      name =  input()
                                                      df._set_value(edit, "Name", name)
                                                      df.to_csv("student_database.csv")
                                                      print("Done.")
                                                      input("Press enter to return to main menu...")
                                                      break
                                                elif value == 2:
                                                      print(row)
                                                      print("Input a new year level: ")
                                                      yr_lvl = input()
                                                      df._set_value(edit, "Year Level", yr_lvl)
                                                      df.to_csv("student_database.csv")
                                                      print("Done.")
                                                      input("Press enter to return to main menu...")
                                                      break
                                                elif value == 3:
                                                      print(row)
                                                      print("Apply a new gender: ")
                                                      gender = input()
                                                      df._set_value(edit, "Gender", gender)
                                                      df.to_csv("student_database.csv")
                                                      print("Done.")
                                                      input("Press enter to return to main menu...")
                                                      break
                                                elif value == 4:
                                                      print(row)
                                                      print("Change a new course: ")
                                                      course = input()
                                                      df._set_value(edit, "Course", course)
                                                      df.to_csv("student_database.csv")
                                                      print("Done.")
                                                      input("Press enter to return to main menu...")
                                                      break
                                                else:
                                                      print("Wrong Value")
                                                      input("Press enter to return to main menu...")

                              break
                        else:
                              bool = False
                  if bool ==  False:
                        print("ID not found")
                        input("Press enter to return to main menu...")

def delete_student():                                                           #this will allow for the user to delete the student in the list using the student ID
      print("Input Student ID:")
      id = str(input())
      with open("student_database.csv") as student_database:
            student_list = csv.reader(student_database)
            df = pandas.read_csv("student_database.csv", index_col= "Student ID")
            for row in student_list:
                  bool = True
                  if id in row:
                        df.drop(id, axis= 0, inplace= True)
                        df.to_csv("student_database.csv")
                        print("Succesfully deleted! ")
                        input("Press enter to return to main menu...")
                  else:
                        bool = False
            if bool == False:
                  print("No Student ID found.")
                  input("Press enter to return to main menu...")

def find():                                                       #this function will find the student based on its student ID
      print("Enter Student ID number: ")
      id = str(input())
      with open("student_database.csv") as student_database:
            student_list = csv.reader(student_database)
            df = pandas.read_csv("student_database.csv", index_col="Student ID")
            for row in student_list:
                 bool = True
                 if id in row:
                       print(row)
                       input("Press enter to return to main menu...")
                 else:
                       bool = False
            if bool == False:
                  print("No Student ID found.")
                  input("Press enter to return to main menu...")


def exit():                   #this function will end the program
      print("Goodbye")
      quit()

while True:
      print("----------------")
      print("Student Database")
      print("1. View Students Information\n"
            "2. Add a student\n"
            "3. Edit student\n"
            "4. Delete a student\n"
            "5. Find Student ID\n"
            "6. Exit\n"
            "\n"
            "Input: ")

      selection = input()

      if selection == "1":
            view_student()
            cls()
      elif selection == "2":
            add_student()
            cls()
      elif selection == "3":
            edit_student()
            cls()
      elif selection == "4":
            delete_student()
            cls()
      elif selection == "5":
            find()
            cls()
      elif selection == "6":
            exit()
      else:
            print("Please select the desired values...")