"""
Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды
и выведите в формате чч:мм:сс. Используйте форматирование строк.
"""

seconds = int(input('Введите время в секундах\n>>>'))
hours = seconds // 3600
minutes = (seconds % 3600) // 60
seconds_new = (seconds % 60)

if minutes < 10:
    minutes = str(minutes)
    minutes = '0' + minutes
if seconds_new < 10:
    seconds_new = str(seconds_new)
    seconds_new = '0' + seconds_new


result = f'{seconds} секунд это (чч:мм:сс): {hours}:{minutes}:{seconds_new}'
print(result)
