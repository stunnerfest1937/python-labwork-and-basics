def new_func():
    n = int(input("enter the number till which sum is to be found: "))
    return n

n = new_func()
sum_value = 0

for j in range(1, n + 1):
 sum_value += j

print("sum is", sum_value)
