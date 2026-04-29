words = ["apple", "bat", "car", "banana", "dog", "cat"]
grouped = {}
for w in words:
    length = len(w)
    if length not in grouped:
        grouped[length] = []
    grouped[length].append(w)
print(grouped)