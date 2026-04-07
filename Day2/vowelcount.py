word=input("Enter any word: ")
count=0
vowels="aeiouAEIOU"
for i in word:
    if i in vowels:
        count=count+1
print(f"{word} has {count} vowels")