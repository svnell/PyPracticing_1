n = input()
count = 0
for i in n:
    count += ord(i) * 3
print("Текст сообщения: '" + n + "'")
print("Стоимость сообщения:", str(count) + '🐝')
