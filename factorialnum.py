# Python Program for factorial of a number
# Factorial of a non-negative integer, is multiplication of all integers smaller than or equal to n.
# For example factorial of 6 is 6*5*4*3*2*1 which is 720.


def factorial(n): #here we use function
     if n<0:
        return 0  #when you put 0 then return 0
     elif n==0 or n==1:
        return 1  #when you put 1 then return 1
     else:
        fact=1
        while(n>1):
            fact *=n # here we use formula of factorial
            n=n-1
        return fact  #here return the value

print(factorial(5))   #final output   


