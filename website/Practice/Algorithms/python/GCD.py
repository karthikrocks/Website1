num1 = 12
num2 = 35
greatest = max(num1, num2)
smallest = min(num1, num2)
remainder = greatest % smallest
while remainder != 0:
    smallest = remainder
    greatest = num1
    remainder = greatest % smallest

print(smallest)
