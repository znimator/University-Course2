with open('alg/lab6/input2.txt', 'r') as f:
    text = f.read()
    words = set(word.lower() for word in text.split())
    words = sorted(words)
    with open('alg/lab6/output2.txt', 'w') as f:
        for word in words:
            f.write(word + '\n')
