__author__ = 'Praveen Kumar Anbalagan'


#recursive method

def factorial(n):

    return 1 if(n==0 or n==1) else n*factorial(n-1)

#getting input from the user and converting into int, because inputs always saved as string
num = int(input('Enter the num to find its Factorial: '))

#printing the factorial
print("The Factorial of {0} is {1}".format(num,factorial(num)))

