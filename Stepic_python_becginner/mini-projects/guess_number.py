from random import randint

def is_valid(number):
    if number.isdigit() and 1 <= int(number) <= 100:
        return True
    else:
        return False

rand_number = randint(1, 100)
print('Добро пожаловать в числовую угадайку')
while True:
    guest = input("Enter your number: ")
    if not is_valid(guest):
        print('А может быть все-таки введем целое число от 1 до 100?')
        continue
    else:
        guest = int(guest)
        if guest == rand_number:
            print("Вы угадали, поздравляем!")
            break
        elif guest > rand_number:
            print("Ваше число больше загаданного, попробуйте еще разок")
            continue
        else:
            print("Ваше число меньше загаданного, попробуйте еще разок")
            continue
print("Спасибо, что играли в числовую угадайку. Еще увидимся...")