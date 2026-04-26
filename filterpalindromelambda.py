L=['radar','world','madam','hello']
print("List:",L)
res=list(filter(lambda x: x == x[::-1],L))
print("Palindrome num in list are",res)