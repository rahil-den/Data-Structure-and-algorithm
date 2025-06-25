def sumoffirstnwith_recursion(n): # My method
    if n == 0:
        return 0
    return n + sumoffirstnwith_recursion(n - 1)
def sumoffirst(i,sum):
    if i < 1:
        print(sum)
        return
        # return sum
    sumoffirst(i - 1, sum + i)  # Paremeters are passede to the function method
def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n-1)
if __name__ == "__main__":
    n = 3
    sum = 0
    result = sumoffirstnwith_recursion(n)
    result1 = sumoffirst(n,sum)
    print(f"The sum of the first {n} natural numbers is: {result}")
    print("Below is the same result")
    sumoffirst(n, sum)  
    # print(f"The sum of the first {n} and {sum} natural numbers is: {result1}")
    num = int(input("Enter a number to find its factorial: "))
    print(f"The factorial of {n} is: {fact(num)}")