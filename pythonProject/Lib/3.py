# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух
# аргументов

def my_func(var1, var2, var3):
    return sum(sorted([var1,var2,var3], reverse=True)[:-1])

result = my_func(12, 10, 97)
print(result)
