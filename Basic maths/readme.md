
# DSA Practice ReadMe

<!-- --- -->

### 📚 Currently Learning:
**Pattern Problems in Python**

---

### 📁 File Descriptions:

1. **Patterns.py**  
   This file includes all the patterns (mostly star and number-based). It's for practicing different pattern-based problems often asked in coding rounds.

2. **Basic_maths.py**  
   This file includes basic mathematical helper methods for solving programming questions.  
   🔑 The key method is for extracting digits or manipulating numbers.

---

### 🔧 Template Code Snippet for Extracting the digits

```python
 #TODO:
 if n == 0:
            return 1  # Edge case: 0 has 1 digit
        Count = 0
        while n > 0:
            lastDigit = n % 10
            print(lastDigit)  # Debugging line to see the last digit
            n = n // 10  # Use integer division
            Count += 1
````


