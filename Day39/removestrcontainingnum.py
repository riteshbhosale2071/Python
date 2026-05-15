def remove():
    t = ("hello", "abc123", "python", "test99")

    clean = []

    for word in t:
        has_digit = False

        for ch in word:
            if ch.isdigit():
                has_digit = True
                break

        if not has_digit:
            clean.append(word)

    print(tuple(clean))

remove()