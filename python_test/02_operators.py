# Topic = Operators

# 1) Predict the output
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)       # Output: True bcoz they are equal
print(a is b)       # Output: False bcoz both are different variables that have the same value
print(a is c)       # Output: True bcoz both variables points at the same item in the memory
print(17 % 5)       # Output: some int remainder
print(2 ** 3 ** 2)  # Output: 512 (a product of 2 raise to the power 9)


# 2) write a code withput using if
num = int(input("Enter your number: "))

print(num % 2 == 0, 10<= num >=50, num % 3 == 0 and num % 5 == 0)
