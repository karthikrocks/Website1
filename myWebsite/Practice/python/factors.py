val1 = 244
loop_num = 1
end_num = int(val1 / 2)
factors = []
for i in range(loop_num, end_num):
    if val1 % i == 0:
        factors.append(i)
factors.append(val1)
print(factors)