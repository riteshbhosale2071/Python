L=["apple", "banana", "orange", "grape", "elephant"]
print("List:",L)
res=filter(lambda a:a[0].lower() in 'aeiouAEIOU', L)
print("Words starting with vowel are",list(res))