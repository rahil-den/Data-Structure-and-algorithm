import math
class Solution:
    def countDigit(self, n):
        if n == 0:
            return 1  # Edge case: 0 has 1 digit
        Count = 0
        while n > 0:
            lastDigit = n % 10
            print(lastDigit)  # Debugging line to see the last digit
            n = n // 10  # Use integer division
            Count += 1
        return Count
    def checkPalindDrome(self,n):
        palindrome = str(n)[::-1]
        print(palindrome)
        if n == int(palindrome):
            return True
        else:
            return False
    def checkreverse(self, n) -> int:
        reverse = 0
        if n == 0:
            return 0
        while n > 0:
            ld = n % 10
            reverse = (reverse * 10)+ld
            n = n // 10
        return reverse
    def print_divisors(self, N):
        divisor =[]
        
        sqrtn = int(math.sqrt(N))
        
        for i in range(1,sqrtn +1):
            if N % i == 0:
                divisor.append(i)
                if i != N//i:
                    divisor.append(N//i)
        divisor.sort()
        # return divisor
        print(' '.join(map(str, divisor)), end='') # Print the divisors in a single line use .join then map to convert to string
    def check_prime(self, n):
        count = 0
        for i in range(1, n+ 1):
            if n%i==0:
                count += 1
        if count == 2:
            return True
        else:
            return False
# Create object
sol = Solution()

# List of test cases
test_cases = [1,13,40,17, -123, 1000, 0,121]


# Loop through test cases
for num in test_cases:
    # print(f"1. Check PalindDROME \n Input: {num} => Output: {sol.checkPalindDrome(num)}")
    print(f"2. Check REVerse \n Input: {num} => Output: {sol.checkreverse(num)}")
    # print(f"print_divisors \n Input: {num} => Output:{sol.print_divisors(num)} ", end="")
    # print(f"3. Count Digit \n Input: {num} => Output: {sol.countDigit(num)}")
    # print(f"4. Check Prime \n Input: {num} => Output: {sol.check_prime(num)}")