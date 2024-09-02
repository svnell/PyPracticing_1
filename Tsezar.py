def code(step, lang):
    if lang == 'ru':
        for i in input():
            if ord('а') <= ord(i) <= ord('я') - step or ord('А') <= ord(i) <= ord('Я') - step:
                print(chr(ord(i) + step), end='')
            elif ord('я') - step < ord(i) <= ord('я'):
                print(chr(ord('а') + (step - 1 - (ord('я') - ord(i)))), end='')
            elif ord('Я') - step < ord(i) <= ord('Я'):
                print(chr(ord('А') + (step - -1 - (ord('Я') - ord(i)))), end='')
            else:
                print(i, end='')
    elif lang == 'eng':
        for i in input():
            if ord('a') <= ord(i) <= ord('z') - step or ord('A') <= ord(i) <= ord('Z') - step:
                print(chr(ord(i) + step), end='')
            elif ord('z') - step < ord(i) <= ord('z'):
                print(chr(ord('a') + (step - 1 - (ord('z') - ord(i)))), end='')
            elif ord('Z') - step < ord(i) <= ord('Z'):
                print(chr(ord('A') + (step - 1 - (ord('Z') - ord(i)))), end='')
            else:
                print(i, end='')


def decode(step, lang, stringa):
    if lang == 'ru':
        for i in input():
            if ord('а') + step <= ord(i) <= ord('я') or ord('А') + step <= ord(i) <= ord('Я'):
                print(chr(ord(i) - step), end='')
            elif ord('а') < ord(i) <= ord('а') + step:
                print(chr(ord('я') - (step - 1 - (ord(i) - ord('а')))), end='')
            elif ord('А') < ord(i) <= ord('А') + step:
                print(chr(ord('Я') - (step - 1 - (ord(i) - ord('А')))), end='')
            else:
                print(i, end='')
    elif lang == 'eng':
        for i in stringa:
            if ord('a') + step <= ord(i) <= ord('z') or ord('A') + step <= ord(i) <= ord('Z'):
                print(chr(ord(i) - step), end='')
            elif ord('a') < ord(i) <= ord('a') + step:
                print(chr(ord('z') - 1 - (step - (ord(i) - ord('a')))), end='')
            elif ord('A') < ord(i) <= ord('A') + step:
                print(chr(ord('Z') - 1 - (step - (ord(i) - ord('A')))), end='')
            else:
                print(i, end='')
        print()


step = int(input())
lang = input()
mod = input()

if mod == 'code':
    code(step, lang)
elif mod == 'decode':
    stringa = input()
    for j in range(26):
        step = j
        print(step)
        decode(step, lang, stringa)
else:
    print('mod : "code" or "decode')
