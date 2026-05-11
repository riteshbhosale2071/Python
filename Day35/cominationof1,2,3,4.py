def find():
    nums = [1, 2, 3, 4]

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            print(nums[i], nums[j])

find()