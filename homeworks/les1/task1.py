"""
Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя
несколько чисел и строк и сохраните в переменные, выведите на экран.
"""

print('Шуточный тест: ваша темная тайна\nВсе ответы надо вводить на русском')
months = {
    'январь': 'енотов',
    'февраль': 'чебурашек',
    'март': 'всех',
    'апрель': 'тушканчиков',
    'май': 'пожарных',
    'июнь': 'муравьев',
    'июль': 'испанцев',
    'август': 'несогласных',
    'сентябрь': 'тараканов',
    'октябрь': 'гусей',
    'ноябрь': 'утконосов',
    'декабрь': 'слоников',
}
letters = {
    'а': 'Вы ищите',
    'б': 'Вы бреете ',
    'в': 'Вы гладите',
    'г': 'Вы целуете',
    'д': 'Вы обнимаете',
    'е': 'Вы моете',
    'ж': 'Вы кусаете',
    'з': 'Вы обижаете',
    'и': 'Вы грызете',
    'к': 'Вы вспоминаете',
    'л': 'Вы любите',
    'м': 'Вы ненавидите',
    'о': 'Вы кидаете',
    'п': 'Вы смешите',
    'р': 'Вы катаете',
    'с': 'Вы понимаете',
    'т': 'Вы презираете',
    'у': 'Вы развлекаете',
    'ф': 'Вы пылесосите',
    'х': 'Вы крадете',
    'ш': 'Вы укрощаете',
    'э': 'Вы защищаете',
    'ю': 'Вы похищаете',
    'я': 'Вы собираете',
    'н': 'Вы коллекционируете',
}
colors = {
    'белый': 'потому что Вам скучно',
    'черный': 'потому что Вам страшно',
    'синий': 'потому что Вам это нравится',
    'красный': 'потому что Вас заставили',
    'оранжевый': 'потому что так хотят Ваши друзья',
    'желтый': 'потому что не знаете почему',
    'зеленый': 'потому что Вам все надоело',
    'голубой': 'потому что это зависимость ',
    'фиолетовый': 'потому что хотите спать',
    'розовый': 'потому что влюбились',
    'коричневый': 'потому что устали от всего',
 }
name = (input('Введите Ваше имя:\n >>> '))
month = (input('Месяц, в котором вы родились?\n >>> ')).lower()
color = (input('Ваш любимый цвет:\n>>> ')).lower()
age = (input('Ваш возраст:\n>>> '))
letter = name[0].lower()
result = f'{name}, {letters[letter]} {months[month]}, {colors[color]}. А ведь Вам уже {age}!'
print(result)
