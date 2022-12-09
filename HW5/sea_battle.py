#создает 2-д список списков заполняя все значения образцом
def create_2d_array_by_sample(xsize, ysize, sample):
    result = [0] * xsize
    for i in range(0, xsize):
        result[i] = [sample] * ysize
    return result

# просто пара методов для красивого вывода
def print_map(input_array: list):
    print("  ", end = "")
    print("   A      B      C      D      E      F      G      H      I      J")
    for i in range(0,10):
        print(str(i) + " ", end="")
        print((input_array[i]))

def print_field(comp_map: list, player_map: list):
    print_map(comp_map)
    print("СВЕРХУ МОЕ ПОЛЕ\n ----------------------------------------------------------------------- \nСНИЗУ - ТВОЕ ПОЛЕ")
    print_map(player_map)

#проверяет соответствие переданной строки шаблону координат: 2 знака, из которых 1 - цифра, другой - англ буква от A до J
def check_coordinates_validity(coordinates_str: str, letters_vocabulary = "ABCDEFGHIJabcdefghij"):
    digits = "0123456789"
    if len(coordinates_str) != 2: return False
    if digits.find(coordinates_str[0]) != -1:
        if digits.find(coordinates_str[1]) != -1: return False
        elif letters_vocabulary.find(coordinates_str[1]) == -1: return False
        else: return True
    elif digits.find(coordinates_str[1]) != -1:
        if letters_vocabulary.find(coordinates_str[0]) == -1: return False
        else: return True
    return False

#считывает координаты с проверкой шаблона
def read_coordinates(prompting_msg = "Введи координаты - ", err_msg = "некорректные координаты"):
    horisontal_placement = "ABCDEFGHIJ"
    coordinates_str = check_quit(str(input(prompting_msg)))
    while not check_coordinates_validity(coordinates_str):
        print(err_msg)
        coordinates_str = check_quit(str(input(prompting_msg)))
    coordinates_str = coordinates_str.upper()
    if coordinates_str[0].isdigit():
        position = (int(coordinates_str[0]),horisontal_placement.find(coordinates_str[1]))
    else:
        position = (int(coordinates_str[1]),horisontal_placement.find(coordinates_str[0]))
    return position

#считывает направвление, с учетом шаблона
def read_direction(prompting_msg = "Введи направление корабля - ", err_msg = "некорректное направление (up/down/left/right)", directions_vocabulary = "updownleftrightUPDOWNLEFTRIGHT"):
    direction = check_quit(str(input(prompting_msg)))
    while directions_vocabulary.find(direction) == -1:
        print(err_msg)
        direction = check_quit(str(input(prompting_msg)))
    return direction.lower()

#проверка допустимости расположения корабля.
def check_ship_placement(start_pos: tuple, size: int, direction: str, map: list):
    check_zone = [(-1,-1),(-1,-1)]
    #check_zone - левая верхняя и правая нижняя точка прямоугольника, который надо проверить на пересечения с др кораблями, сложенные в лист кортежей
    #check_zone формируется как плюс 1 клетка в каждую стоорону, либо край карты

    #сначала проверяем влезает ли сам корабль просто по размеру до края доски и если влезет - формируем для него зону проверки
    if direction == "up":
        if start_pos[0]+1 < size: return False
        check_zone = [(max(0,start_pos[0] - size),max(0,start_pos[1] - 1)),(min(len(map) - 1,start_pos[0] + 1),min(len(map) - 1,start_pos[1] + 1))]
    elif direction == "down":
        if len(map)-start_pos[0] < size: return False
        check_zone = [(max(0,start_pos[0] - 1),max(0,start_pos[1] - 1)),(min(len(map) - 1,start_pos[0] + size),min(len(map) - 1,start_pos[1] + 1))]
    elif direction == "right":
        if len(map[start_pos[0]])-start_pos[1] < size: return False
        check_zone = [(max(0,start_pos[0] - 1),max(0,start_pos[1] - 1)),(min(len(map) - 1,start_pos[0] + 1),min(len(map) - 1,start_pos[1] + size))]
    elif direction == "left":
        if start_pos[1] + 1 < size: return False
        check_zone = [(max(0,start_pos[0] - 1),max(0,start_pos[1] - size)),(min(len(map) - 1,start_pos[0] + 1),min(len(map) - 1,start_pos[1] + 1))]
    else: return False #Если вдруг сюда прокралось некорректное указание направления - возвращаем Ложь

    #теперь собственно проверяем check_zone на отсутствие пересечений с другими кораблями, если она была сформирована
    if check_zone[0][0] != -1:
        for i in range(check_zone[0][0],check_zone[1][0]+1):
            for j in range(check_zone[0][1],check_zone[1][1]+1):
                if map[i][j] != "   ": return False
        return True
    else: return False

