import random


def is_valid():
    while True:
        usr_name = input('Как тебя зовут?\n')
        if usr_name.isalpha():
            return usr_name
        print('Людей так не зовут, давай попробуем еще рай, друг:')


def ball_job(usr_name):
    input(f'{usr_name.title()}, какой у тебя вопрос?\n')
    print(random.choice(ansrs))
    return input('Остались вопросы?\n').lower()


ansrs = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да', 'Можешь быть уверен в этом',
         'Мне кажется - да', 'Вероятнее всего', 'Хорошие перспективы', 'Знаки говорят - да', 'Да',
         "Пока неясно, попробуй снова", 'Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать',
         'Сконцентрируйся и спроси опять', 'Даже не думай', 'Мой ответ - нет', 'По моим данным - нет',
         'Перспективы не очень хорошие', 'Весьма сомнительно'
         ]

print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
name = is_valid()
print(f'Привет, {name.title()}!', sep='\n')
while True:
    if ball_job(name) in ['да', 'da']:
        continue
    else:
        print('Возвращайся если возникнут вопросы!')
        break