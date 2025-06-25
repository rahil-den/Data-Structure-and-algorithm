""" 
First pattern
*
**
***
****
*****

"""

def first_patternt(n):
    for i in range(1,n+1): # this loop is for the number of rows| lines
        for j in range(i): # this loop is for the number of columns
            print("*", end="")
        print()


"""
Second pattern
1
12
123
1234
"""

def second_pattern(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j, end="")
        print()
"""
Third pattern
1
22
333
"""
def third_pattern(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(i, end="")
        print()
"""
Fourth pattern
*****
****
***
**
*
"""

def fourth_pattern(n):
    for i in range(1,n+1):
        for j in range(n-i+1):
            print("*", end="")
        print()
"""
Fifth pattern
12345
1234
123
12
1
"""
def fifth_pattern(n):
    for i in range(1,n+1):
        for j in range(1,n-i+1):
            print(j, end="")
        print()

"""
Sixth pattern
    *    
   ***
  *****
"""
def sixth_pattern(n): 
    #space
    for i in range(1,n+1):
        for j in range(n-i+1): # we can write n-i-1 too but that will make the pattern look different 
            print(" ", end="")
            #stars
        for j in range(2*i-1):
            print("*", end="")
        print()   
"""
    *****
     ***
      *
"""
def seventh_pattern(n):
    # sum = 2 * n- (2*i-1)
    #numbers of space
    for i in range(1,n+1):
        #stars
        for j in range(i):
            print(" ", end="")
        for j in range(2 * n - (2*i-1)):
            print("*", end="")
        print()   

def eighth_pattern(n):
    sixth_pattern(n)
    seventh_pattern(n)


"""
9th pattern
*
**
***
****
***
**
*"""

"""
this one works but the pattern is not correct
def ninth_pattern(n):
    for i in range(1,2*n-1):
        stars = i
        if (i > n):
            stars = 2*n - i
            for j in range(1, stars+1):
                print("*", end="")
        else:
            for j in range(1, stars+1):
                print("*", end="")
        print()"""
def ninth_pattern(n):
    # Loop through rows: total rows = 2n - 1
    for i in range(1, 2 * n):
        # Determine the number of stars in the current row
        if i <= n:
            stars = i  # Increasing part
        else:
            stars = 2 * n - i  # Decreasing part

        # Print stars for this row
        for _ in range(stars):
            print("*", end="")

        # Move to the next line
        print()

"""
Tenth pattern
1
01 
101
0101
10101"""
"""
This one works but the pattern come sout as 01 
def tenth_pattern(n):
    start = 1
    for i in range(0, n+1):
        if(i%2 == 0):
            start = 1
        else:
            start = 0
        for j in range(0,i+1):
            print(start, end="")
            start = 1 - start # this will change the value of start from 0 to 1 and vice versa basically filp
        print()"""
def tenth_pattern(n):
    for i in range(n):
        # Start alternates based on row number
        if i % 2 == 0:
            start = 1
        else:
            start = 0
        
        for j in range(i + 1):  # Each row prints i+1 elements
            print(start, end="")
            start = 1 - start  # Flip the bit

        print()  # Move to the next line

"""
Eleventh pattern

1      1
12    21
123  321
1234 4321
1234554321"""       

def eleventh_pattern(n):
    space = 2 * (n-1)
    for i in range(1,n+1):
        # numbers
        for j in range(1,i+1):
            print(j, end="")
        # spaces
        for j in range(space):
            print(" ", end="")
        # numbers
        for j in range(i,0,-1):
            print(j, end="")
        print()
        space -= 2
          

"""
Twelth pattern
1
2 3
4 5 6
7 8 9 10
"""

def twelveth_pattern(n):
    nums = 1
    for i in range(1,n+1):
        for j in range(i):
            print(nums, end=" ")
            nums += 1
        print()
"""
Thirteenth pattern
A
AB
ABC
"""

def thirteenth_pattern(n):
    for i in range(1,n+1):
        for j in range(i):
            print(chr(65+j), end=" ") # 65 is the ascii value of A
        print()
"""
Fourteenth pattern
A B C D E
A B C D
A B C
A B
A"""

def fourteenth_pattern(n):
    for i in range(1,n+1):
        for j in range(n-i+1):
            print(chr(65+j), end=" ")
        print()
"""
Fifteenth pattern
A 
B B
C C C
D D D D
"""


def fifteenth_pattern(n):
    for i in range(1,n+1):
        # start =  A + i
        start = chr(65 + i - 1)
        for j in range(i):
            print(start, end=" ")
            # start += 1
        print()
"""
Sixteenth pattern
    A
   ABA
   ABCBA
   ABCDCBA"""

def sixteenth_pattern(n):
      for i in range(1, n + 1):
        # Print spaces
        print(" " * (n - i), end="")

        total_chars = 2 * i - 1  # Total characters to print in this row
        for j in range(1, total_chars + 1):
            if j <= i:
                # Increasing part: A, B, C...
                print(chr(64 + j), end="")
            else:
                # Decreasing part: C, B, A...
                print(chr(64 + (2 * i - j)), end="")
        print() 

"""
Seventeenth pattern
E
D E
C D E
B C D E
A B C D E
"""

def seventeenth_pattern(n):
    for i in range(n):
        start = 69 - i
        for j in range(start, 70):
            print(chr(j), end=" ")
        print()

"""
Eighteenth pattern
**********
****  ****
***    ***
**      **
*        *
*        *
**      **
***    ***
****  ****
**********
""" 

def eighteenth_pattern(n):
    iniSpace = 0
    for i in range(n):
        # stars
        for j in range(n-i):
            print("*", end="")
        # spaces
        for j in range(iniSpace):
            print(" ", end="")
        # stars
        for j in range(n-i):
            print("*", end="")
        iniSpace += 2
        print()
    space = 2*n-2 # MAXIMUM SPACE
    for i in range(n):
        for j in range(i+1): # I+1 because we need to print the stars
            print("*", end="")
        for j in range(space):  # it can work like space - 2 too.
            print(" ", end="")
        for j in range(i+1):
            print("*", end="")
        space -= 2
        print()

"""
Nineteenth pattern
*         *
**       **
***     ***
****   ****
**********
****  ****
***    ***
**      **
*        *
"""

def nineteenth_pattern(n):
    spaces = 2 * n - 2
    for i in range(1, 2 * n):  # 1 to 2n-1
        stars = i
        if i > n:
            stars = 2 * n - i
        print("*" * stars + " " * spaces + "*" * stars) # isme J wali line ko print karne ke liye humne spaces ko use kiya hai
        if i < n:
            spaces -= 2
        else:
            spaces += 2


"""
Twentieth pattern
****
*  *
*  *
****"""

# def twentieth_pattern(n):
#     for i in range(n):
#         if i == 0 or i == n-1:
#             print("*" * n)
#         else:
#             print("*" + " " * (n-2) + "*")
#     print()

#  We can also use this one and above one both are correct but the above one does not containt J Loop. Because we are printing the stars and spaces in the same line. like print("*" * stars + " " * (n-2) + "*" * stars) here n - 2 is the space.

def twentieth_pattern(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n-1 or j == 0 or j == n-1:
                print("*", end="")
            else:
                print(" ", end="")
        print()
def menu():
    print("\nChoose a pattern to print:")
    print("1. First Pattern")
    print("2. Second Pattern")
    print("3. Third Pattern")
    print("4. Fourth Pattern")
    print("5. Fifth Pattern")
    print("6. Sixth Pattern")
    print("7. Seventh Pattern")
    print("8. Eighth Pattern")
    print("9. Ninth Pattern")
    print("10. Tenth Pattern")
    print("11. Eleventh Pattern")
    print("12. Twelveth Pattern")
    print("13. Thirteenth Pattern")
    print("14. Fourteenth Pattern")
    print("15. Fifteenth Pattern")
    print("16. Sixteenth Pattern")
    print("17. Seventeenth Pattern")
    print("18. Eighteenth Pattern")
    print("19. Nineteenth Pattern")
    print("20. Twentieth Pattern")
    print("0. Exit")

if __name__ == "__main__":
    pattern_functions = {
        1: first_patternt,
        2: second_pattern,
        3: third_pattern,
        4: fourth_pattern,
        5: fifth_pattern,
        6: sixth_pattern,
        7: seventh_pattern,
        8: eighth_pattern,
        9: ninth_pattern,
        10: tenth_pattern,
        11: eleventh_pattern,
        12: twelveth_pattern,
        13: thirteenth_pattern,
        14: fourteenth_pattern,
        15: fifteenth_pattern,
        16: sixteenth_pattern,
        17: seventeenth_pattern,
        18: eighteenth_pattern,
        19: nineteenth_pattern,
        20: twentieth_pattern
    }

    while True:
        menu()
        choice = int(input("Enter your choice: "))
        if choice == 0:
            print("Exiting...")
            break
        elif 1 <= choice <= 20:
            n = int(input("Enter the number of rows: "))
            pattern_functions[choice](n)
        else:
            print("Invalid choice. Please select a number between 0 and 20.")