data = ["9876543210", "12345", "abcd123456", "9998887776", "123456789"]
valid = list(filter(lambda x: x.isdigit() and len(x) == 10, data))
print(valid)