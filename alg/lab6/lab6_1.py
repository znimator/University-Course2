with open('alg/lab6/input1.txt', 'r') as f:
    s = f.read()

result = ''.join([s[i] for i in range(0, len(s), 2)])

with open('alg/lab6/output1.txt', 'w') as f:
    f.write(result)
