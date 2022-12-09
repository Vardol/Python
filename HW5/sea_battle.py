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
    print("\n ----------------------------------------------------------------------- \n")
    print_map(player_map)

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

def read_coordinates(prompting_msg = "Введи координаты - ", err_msg = "некорректные координаты"):
    horisontal_placement = "ABCDEFGHIJ"
    coordinates_str = str(input(prompting_msg))
    while not check_coordinates_validity(coordinates_str):
        print(err_msg)
        coordinates_str = str(input(prompting_msg))
    coordinates_str = coordinates_str.upper()
    if coordinates_str[0].isdigit():
        position = (int(coordinates_str[0]),horisontal_placement.find(coordinates_str[1]))
    else:
        position = (int(coordinates_str[1]),horisontal_placement.find(coordinates_str[0]))
    return position

def read_direction(prompting_msg = "Введи направление корабля - ", err_msg = "некорректное направление (up/down/left/right)", directions_vocabulary = "updownleftrightUPDOWNLEFTRIGHT"):
    direction = input(prompting_msg)
    while directions_vocabulary.find(direction) == -1:
        print(err_msg)
        direction = input(prompting_msg)
    return direction.lower()

#проверка допустимости расположения корабля. TODO: добавить проверку на соседние корабли
def check_placement(start_pos: tuple, size: int, direction: str, map: list):
    if direction == "up":
        if start_pos[0]+1 < size:
            return False
        else:
            for i in range(0, size):
                if map[start_pos[0]-i][start_pos[1]] != "   ": return False
        #check_zone = [(max(0,start_pos[0] - size),max(0,start_pos[1] - 1)),(min(len(map),start_pos[0] + 1),min(len(map),start_pos[1] + 1))]
        return True
    elif direction == "down":
        if len(map)-start_pos[0] < size: return False
        else:
            for i in range(0, size):
                if map[start_pos[0]+i][start_pos[1]] != "   ": return False
        return True
    elif direction == "right":
        if len(map[start_pos[0]])-start_pos[1] < size: return False
        else:
            for i in range(0, size):
                if map[start_pos[0]][start_pos[1]+i] != "   ": return False
        return True
    elif direction == "left":
        if start_pos[1] + 1 < size: return False
        else:
            for i in range(0, size):
                if map[start_pos[0]][start_pos[1]-i] != "   ": return False
        return True
    else: return False


#просто ставит корабль с заданными параметрами, по заданным координатам
def place_ship(start_pos: tuple, size: int, direction: str, map: list):
    if not check_placement(start_pos, size, direction, map): return map
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


#ставит корабль заданного размера в случайной позиции
def place_random_ship_Xtimes(size: int, number_of_ships: int, map: list):
    import random
    directions = ["up", "down", "left", "right"]
    for i in range(0, number_of_ships):
        start_pos = (random.randint(0,9),random.randint(0,9))
        direction = directions[random.randint(0,3)]
        while not check_placement(start_pos, size, direction, map):
            start_pos = (random.randint(0,9),random.randint(0,9))
            direction = directions[random.randint(0,3)]
        map = place_ship(start_pos, size, direction, map)
    return map

#выставляет стандартный набор кораблей в случайных местах
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





player_map = create_2d_array_by_sample(10,10, "   ")
comp_map = create_2d_array_by_sample(10,10, "   ")
shot_map = create_2d_array_by_sample(10,10, "   ")
comp_map = place_standart_ships(comp_map)


print("Привет! Как тебя зовут?")
player_name = input()
print(player_name + ", сыграем в морской бой? Y/N ")
if (input()) not in ["Да", "да", "ДА", "дА", "yes", "Yes", "YES", "YEs", "YeS", "yeS", "yES", "Y", "y", "давай", "Давай"]:
    print("Ну тогда до скорого, " + player_name + "!")
    exit
print("Вот твое поле, " + player_name + ". Расставляй корабли (я не буду подсматривать, честно!)")
print_map(player_map)
print("Вводи два знака: букву (A - J) и цифру (0 - 9)")
horisontal_placement = "ABCDEFGHIJ"

#расставляем однопалубники
for i in range(0,3):
    start_pos = read_coordinates("Вводи координаты однопалубника - ")
    while not check_placement(start_pos, 1, "up", player_map):
        print("некорректное расположение корабля")
        start_pos = read_coordinates("Вводи координаты трехпалубника - ")
    player_map = place_ship(start_pos, 1, "up", player_map)
    print_map(player_map)
    
#расставляем двухпалубники
for i in range(0,2):
    start_pos = read_coordinates("Вводи координаты двухпалубника - ")
    direction = read_direction()
    while not check_placement(start_pos, 2, direction, player_map):
        print("некорректное расположение корабля")
        start_pos = read_coordinates("Вводи координаты трехпалубника - ")
        direction = read_direction()
    player_map = place_ship(start_pos, 2, direction, player_map)
    print_map(player_map)

#ставим 1 трехпалубник
start_pos = read_coordinates("Вводи координаты трехпалубника - ")
direction = read_direction()
while not check_placement(start_pos, 3, direction, player_map):
    print("некорректное расположение корабля")
    start_pos = read_coordinates("Вводи координаты трехпалубника - ")
    direction = read_direction()

player_map = place_ship(start_pos, 3, direction, player_map)
print_map(player_map)


print("Корабли расставлены. К Бою!")
comp_win = False
player_win = False
player_turn = True                                                 #TODO: comp logic to finish off previously hit ships
decision_list = {"first_diag": False, "second_diag": False, "finishing meal": (-1,-1), "cheating bastard": False}
                                                                #TODO: cheating comp logic, where comp finds player's ships
turns_counter = 1
while comp_win == False and player_win == False:
    print("Ход №" + str(turns_counter))
    print_field(shot_map, player_map)
    while player_turn:
        player_turn = False
        shot_pos  = read_coordinates("Твой выстрел - ")
        if comp_map[shot_pos[0]][shot_pos[1]] == " O ":
            print("Попал!")
            comp_map[shot_pos[0]][shot_pos[1]] = " 8 "
            shot_map[shot_pos[0]][shot_pos[1]] = " 8 "
            player_turn = True
        elif comp_map[shot_pos[0]][shot_pos[1]] == "   ":
            print("Мимо!")
            comp_map[shot_pos[0]][shot_pos[1]] = " X "
            shot_map[shot_pos[0]][shot_pos[1]] = " X "
        print_field(shot_map, player_map)

        if check_defeat(comp_map):
            player_win = True
            break

    while not player_turn:
        player_turn = True

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
