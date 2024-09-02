def len_finder(line: str) -> int:
    counter = 0
    for i in line:
        if i.isalpha():
            counter += 1
    return counter


def encoder(to_encode: str, step) -> str:
    new_str = ''
    for i in to_encode:
        if i.isalpha():
            c = ('a', 'A')[i.isupper()]
            new_str += chr(ord(c) + (ord(i) + step - ord(c)) % 26)
        else:
            new_str += i
    return new_str


words = input().split()
encoded_message = []
for word in words:
    encoded_message.append(encoder(word, len_finder(word)))
print(' '.join(encoded_message))
