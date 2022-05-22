# Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.
user_score = int(input('Введите количество секунд '))
hours = user_score//3600
minuts = (user_score//60)%60
secunds = (user_score%60)%60
print(hours, minuts, secunds)