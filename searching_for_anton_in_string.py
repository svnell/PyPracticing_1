def indexer(word: str, letter: str, j: int, shift: int):
    if letter[j] in word[shift:]:
        if j == len(letter) - 1:
            return True
        else:
            return indexer(word, letter, j + 1, shift + word[shift:].index(letter[j]))
    return False


frigers = [input().lower() for _ in range(int(input()))]
anton = 'anton' #решение не привязано к статике, при желании можно "антона" заинпутить
i = 0
j = 0
for line in range(len(frigers)):
    if indexer(frigers[line], anton, j, i):
        print(line + 1, end=' ')