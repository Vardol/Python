# 3.12 Вводим с клаиватуры строку. Необходимо развернуть подстроку между первой и последней буквой "о".
# Если она только одна или её нет - то сообщить, что буква "о" -одна или не встречается



def revert_string(input_string: str, start_pos = 0, end_pos = -101):
    if end_pos == -101: end_pos = len(input_string) - 1
    #если не введена крайняя позиция диапазона - устанавливаем ее на последний элемент строки

    if start_pos < 0 or end_pos < 0 or start_pos >= len(input_string) or end_pos >= len(input_string):
        return "некорректный ввод диапазона"

    if end_pos < start_pos:
        swap_value = start_pos
        start_pos = end_pos
        end_pos = swap_value
    # если конечная точка стоит раньше начальной, то меняем их местами для простоты обработки

    reverted_part = input_string[start_pos:end_pos+1]
    reverted_part = reverted_part[::-1]

    return input_string[:start_pos]+reverted_part+input_string[end_pos+1:]




def find_range_between_letters(input_string: str, input_char: str):
    
    input_char = input_char[0] # если введено несколько символов - то ищем только по первому

    first_char_index = -1
    for i in range(0,len(input_string)):
        if input_string[i] == input_char[0]:
            first_char_index = i
            break
    if first_char_index == len(input_string) - 1 or first_char_index < 0: return (-1, -1)
    # если искомый символ не нашелся и first_char_index все еще равен "-1" или он нашелся на последней позиции (т.е. нет второго),
    # то возвращаем кортеж с "-1", в качестве сигнала об ошибке

    last_char_index = -1
    for i in range(0, len(input_string) - first_char_index - 1,):
        if input_string[len(input_string) - 1 - i] == input_char[0]:
            last_char_index = len(input_string) - 1 - i
            break
    if last_char_index < 0: return (-1, -1)
    # если искомый символ не нашелся в оставшей непроверенной на предыдущем этапе части строки и last_char_index все еще равен "-1",
    # то возвращаем кортеж с "-1", в качестве сигнала об ошибке

    return (first_char_index, last_char_index)



input_string = input("Введите строку - ")
o_range = find_range_between_letters(input_string, "o")
if o_range[0] < 0: print("В диапазоне менее 2 букв о - нечего разворачивать!")
else: print(revert_string(input_string, o_range[0], o_range[1]))