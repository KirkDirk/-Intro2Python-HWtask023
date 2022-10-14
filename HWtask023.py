# Создайте программу для игры в ""Крестики-нолики"".
import random
game_mode = int(input('Выберите режим игры: 1 - human, 2 - bot, 3 - skynet: '))
gamer1 = input('Введите имя первого игрока: ')
if game_mode == 1: gamer2 = input('Введите имя второго игрока: ')
if game_mode == 2: gamer2 = 'Bot'
if game_mode == 3: gamer2 = 'Skynet'

# формируем очередность игроков 
list_gamers = [gamer1, gamer2]
list_gamers[0] = random.choice(list_gamers)
if list_gamers[0] == gamer1:
    list_gamers[1] = gamer2
else: list_gamers[1] = gamer1
print('Играют в Крестики-нолики: ', gamer1, ' и ', gamer2, '. Первым будет ходить - ', list_gamers[0])

# играем
listXO = []
print(
    '-------\n'
    '| | | |\n'
    '-------\n'
    '| | | |\n'
    '-------\n'
    '| | | |\n'
    '-------\n'    
)