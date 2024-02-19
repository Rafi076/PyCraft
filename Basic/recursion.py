# recursion is the process of defining somthing in terms of itself.

# factorial of a number using recursion

def factorial(num):
    if(num == 1 or num == 0): return 1
    else: return(factorial(num-1)*num)

num = int(input("Enter a number : "))
x = factorial(num)
print(f"Factorial of {num} is = ",x)



# Fibonacci serices: 
def fibonacci(num):
    fib_serices = [0,1]
    while len(fib_serices)<num:
        fib_serices.append(fib_serices[-1]+fib_serices[-2])
    return fib_serices

num = int(input("Enter a number for fibonacci serices : "))
result = fibonacci(num)
print(result)
