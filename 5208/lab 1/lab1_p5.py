#creates GPA scale
def get_four_scale(GPA):
    if GPA >= 97 and GPA <= 100:
        return 4.0
    elif GPA >= 93 and GPA <= 96:
        return 4.0
    elif GPA >= 90 and GPA <= 92:
        return 3.7
    elif GPA >= 87 and GPA <= 89:
        return 3.3
    elif GPA >= 83 and GPA <= 86:
        return 3.0
    elif GPA >= 80 and GPA <= 82:
        return 2.7
    elif GPA >= 77 and GPA <= 79:
        return 2.3
    elif GPA >= 73 and GPA <= 76:
        return 2.0
    elif GPA >= 70 and GPA <= 72:
        return 1.7
    elif GPA >= 67 and GPA <= 69:
        return 1.3
    elif GPA >= 63 and GPA <= 66:
        return 1.0
    elif GPA >= 60 and GPA <= 62:
        return 0.7
    else:
        return 0.0
    
#creates letter grade scale    
def getLetterGrade(GPA):

    if GPA >= 97 and GPA <= 100:
        return "A+"
    elif GPA >= 93 and GPA <= 96:
        return "A"
    elif GPA >= 90 and GPA <= 92:
        return "A-"
    elif GPA >= 87 and GPA <= 89:
        return "B+"
    elif GPA >= 83 and GPA <= 86:
        return "B"
    elif GPA >= 80 and GPA <= 82:
        return "B-"
    elif GPA >= 77 and GPA <= 79:
        return "C+"
    elif GPA >= 73 and GPA <= 76:
        return "C"
    elif GPA >= 70 and GPA <= 72:
        return "C-"
    elif GPA >= 67 and GPA <= 69:
        return "D+"
    elif GPA >= 63 and GPA <= 66:
        return "D"
    elif GPA >= 60 and GPA <= 62:
        return "D-"
    else:
        return "F"
    

def main():

    #asks user to input name    
    stuName = input("Enter Student Name: ")

    #creates list for courses and grades
    courses = []
    grades = []

    #asks user to input number of courses 
    i = int(input("Enter number of courses? "))

    #asks user for course name and grade
    for i in range(4):
        courses.append(input("Course#" + str(i+1) + "? "))
        grades.append(float(input("Course Grade (0-100)? ")))

    #prints name of student 
    print("\n\nHere is : " + stuName + "'s info ")
    print("--------------------------------------------------------------")
    print("Course: Grade: Course GPA")
    ("--------------------------------------------------------------")
    s = 0
    
    #prints results of course GPA
    for i in range(4):
        cGpa = get_four_scale(grades[i])
        s += cGpa
        print("%s : %.1f : %.2f "%(courses[i], grades[i], cGpa))

    #prints quarter GPA
    print("\nQuarter GPA: %.3f "%(s/4.0))
    print("--------------------------------------------------------------")



main()    