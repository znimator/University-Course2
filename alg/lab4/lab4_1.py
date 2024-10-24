def transform_string(s):
    result = ''
    for c in s:
        if c != '*':
            result += c * 2
    return result


s = input()
print(transform_string(s))