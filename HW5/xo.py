#создает 2-д список списков заполняя все значения образцом
def create_2d_array_by_sample(xsize, ysize, sample):
    result = [0] * xsize
    for i in range(0, xsize):
        result[i] = [sample] * ysize
    return result

# просто пара методов для красивого вывода
def print_field(input_array: list):
    print("  ", end = "")
    print("   A      B      C")
    for i in range(0,len(input_array)):
        print(str(i) + " ", end="")
        print((input_array[i]))

#проверяет соответствие переданной строки шаблону координат: 2 знака, из которых 1 - цифра, другой - англ буква от A до J
def check_coordinates_validity(coordinates_str: str, letters_vocabulary = "ABCabc"):
    digits = "012"
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
    horisontal_placement = "ABC"
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


#проверяем все вводы строк на выражение волеизъявления пользователя прекратить игру
def check_quit(input_str: str):
    if input_str.find("quit") != -1 or input_str.find("exit") != -1: exit()
    else: return input_str

def comp_moves(field: list):
    comp_placement = (-1, -1)
    for i in range(0,len(field)):
        for j in range(0,len(field)):
            if field[i][j] == " X ":
                

#проверяет наличие в ряд 3 знаков
def check_win(map: list):
    #TODO
    return "O X D U"

def player_moves(field: list):
    player_placement = read_coordinates("Твой ход (введи координаты из двух знаков A-C, 0-2) - ")
    while field[player_placement[0]][player_placement[1]] != "   ":
        print("Тут уже занято!")
        player_placement = read_coordinates("Твой ход (введи координаты из двух знаков A-C, 0-2) - ")
    field[player_placement[0]][player_placement[1]] = " X "
    return field
    


#!!!собственно тело программы начинается здесь!!!

#делаем 3 поля: 1 - компа (сразу его наполяем стандартными кораблями), 1 - игрока, 1 - отмечать выстрелы игрока
field = create_2d_array_by_sample(3,3, "   ")

print("\nКрестики, нолики v1.0. Для выхода введите exit или quit.\n\n")
print("Привет! Как тебя зовут?")
player_name = check_quit(input())
print(player_name + ", сыграем в Крестики нолики? Y/N ")
if (input().upper()) not in ["ДА", "YES", "Y", "ДАВАЙ"]:
    print("Ну тогда до скорого, трусишка " + player_name + "!")
    exit()
print("Так и быть уступаю тебе право первого хода. Ты ходишь крестиками")
horisontal_placement = "ABC"

#флаги для контроля и завершения игры
comp_win = False
player_win = False
draw = False

#Логика первого хода - стараемся поставить в центр, но если он уже занят - ставим в верхний левый угол
field = player_moves(field)
if field[1][1] == "   ":
    field[1][1] = " O "
    print("Мой ход - B1")
else:
    field[0][0] = " O "
    print("Мой ход - A0")


