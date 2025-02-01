#iterations
#Game with exit_right condition
exit_right = True  
if exit_right:
    set_background("woods_background")
    if exit_right:
        set_background("woods_background")
        if exit_right:
            set_background("woods_background")
        else:
            set_background("exit_background")
    else:
        set_background("exit_background")
else:
    set_background("exit_background")


#Using both while and for loop
while exit_right:
    set_background("woods_background")
    user_input = input("Which way to go? (left/right): ").lower()
    if user_input == "right":
        set_background("exit_background")
        exit_right = False
    else:
        print("You chose left. Try again.")

#Lost Forest program using while loop
where = input("You're in the Lost Forest. Go left or right? ")
while where == "right":
    where = input("You're in the Lost Forest. Go left or right? ")
print("You got out!")

#Example 2
where = input("Go left or right? ")
while where == "right":
    where = input("Go left or right? ")
print("You got out!")

#Example with numbers
n = int(input("Enter a non-negative integer: "))
while n > 0:
    print('x')
    n = n - 1

#Example 2
n = 0
where = input("Go left or right? ")
while where == "right":
    n += 1
    print(n)
    if n > 2:
        print(":(")
    where = input("Go left or right? ")
print("You got out!")

#Iterate through numbers using while loop
n = 0
while n < 5:
    print(n)
    n += 1 # n=n+1

#Find Factorial using while loop
x = 4
i = 1
factorial = 1
while i <= x:
    factorial *= i # factorial=factorial*i
    i += 1 # i=i+1
print(f"{x} factorial is {factorial}")

#Iterate through numbers using for loop
for n in range(5):
    print(n)
for n in range(4):
    print(n)
for n in range(3, 5):
    print(n)

#Different ranges example
for i in range(1, 4, 1):
    print(i)
for j in range(1, 4, 2):
    print(j * 2)
for me in range(4, 0, -1):
    print("$" * me)

#Sum program
mysum = 0
for i in range(10):
    mysum += i  # mysum = mysum+i
print(mysum)

#Sum numbers in a particular range
mysum = 0
start = 5
end = 10
for i in range(start, end + 1):
    print("i =", i)
    mysum += i
print(mysum)

#Find Factorial using for loop
x = 4
factorial = 1
for i in range(1, x + 1, 1):
    factorial *= i
print(f"{x} factorial is {factorial}")