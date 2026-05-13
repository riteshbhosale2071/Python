def bag_of_words(sentences):

    vocab = []

    # Create vocabulary
    for sentence in sentences:
        for word in sentence.lower().split():

            if word not in vocab:
                vocab.append(word)

    print("Vocabulary =", vocab)

    vectors = []

    # Create vectors
    for sentence in sentences:

        vector = []

        words = sentence.lower().split()

        for word in vocab:
            vector.append(words.count(word))

        vectors.append(vector)

    return vectors


data = [
    "I love python",
    "python is easy",
    "I love coding"
]

result = bag_of_words(data)

print("\nVectors:")
for i in result:
    print(i)