# recursion and basically it refers to a function calling itself.
def factorial(n):
    if n < 1:
        return 1
    else:
        number = n*factorial(n-1)
    return number
print(factorial(5))