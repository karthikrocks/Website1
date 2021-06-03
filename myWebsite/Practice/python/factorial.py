num = int(input("please enter value: "))
ans = []
ans.append(num)
ans.append(num - 1)
for i in range(2, num):
    num -= 1
    result = int(num - 1)
    ans.append(result)
total = 1
for x in ans:
    total *= x
print(f'Factorial is', total)