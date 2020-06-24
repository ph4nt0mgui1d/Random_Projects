#Fibonacci Series

terms = int(input("How many terms do you want to print : "))
n1 = 0
n2 = 1
a = 0

if terms <= 0:
    print("Enter a positive value and greater than zero.")
elif terms == 1:
    print ("Fibonacci series : {}".format(n1))
else:
    print("Fibonacci sereies : ")
    while a < terms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        a += 1