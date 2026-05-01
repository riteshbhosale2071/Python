data = ["abc@gmail.com", "hello", "test@yahoo.com", "123", "user@outlook.com"]
emails = list(filter(lambda x: "@" in x, data))
print(emails)