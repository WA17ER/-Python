# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима,
# весна, лето, осень). Напишите решения через list и через dict


user_month = int(input('Введите номер месяца '))
month_dict = {'Winter': [1, 2, 12], 'Spring': [3, 4, 5], 'Summer': [6, 7, 8], 'Autum': [9, 10, 11]}
for key, value in month_dict.items():
    if user_month in month_dict[key]:
        print(key)
    else:
        pass

month_list = [None, 'Winter', 'Winter', 'Spring', 'Spring', 'Spring', 'Summer', 'Summer', 'Summer', 'Autum',
              'Autum', 'Autum', 'Winter']

print(month_list[user_month])
