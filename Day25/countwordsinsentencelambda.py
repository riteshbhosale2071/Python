sentence = "Python is very easy to learn"
count = (lambda s: len(s.split()))(sentence)
print("Word count:", count)