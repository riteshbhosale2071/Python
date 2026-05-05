def sum(num):
    previous=0
    for i in range(num):
        sum=previous+i
        print(f"The current num is {i}, previous num was {previous} and sum of num is {sum}")
        previous=i
sum(10)