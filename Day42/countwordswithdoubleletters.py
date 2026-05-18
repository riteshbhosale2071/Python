def find():
    t = ("apple", "banana", "cat", "coffee")

    count = 0

    for word in t:

        for i in range(len(word) - 1):

            if word[i] == word[i + 1]:
                count += 1
                break

    print("Words with Double Letters:", count)

find()