while comp_win == False and player_win == False and draw == False:
    field = player_moves(field)
    field = comp_moves(field)
    
    result = check_win(field)
    if result == "X": player_win = True
    elif result == "O": comp_win = True
    elif result == "D": draw = True

    print_field(shot_map, player_map)
    while player_turn:
        player_turn = False

        #считываем с игрока координаты выстрела, отмечаем его на двух картах (компа и выстрелов)
        shot_pos  = read_coordinates("Твой выстрел - ")
        if comp_map[shot_pos[0]][shot_pos[1]] == " O ":
            comp_map[shot_pos[0]][shot_pos[1]] = " 8 "
            shot_map[shot_pos[0]][shot_pos[1]] = " 8 "
            player_turn = True # если попал - снова стреляешь
            if check_ship_sunk(comp_map,find_ship_check_zone(shot_pos,comp_map)):
                shot_map = mark_sunk_ship_zone(shot_map, find_ship_check_zone(shot_pos,comp_map))
                comp_map = mark_sunk_ship_zone(comp_map, find_ship_check_zone(shot_pos,comp_map))
                print_field(shot_map, player_map)
                print("Ты потопил мой корабль!")
            else:
                print_field(shot_map, player_map)
                print("Ты ранил мой корабль!")
        elif comp_map[shot_pos[0]][shot_pos[1]] == "   ":
            comp_map[shot_pos[0]][shot_pos[1]] = " X "
            shot_map[shot_pos[0]][shot_pos[1]] = " X "
            print_field(shot_map, player_map)
            print("Ты промахнулся!")
        else:
            print_field(shot_map, player_map)
            print("Мимо!")

        #проверяем, на случай, если этим залпом был подбит последний корабль компа
        if check_win(field):
            player_win = True
            break

    while not player_turn:
        player_turn = True
        #Перебираем доступные нам логики в заданном порядке

        #Логика добивания ранненого корабля
        if decision_list["finishing meal"][0] != -1:
            print("добиваем" + str(decision_list["finishing meal"]))
            placed_shot = False
            
            #проверяем на трехпалубник сверху (т.е. ситуация в которой были два соседних попадания, а корабль не убит)
            if (
                decision_list["finishing meal"][0] > 0 
                and player_map[decision_list["finishing meal"][0] - 1][decision_list["finishing meal"][1]] == " 8 "
                and not placed_shot
                ):
                    if (
                        decision_list["finishing meal"][0] - 1 > 0
                        and player_map[decision_list["finishing meal"][0] - 2][decision_list["finishing meal"][1]] in ["   ", " O "]
                        ):
                        shot_pos = (decision_list["finishing meal"][0] - 2, decision_list["finishing meal"][1])
                        placed_shot = True
                    elif (
                        decision_list["finishing meal"][0] < len(player_map) - 1
                        and player_map[decision_list["finishing meal"][0] + 1][decision_list["finishing meal"][1]] in ["   ", " O "]
                        ):
                        shot_pos = (decision_list["finishing meal"][0] + 1, decision_list["finishing meal"][1])
                        placed_shot = True

            # проверяем трехпалубник снизу
            if (
                decision_list["finishing meal"][0] < len(player_map) - 1 
                and player_map[decision_list["finishing meal"][0] + 1][decision_list["finishing meal"][1]] == " 8 "
                and not placed_shot
                ):
                    if (
                        decision_list["finishing meal"][0] > 0
                        and player_map[decision_list["finishing meal"][0] - 1][decision_list["finishing meal"][1]] in ["   ", " O "]
                        ):
                        shot_pos = (decision_list["finishing meal"][0] - 1, decision_list["finishing meal"][1])
                        placed_shot = True
                    elif (
                        decision_list["finishing meal"][0] < len(player_map) - 2
                        and player_map[decision_list["finishing meal"][0] + 2][decision_list["finishing meal"][1]] in ["   ", " O "]
                        ):
                        shot_pos = (decision_list["finishing meal"][0] + 2, decision_list["finishing meal"][1])
                        placed_shot = True

            # проверяем трехпалубник слева
            if (
                decision_list["finishing meal"][1] > 0 
                and player_map[decision_list["finishing meal"][0]][decision_list["finishing meal"][1] - 1] == " 8 "
                and not placed_shot
                ):
                    if (
                        decision_list["finishing meal"][0] - 1 > 0
                        and player_map[decision_list["finishing meal"][0]][decision_list["finishing meal"][1] - 2] in ["   ", " O "]
                        ):
                        shot_pos = (decision_list["finishing meal"][0], decision_list["finishing meal"][1] - 2)
                        placed_shot = True
                    elif (
                        decision_list["finishing meal"][1] < len(player_map) - 1
                        and player_map[decision_list["finishing meal"][0]][decision_list["finishing meal"][1] + 1] in ["   ", " O "]
                        ):
                        shot_pos = (decision_list["finishing meal"][0], decision_list["finishing meal"][1] + 1)
                        placed_shot = True

            # проверяем трехпалубник справа
            if (
                decision_list["finishing meal"][1] < len(player_map) - 1 
                and player_map[decision_list["finishing meal"][0]][decision_list["finishing meal"][1] + 1] == " 8 "
                and not placed_shot
                ):
                    if (
                        decision_list["finishing meal"][1] > 0
                        and player_map[decision_list["finishing meal"][0]][decision_list["finishing meal"][1] - 1] in ["   ", " O "]
                        ):
                        shot_pos = (decision_list["finishing meal"][0], decision_list["finishing meal"][1] - 1)
                        placed_shot = True
                    elif (
                        decision_list["finishing meal"][1] < len(player_map) - 2
                        and player_map[decision_list["finishing meal"][0]][decision_list["finishing meal"][1] + 2] in ["   ", " O "]
                        ):
                        shot_pos = (decision_list["finishing meal"][0], decision_list["finishing meal"][1] + 2)
                        placed_shot = True


            #пробуем вверх от ранения
            if decision_list["finishing meal"][0] > 0 and not placed_shot:
                print("ищем вверх")
                if player_map[decision_list["finishing meal"][0] - 1][decision_list["finishing meal"][1]] in ["   ", " O "]:
                    shot_pos = (decision_list["finishing meal"][0] - 1,decision_list["finishing meal"][1])
                    placed_shot = True
                elif (
                    decision_list["finishing meal"][0] - 2 >= 0
                    and player_map[decision_list["finishing meal"][0] - 1][decision_list["finishing meal"][1]] == " 8 " 
                    and player_map[decision_list["finishing meal"][0] - 2][decision_list["finishing meal"][1]] in ["   ", " O "] 
                    ):
                        shot_pos = (decision_list["finishing meal"][0] - 2,decision_list["finishing meal"][1])
                        placed_shot = True

            #пробуем вниз от ранения
            if decision_list["finishing meal"][0] < len(player_map) - 1 and not placed_shot:
                print("ищем вниз")
                if player_map[decision_list["finishing meal"][0] + 1][decision_list["finishing meal"][1]] in ["   ", " O "]:
                    shot_pos = (decision_list["finishing meal"][0] + 1,decision_list["finishing meal"][1])
                    placed_shot = True
                elif (
                    decision_list["finishing meal"][0] + 2 <= len(player_map) - 1
                    and player_map[decision_list["finishing meal"][0] + 1][decision_list["finishing meal"][1]] == " 8 "
                    and player_map[decision_list["finishing meal"][0] + 2][decision_list["finishing meal"][1]] in ["   ", " O "] 
                    ):
                        shot_pos = (decision_list["finishing meal"][0] + 2,decision_list["finishing meal"][1])
                        placed_shot = True

            #пробуем влево от ранения
            if decision_list["finishing meal"][1] > 0 and not placed_shot:
                print("ищем влево")
                if player_map[decision_list["finishing meal"][0]][decision_list["finishing meal"][1] - 1] in ["   ", " O "]:
                    shot_pos = (decision_list["finishing meal"][0],decision_list["finishing meal"][1] - 1)
                    placed_shot = True
                elif (
                    decision_list["finishing meal"][1] - 2 >= 0
                    and player_map[decision_list["finishing meal"][0]][decision_list["finishing meal"][1] - 1] == " 8 " 
                    and player_map[decision_list["finishing meal"][0]][decision_list["finishing meal"][1] - 2] in ["   ", " O "]
                    ):
                    shot_pos = (decision_list["finishing meal"][0],decision_list["finishing meal"][1] - 2)
                    placed_shot = True

            #пробуем вправо от ранения
            if decision_list["finishing meal"][1] < len(player_map) - 1 and not placed_shot:
                print("ищем вправо")
                if player_map[decision_list["finishing meal"][0]][decision_list["finishing meal"][1] + 1] in ["   ", " O "]:
                    shot_pos = (decision_list["finishing meal"][0],decision_list["finishing meal"][1] + 1)
                    placed_shot = True
                elif (
                    decision_list["finishing meal"][1] + 2 <= len(player_map) - 1
                    and player_map[decision_list["finishing meal"][0]][decision_list["finishing meal"][1] + 1] == " 8 " 
                    and player_map[decision_list["finishing meal"][0]][decision_list["finishing meal"][1] + 2] in ["   ", " O "]
                    ):
                        shot_pos = (decision_list["finishing meal"][0],decision_list["finishing meal"][1] + 2)
                        placed_shot = True

            if not placed_shot:
                print("не разместили выстрел")
                decision_list["finishing meal"] = (-1,-1)
                


        #Логика простреливания первой диагонали
        elif not decision_list["first_diag"]:
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
        
        #Логика прострела в "шахматном" порядке
        elif not decision_list["chess_order"]:
            placed_shot = False
            for i in range(0,10):
                for j in range(0,10):
                    if player_map[i][j] in [" O ", "   "]:
                        unshot_surrounding_tiles_current = 0
                        if i > 0 and player_map[i-1][j] in [" O ", "   "]: unshot_surrounding_tiles_current += 1
                        if j > 0 and player_map[i][j-1] in [" O ", "   "]: unshot_surrounding_tiles_current += 1
                        if i < len(player_map) - 1 and player_map[i+1][j] in [" O ", "   "]: unshot_surrounding_tiles_current += 1
                        if j < len(player_map) - 1 and player_map[i][j+1] in [" O ", "   "]: unshot_surrounding_tiles_current += 1
                        
                        
                        if j < len(player_map) - 1 and player_map[i][j+1] in [" O ", "   "]:
                            next = j+1
                            unshot_surrounding_tiles_next = 0
                            if i > 0 and player_map[i-1][next] in [" O ", "   "]: unshot_surrounding_tiles_next += 1
                            if next > 0 and player_map[i][next-1] in [" O ", "   "]: unshot_surrounding_tiles_next += 1
                            if i < len(player_map) - 1 and player_map[i+1][next] in [" O ", "   "]: unshot_surrounding_tiles_next += 1
                            if next < len(player_map) - 1 and player_map[i][next+1] in [" O ", "   "]: unshot_surrounding_tiles_next += 1
                            if unshot_surrounding_tiles_next >= unshot_surrounding_tiles_current:
                                j = next
                                unshot_surrounding_tiles_current = unshot_surrounding_tiles_next

                        if unshot_surrounding_tiles_current >= 2:
                            shot_pos = (i,j)
                            placed_shot = True
                            break
                if placed_shot: break
            if not placed_shot: decision_list["chess_order"] = True

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
            player_map[shot_pos[0]][shot_pos[1]] = " 8 "
            player_turn = False
            if check_ship_sunk(player_map,find_ship_check_zone(shot_pos,player_map)):
                player_map = mark_sunk_ship_zone(player_map, find_ship_check_zone(shot_pos,player_map))
                decision_list["finishing meal"] = (-1,-1)
                print_field(shot_map, player_map)
                print("Я потопил твой корабль!")
            else:
                print_field(shot_map, player_map)
                print("Я ранил твой корабль!")
                decision_list["finishing meal"] = (shot_pos[0], shot_pos[1])
        elif player_map[shot_pos[0]][shot_pos[1]] == "   ":
            print_field(shot_map, player_map)
            print("Я промахнулся!")
            player_map[shot_pos[0]][shot_pos[1]] = " X "
        else:
            print_field(shot_map, player_map)
            print("Мимо")
        
        if check_defeat(player_map):
            comp_win = True
            break
    
    turns_counter += 1

if comp_win: print("Я победил тебя, кожанный мешок с костями!!!")
if player_win: print("Поздравляю тебя с победой, адмирал " + player_name + "!!!")
