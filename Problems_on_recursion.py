# Print Name n times using recursion
class Name:
    def getName(self,i:int,n:int) -> int:
        if (i > n):
            print("Test...Test...")
            return self.getName(i+1,n)
        else:
            print("Not Test...")
            
# sol = Name()
# print("Get Ans:",sol.getName(2,1))

# Print Linearly form 1 to N
# return i on above code during i > n


# Print in terms of N -> 1
class Name:
    def getName(self, i: int) -> None:
        if i < 1:
            return
        print(i, "Test...Test...")
        self.getName(i - 1)

# Example usage:
sol = Name()
sol.getName(5)

# Parameterised and Functional Recursion

print("Parameterised and Functional Recursion")

class parameterised:
    def getName(self, i: int, sum: int) -> None:
      if i<1:
        print("Sum is:", sum)
        return
      sum += i
      self.getName(i-1,sum)

# Reverse an array using recursion

# arr = [1,3,2,4,4]

# l and r is the index of array

class ReverseArray:
    def reverse(self,l:int,r:int,arr:list):
        if l >= r:
            return
        arr[l], arr[r] = arr[r], arr[l]
        self.reverse(l + 1, r - 1,arr)

arr = [1, 3, 2, 4, 4]
arrayGet = ReverseArray()
# l(starting index) and r(ending index) is the index of array
arrayGet.reverse(0, len(arr) - 1, arr)
print("<===== ReverseArray =====>", arr)


# Palindrome Check Using Recursion:

class PalindromeCheck:
    def is_palindrome(self, s: str, left: int, right: int) -> bool:
        if left >= right:
            return True
        if s[left] != s[right]:
            return False
        return self.is_palindrome(s, left + 1, right - 1)

word = "madam"
checker = PalindromeCheck()
result = checker.is_palindrome(word, 0, len(word) - 1)
print(f"'{word}' is a palindrome? ->", result)

#  Multiple Recursion Calls

class MultipleRecursion:
    def fibonacci(self, n: int) -> int:
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fibonacci(n - 1) + self.fibonacci(n - 2)
        


# Hashing | Maps | Time Complexity | Collisions | Division Rule of Hashing

class HashingExample:
    def getNumber(self,num:int,arr:list) -> int:
        count = 0
        for i in range(len(arr)):
            if arr[i] == num:
                count += 1
        return count
    
    def getHash(self,arr:list) -> dict:
        hash_map = {}
        for num in arr:
            if num in hash_map:
                hash_map[num] += 1

            else:
                hash_map[num] = 1
        return hash_map

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4]   
data = HashingExample()
result = data.getHash(arr)
print("Frequencies:", result)
