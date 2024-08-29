import random


def is_valid():
    while True:
        guess_num = input()
        if guess_num.isdigit():
            if 1 <= int(guess_num) <= 100:
                return guess_num
        print("Попробуй еще, нужно число от 1 до 100!")


def check(guess_num, target_num):

    if int(guess_num) > target_num:
        print('Ваше число больше загаданного, попробуйте еще разок')
    elif int(guess_num) < target_num:
        print('Ваше число меньше загаданного, попробуйте еще разок')
    else:
        print('Вы угадали, поздравляем!')
        return False
    return True


num = random.randint(1, 100)
print("Добро пожаловать в числовую угадайку")
status = True
while status:
    status = check(is_valid(), num)
    continue
print("Спасибо, что играли в числовую угадайку. Еще увидимся...")


