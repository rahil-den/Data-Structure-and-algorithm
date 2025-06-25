# How does recursion work? when a function call itself, it creates a new frame on the call stack. It'll only stop when it reaches the base condition.

def pri():
    print("Hello World" + "1" )  # This will print "Hello World" followed by 1000 ones
    pri()  

# pri()  # This will cause a RecursionError: maximum recursion depth exceeded in comparison

# To stop this from happening we can use a base condition 

def pri2(n):
    if n == 0:
        return
    print("Hello World" + str(n))
    pri2(n - 1)  # This will print "Hello World" followed by the current value of n, decrementing it each time
# pri2(5)  # This will print "Hello World" followed by 5, 4, 3, 2, 1, and then stop

# Now we will look at another video from striver's list.

def pri3(i):
    if i < 1:
        return
    print(i)
    pri3(i - 1)  
# pri3(5, 1)  # This will print numbers from 5 to 10 in reverse order

def backtracking(i,n):
    # This is the basic function for backtracking printing number from 1 -> n
    if i < 1:
        return
    backtracking(i - 1, n)  
    print(i)  # Print the current value of i after the recursive call returns

def backtracking2(i,n):
    if i > n:
        return
    backtracking2(i + 1, n) 
    print(i)
if  __name__== "__main__":
    # Uncomment the function calls below to test the code
    # pri()  # This will cause a RecursionError
    # pri2(5)  # This will print "Hello World" followed by 5, 4, 3, 2, 1
    pri3(5)  # This will print numbers from 5 to 1 in reverse order
    print("\n from here we are printing backtracking [1 -> n]")
    backtracking(5,5)  # This will print numbers from 1 to 5 in order
    print("\n from here we are printing backtracking [n -> 1]")
    backtracking2(1,5)