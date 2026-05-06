def perfect(num):
    total = 0
    for i in range(1, num):
        if num % i == 0:
            total += i
    return total == num

print("Perfect numbers between 1 and 1000 are:")
for n in range(1, 1001):
    if perfect(n):
        print(n)