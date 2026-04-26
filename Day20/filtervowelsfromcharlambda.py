S=['a','c','e','o','H','I']
print("Characters:",S)
res=filter(lambda a:a in 'aeiouAEIOU', S)
print("Vowels in characters are",list(res))