sentence = "Python is very easy"
print(sentence)
result = (lambda s: " ".join(s.split()[::-1]))(sentence)
print(result)