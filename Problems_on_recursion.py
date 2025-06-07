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



