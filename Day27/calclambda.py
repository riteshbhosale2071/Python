calc = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b
}
a = 10
b = 5
op = '+'
result = calc[op](a, b)
print("Result:", result)