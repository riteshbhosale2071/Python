words = ["apple", "banana", "kiwi", "watermelon"]
result = max(words, key=lambda x: len(x))
print("Longest word:", result)