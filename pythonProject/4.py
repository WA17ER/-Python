# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл
# while и арифметические операции.
user_score = int(input('Введите целое число '))
score = 0
while user_score % 10 > 0:
    if score < user_score % 10:
        score = user_score % 10
        pass
    else:
        pass
    user_score //= 10

print(score)