num = int(input("please enter value: "))
end = int(input("please enter end value: "))
end += 1
for i in range(1, end):
    multiple = num * i
    print(multiple)