#проверяем все вводы строк на выражение волеизъявления пользователя прекратить игру
def check_quit(input_str: str):
    if input_str.find("quit") != -1 or input_str.find("exit") != -1: exit()
    else: return input_str

#ставит корабль с заданным размером, по заданным координатам и направлению
def place_ship(start_pos: tuple, size: int, direction: str, map: list):
    if not check_ship_placement(start_pos, size, direction, map): return map
    else:
        if direction == "up":
            for i in range(0, size):
                map[start_pos[0]-i][start_pos[1]] = " O "
            return map
        if direction == "down":
            for i in range(0, size):
                map[start_pos[0]+i][start_pos[1]] = " O "
            return map
        if direction == "right":
            for i in range(0, size):
                map[start_pos[0]][start_pos[1]+i] = " O "
            return map
        if direction == "left":
            for i in range(0, size):
                map[start_pos[0]][start_pos[1]-i] = " O "
            return map


#ставит заданное количество кораблей заданного размера в случайных координатах
def place_random_ship_Xtimes(size: int, number_of_ships: int, map: list):
    import random
    directions = ["up", "down", "left", "right"]
    for i in range(0, number_of_ships):
        start_pos = (random.randint(0,9),random.randint(0,9))
        direction = directions[random.randint(0,3)]
        while not check_ship_placement(start_pos, size, direction, map):
            start_pos = (random.randint(0,9),random.randint(0,9))
            direction = directions[random.randint(0,3)]
        map = place_ship(start_pos, size, direction, map)
    return map

#выставляет стандартный набор кораблей (1 трехпалубник, 2 двухпалубника, 3 буйка) в случайных местах полученной карты
def place_standart_ships(map: list):
    map = place_random_ship_Xtimes(1, 3, map)
    map = place_random_ship_Xtimes(2, 2, map)
    map = place_random_ship_Xtimes(3, 1, map)
    return map

#проверяет все ли корабли подбиты на карте
def check_defeat(map: list):
    for i in range(0,len(map)):
        for j in range(0,len(map[i])):
            if map[i][j] == " O ": return False
    return True


#!!!собственно тело программы начинается здесь!!!

#делаем 3 поля: 1 - компа (сразу его наполяем стандартными кораблями), 1 - игрока, 1 - отмечать выстрелы игрока
player_map = create_2d_array_by_sample(10,10, "   ")
comp_map = create_2d_array_by_sample(10,10, "   ")
shot_map = create_2d_array_by_sample(10,10, "   ")
comp_map = place_standart_ships(comp_map)

print("\nМорской Бой v1.0. Для выхода введите exit или quit.\n\n")
print("Привет! Как тебя зовут?")
player_name = check_quit(input())
print(player_name + ", сыграем в морской бой? Y/N ")
if (input().upper()) not in ["ДА", "YES", "Y", "ДАВАЙ"]:
    print("Ну тогда до скорого, трусишка " + player_name + "!")
    exit()
print("Вот твое поле, " + player_name + ". Расставляй корабли (я не буду подсматривать, честно!)")
print_map(player_map)
print("Вводи два знака: букву (A - J) и цифру (0 - 9)")
horisontal_placement = "ABCDEFGHIJ"

#расставляем однопалубники
for i in range(0,3):
    start_pos = read_coordinates("Вводи координаты однопалубника - ")
    while not check_ship_placement(start_pos, 1, "up", player_map):
        print("некорректное расположение корабля")
        start_pos = read_coordinates("Вводи координаты трехпалубника - ")
    player_map = place_ship(start_pos, 1, "up", player_map)
    print_map(player_map)
    
