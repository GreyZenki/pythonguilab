#opens the students.csv file
with open ('students.csv', 'r') as f:
    #reads the students.csv file and sets it as a variable
    read_file = f.read() 
    #prints the contents of the students.csv file
    print(read_file)
