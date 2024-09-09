#def new_format(stg, letter_to_delete):
#return new_format
def deleter(stringa: str, i):
    new_stringa = stringa
    if new_stringa == '  ':
        return ''
    else:
        for s in stringa:
            if chr(i) in new_stringa:
                if s == chr(i):
                    new_stringa = new_stringa.replace(s, '')
                    return deleter(new_stringa, i + 1)
                print(new_stringa + f' + {chr(i-1)}')
                return deleter(new_stringa, i + 1)


stg = input().lower() + ' запретил букву'
i = 1072
deleter(stg, i)



