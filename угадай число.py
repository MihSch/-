from random import randint

count_game = int()
count_win = int()
count_non = int()

print('''
------Правила игры "Угадай число"------
         Дается три попытки.
        Победа достается тем 
        счастливчикам, которые
       угадали число от 1 до 2 
             все три раза.
                Удачи!
    ''')

while count_game < 3:

    num_rand = randint(1, 2)
    num_in = int(input('\n Угадайте число от 1 до 2: \n'))
    count_game += 1
    if num_rand == num_in:
        print('Угадали')
        count_win += 1
    else:
        print('Не угадали')
        count_non += 1

if count_win == 3:
    print('\n You ROCK \n')
else:
    print('\n ПОТРАЧЕНО \n')
print(f'Статистика: Угадано {count_win} раз(а), не угадано {count_non} раз(а)')
