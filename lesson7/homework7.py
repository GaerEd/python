# решение нашел в интернет

import sys, datetime

today = datetime.date.isoweekday(datetime.date.today())

#расписание
monday = """
1. Геометрия
2. Физкультура
3. Немецкий язык
4. Физика
5. Биология
6. Основы здоровье
7. Зарубежная литература
"""

tuesday = """
1. Химия
2. Английский язык
3. Украинский язык
4. Алгебра
5. Украинская литература
6. Информатика
7. Труды
"""

wednesday = """
1. Немецкий язык
2. Мистецтво
3. Алгебра
4. Физика
5. Правознавство
6. География
7. Всемирная история
8. Физкультура
"""

thursday = """
1. Английский язык
2. Алгебра
3. Химия
4. Зарубежная литература
5. Информатика
6. Всемирная история
7. Биология
"""

friday = """
1. Геометрия
2. Физкультура
3. Физика
4. Английский язык
5. Украинский язык
6. География
7. Украинская литература
8. Виховна година
"""
#дни недели
if today == 1:
    today_rasp = monday
    today_word = "понедельник"
if today == 2:
    today_rasp = tuesday
    today_word = "вторник"
if today == 3:
    today_rasp = wednesday
    today_word = "среда"
if today == 4:
    today_rasp = thursday
    today_word = "четверг"
if today == 5:
    today_rasp = friday
    today_word = "пятница"
if today == 6:
    today_word = "суббота"
if today == 7:
    today_word = "воскресенье"

#начало
while True:
    #приветствие
    print("""Расписание уроков 9-Б класа
#### ЗОШ I-III ст. №4""")

    #today
    value = int(input("Сегодня " +today_word+ ".Выдать расписание уроков на сегодня?\n1 - да\n2 - нет\n"))
    if value == 1:
        print(today_rasp)
    if value == 2:
        value = int(input("1 - Выдать расписание уроков на завтра\n2 - Расписание уроков на определённый день\n"))
        if value == 1:
            today +=1
            print(today)
            print("Завтра", today_word, "\n", today_rasp)
            today -=1
        if value == 2:
            value = int(input("1. Понедельник\n"))