#расставляем двухпалубники
for i in range(0,2):
    start_pos = read_coordinates("Вводи координаты двухпалубника - ")
    direction = read_direction()
    while not check_ship_placement(start_pos, 2, direction, player_map):
        print("некорректное расположение корабля")
        start_pos = read_coordinates("Вводи координаты трехпалубника - ")
        direction = read_direction()
    player_map = place_ship(start_pos, 2, direction, player_map)
    print_map(player_map)

#ставим 1 трехпалубник
start_pos = read_coordinates("Вводи координаты трехпалубника - ")
direction = read_direction()
while not check_ship_placement(start_pos, 3, direction, player_map):
    print("некорректное расположение корабля")
    start_pos = read_coordinates("Вводи координаты трехпалубника - ")
    direction = read_direction()

player_map = place_ship(start_pos, 3, direction, player_map)
print_map(player_map)
print("Корабли расставлены. К Бою!")

#флаги для контроля течения и завершения игры
comp_win = False
player_win = False
player_turn = True #игрок ходит первым

#список действий для компа. реализация - ниже                   #TODO: comp logic to finish off previously hit ships
decision_list = {"first_diag": False, "second_diag": False, "finishing meal": (-1,-1), "cheating bastard": False}
                                                                #TODO: cheating comp logic, where comp finds player's ships
turns_counter = 1

#цикл самой игры идет, пока никто не выиграл
while comp_win == False and player_win == False:
    print("Ход №" + str(turns_counter))
    print_field(shot_map, player_map)
    while player_turn:
        player_turn = False

        #считываем с игрока координаты выстрела, отмечаем его на двух картах (компа и выстрелов)
        shot_pos  = read_coordinates("Твой выстрел - ")
        if comp_map[shot_pos[0]][shot_pos[1]] == " O ":
            print("Попал!")                             #TODO:ввести дифференциированный ответ "РАНИЛ"/"УБИЛ" через check_zone
            comp_map[shot_pos[0]][shot_pos[1]] = " 8 "
            shot_map[shot_pos[0]][shot_pos[1]] = " 8 "
            player_turn = True # если попал - снова стреляешь
        elif comp_map[shot_pos[0]][shot_pos[1]] == "   ":
            print("Мимо!")
            comp_map[shot_pos[0]][shot_pos[1]] = " X "
            shot_map[shot_pos[0]][shot_pos[1]] = " X "
        print_field(shot_map, player_map)

        #проверяем, на случай, если этим залпом был подбит последний корабль компа
        if check_defeat(comp_map):
            player_win = True
            break

    while not player_turn:
        player_turn = True
        #Перебираем доступные нам логики в заданном порядке

        #Логика простреливания первой диагонали
        if not decision_list["first_diag"]:
            for i in range(0,10):
                if player_map[i][i] != " 8 " and player_map[i][i] != " X ":
                    shot_pos = (i,i)
                    if shot_pos[1] == 9:
                        decision_list["first_diag"] = True
                    break

        #Логика простреливания второй диагонали
        elif not decision_list["second_diag"]:
            for i in range(0,10):
                if player_map[9 - i][i] != " 8 " and player_map[9 - i][i] != " X ":
                    shot_pos = (9 - i,i)
                    if shot_pos[1] == 9:
                        decision_list["second_diag"] = True
                    break
        
        #Логика прямого поочередного простреливания всего поля
        else:
            placed_shot = False
            for i in range(0,10):
                for j in range(0,10):
                    if player_map[i][j] == " O " or player_map[i][j] == "   ":
                        shot_pos = (i,j)
                        placed_shot = True
                        break
                if placed_shot: break
        
        print("Мой выстрел - ", end = "")
        print(str(shot_pos[0]) + str(horisontal_placement[shot_pos[1]]))

        if player_map[shot_pos[0]][shot_pos[1]] == " O ":
            print("Попал!")
            player_map[shot_pos[0]][shot_pos[1]] = " 8 "
            player_turn = False
        elif player_map[shot_pos[0]][shot_pos[1]] == "   ":
            print("Мимо!")
            player_map[shot_pos[0]][shot_pos[1]] = " X "
        print_field(shot_map, player_map)
        
        if check_defeat(player_map):
            comp_win = True
            break
    
    turns_counter += 1

if comp_win: print("Я победил тебя, кожанный мешок с костями!!!")
if player_win: print("Поздравляю тебя с победой, адмирал " + player_name + "!!!")
