raiting = [1,4,6,8]
user_val = int(input('Введите число '))
raiting.append(user_val)
print(sorted(raiting, reverse=True))