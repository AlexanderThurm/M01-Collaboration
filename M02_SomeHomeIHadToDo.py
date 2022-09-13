loopValue = "y"

while loopValue == "y":

    studentLastName = input("What is your Last Name?")
    studentFirstName = input("Please enter you first name.")
    studentGPA = float(input("Please input your GPA."))

    if  studentGPA >= 3.25:
        print(studentFirstName, studentLastName, "does make the honor role.")
    else:
        print(studentFirstName, studentLastName, "does not make the honor role.")


    if studentGPA >= 3.5:
        print(studentFirstName, studentLastName, "does make the Dean's list.")
    else:
        print(studentFirstName, studentLastName, "does not make the Dean's list.")
    loopValue = input("Do you want to continue this program? y or n")

else:
    print("Thank you for using this program!")
    quit()
