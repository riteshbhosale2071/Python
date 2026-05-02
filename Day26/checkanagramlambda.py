s1 = "listen"
s2 = "silent"
check = lambda a, b: sorted(a) == sorted(b)
print("Anagram" if check(s1, s2) else "Not Anagram")