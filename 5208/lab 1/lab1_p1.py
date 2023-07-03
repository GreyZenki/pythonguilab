#asks the user for name
name = input ("What is your name?")

#asks the user for age
age = int(input("How old are you?"))

#takes the age and subtracts by the current year to get birth year of user
year = 2022 - age

#prints the name of user and year of birth
print(name + " you were born in the year " + str(year))

