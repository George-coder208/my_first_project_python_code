from random import randint, choice, seed
from time import time
atk = 15
hp = 100
time_for_fight = 10
artefakty = []
seed(1)
print ('О! Путник! в наших краях это редкость, как я могу к вам оброщатся?') # приветствие
name = input()
print ('ммммм... понятно,\nНу раз уж я тебя здесь нашёл, то обучу чуть-чуть,\n ну все познаётся на практики, ты готов?')
if input('(пиши "да" если хочешь жить)\n') != 'да':
    print('(тебя сьела агрессивная лягушка, пока:))')

    exit(0)
print ('Теперь первое сражение,\nО! вот как раз! агресивная легушка')
if input("Подойдет?\n") != "да":
    print('ну тогда не знаю, ой! (тебя сьела агрессивная лягушка, пока:))')
    exit (0)
hp_mob_s = 100
mob_atak = 20
r_number = randint(1,10)
r_number2 = randint(1,10)
r_choise = choice (["+","-"])
print (r_number, r_choise, r_number2, '= ?' )
result = r_number + r_number2 if r_choise == '+' else r_number - r_number2
n_time = time()
wrong_resualt = int(input())
p_time = time()
your_atk = ((time_for_fight - int(p_time - n_time)) * atk)
hp_mob_f = hp_mob_s-your_atk

if wrong_resualt != result:
    print('(тебя сьела агрессивная лягушка, пока:))')
    exit(0)
while hp_mob_f >= 0:
    hp = hp - mob_atak
    r_number = randint(1, 10)
    r_number2 = randint(1, 10)
    r_choise = choice(["+", "-"])
    print(r_number, r_choise, r_number2, '= ?')
    result = r_number + r_number2 if r_choise == '+' else r_number - r_number2
    n_time = time()
    wrong_resualt = int(input())
    p_time = time()
    your_atk = ((time_for_fight - int(p_time - n_time)) * atk)
    hp_mob_f = hp_mob_f - your_atk
    if wrong_resualt != result or hp <= 0:
        print('(тебя сьела агрессивная лягушка, пока:))')
        exit(0)
print ('поздравляю враг повержин')
print (f'Вот ты и получил первый опыт "{name}" хи-хи-хи\nА и еще, хотел тебе вручить вот этот артефакт,\nвозможно он тебе пригодится\n(тебе вручают "Лесной артефакт")')
artefakty.append('Лесной артефакт')
print ('лесной артефакт дает + 50 к здоровью')
hp = hp + 50
print ('ПОЗДРАВЛЯЮ С ПРОХОЖДЕНИЕМ ПЕРВОГО ЭТАПА')
#------------------------------------------------1 этап 'обучение закончин'---------------------------------------------
if input ('готовы продолжать?\n') == 'да':
    print ('тогда начнем наше ЛЕСНОЕ ИСПЫТАНИЕ')
else:
    print ('вас догнали сородичи агресскивной лягушки')
    exit(0)
a = input ('как ты пойдешь через заросли или по ровнине? (пишите "по ровнине" или "через заросли")\n')
if a == 'через заросли':
    print('ты пробираешься через заросли\nно что это там? новый противник МАГИЧЕСКАЯ ЛИСА')
    if input('вы готовы?\n') != 'да':
        print('тебя догнало все семейство агрессивных лягушек')
        exit(0)
    hp_mob = 200
    mob_atak = 20
    r_number = randint(1, 10)
    r_number2 = randint(1, 10)
    r_choise = choice(["+", "*", "/", "-"])
    print(r_number, r_choise, r_number2, '= ?')
    if r_choise == '+':
        result = r_number + r_number2
    elif r_choise == '*':
        result = r_number * r_number2
    elif r_choise == '/':
        result = r_number / r_number2
    else:
        result = r_number - r_number2
    n_time = time()
    wrong_resualt = int(input())
    p_time = time()
    your_atk = ((time_for_fight - int(p_time - n_time)) * atk)
    if wrong_resualt != result or hp <= 0:
        print('(тебя сьела магическая лиса, пока:))')
        exit(0)
    while hp_mob > 0:
        hp = hp - mob_atak
        print('лиса снесла вам 25 здоровья')
        r_number = randint(1, 10)
        r_number2 = randint(1, 10)
        r_choise = choice(["+", "*", "/", "-"])
        print(r_number, r_choise, r_number2, '= ?')
        if r_choise == '+':
            result = r_number + r_number2
        elif r_choise == '*':
            result = r_number * r_number2
        elif r_choise == '/':
            result = r_number / r_number2
        else:
            result = r_number - r_number2
        n_time = time()
        wrong_resualt = int(input())
        p_time = time()
        your_atk = ((time_for_fight - int(p_time - n_time)) * atk)
        hp_mob = hp_mob - your_atk
        if wrong_resualt != result or hp <= 0:
            print('(тебя сьела магическая лиса, пока:))')
            exit(0)
    print('поздравляю вы победили магическую лису')
    if input("осмотреть поле боя?\n") == 'да':
        chance = randint(0, 100)
        if chance < 75:
            artefakty.append('клык лисы')
            atk = atk + 10
            print ('вы нашли артефакт клык лисы, + 10 к атаке')
        else:
            print("вы не чего не нашли")
    else:
        print("ты пошел дальше")
elif a == 'по ровнине':
    print('ты долго идешь и вдруг видешь разьеренного лесног кабана')
    hp_mob = 200
    mob_atak = 20
    r_number = randint(1, 10)
    r_number2 = randint(1, 10)
    r_choise = choice(["+", "-"])
    print(r_number, r_choise, r_number2, '= ?')
    if r_choise == '+':
        result = r_number + r_number2
    else:
        result = r_number - r_number2
    n_time = time()
    wrong_resualt = int(input())
    p_time = time()
    your_atk = ((time_for_fight - int(p_time - n_time)) * atk)
    if wrong_resualt != result or hp <= 0:
        print('(тебя сьел лесной кабан, пока:))')
        exit(0)
    while hp_mob > 0:
        hp = hp - mob_atak
        r_number = randint(1, 10)
        r_number2 = randint(1, 10)
        r_choise = choice(["+", "-"])
        print(r_number, r_choise, r_number2, '= ?')
        if r_choise == '+':
            result = r_number + r_number2
        else:
            result = r_number - r_number2
        n_time = time()
        wrong_resualt = int(input())
        p_time = time()
        your_atk = ((time_for_fight - int(p_time - n_time)) * atk)
        if wrong_resualt != result or hp <= 0:
            print('(тебя сьел лесной кабан, пока:))')
            exit(0)
else:
    print('ты реально никуда не хочешь? тогда пока:)\n(тебя съели агрессивные лягушки вместе с кокосами)')
    exit(0)