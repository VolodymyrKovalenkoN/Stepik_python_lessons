# Напишите программу, которая определяет, состоит ли двузначное число, 
# введенное с клавиатуры, из одинаковых цифр. 
# Если состоит, то программа выводит «ДА»,
#  в противном случае программа выводит «НЕТ».

user_number = int(input("Enter a two-digit number: "))
fisrt_digit = user_number // 10
second_digit = user_number % 10
if fisrt_digit == second_digit:
    print("Yes, they are equal.")
else:
    print("No, they are differnt.")