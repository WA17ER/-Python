# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 +
# 33 + 333 = 369.

user_score = input('Введите число ')
result = int(user_score) + int(user_score*2) +int(user_score*3)
print(result)