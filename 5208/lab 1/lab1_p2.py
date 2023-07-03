#asks the user to enter number
num = int(input("Enter number:"))
list_divisors = []

#finds all divisors for given number
for i in range(1, num):
    if num % i ==0:
            list_divisors.append(i)
#prints list of divsors
print(list_divisors)
