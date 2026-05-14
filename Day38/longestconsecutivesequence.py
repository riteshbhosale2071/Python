def find():
    t = (1, 9, 3, 10, 4, 20, 2)

    nums = set(t)
    longest = 0

    for num in nums:
        if num - 1 not in nums:
            current = num
            count = 1

            while current + 1 in nums:
                current += 1
                count += 1

            longest = max(longest, count)

    print("Longest Consecutive Length:", longest)

find()