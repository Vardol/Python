import dbi
import ui
import utils


def activity_isempty(activity: dict):
    if activity["day"] == "EMPTY" and activity["time"] == -1 and activity["name"] == "EMPTY": return True
    else: return False

def instructions():
    instructions = ""
    instructions += "Консольный бот позволяет создавать еженедельное расписание текстовыми командами.\n"
    instructions += "Бот хранит отдельные расписания для каждого пользователя.\n"
    instructions += "Формат ввода: '<КОМАНДА> <параметры записи>'\n"
    instructions += "<параметры записи> могут включать день недели (на рус или англ полностью или сокращено), время (двузначное число) и описание (текст)\n"
    instructions += "<команда> может вводится большими или маленькими буквами. Список доступных команд:'\n"
    instructions += "__________________________________________________________________________________________\n"
    instructions += "ADD (ДОБАВИТЬ, ДОБАВЬ) - добавляет запись в расписание.\n"
    instructions += "PRINT (TIMETABLE, SCHEDULE, РАСПИСАНИЕ, ПЕЧАТЬ) - выводит расписание полностью.\n"
    instructions += "FIND (НАЙТИ, НАЙДИ) - выводит записи в расписании, соответствующие запросу.\n"
    instructions += "PRINT (TIMETABLE, SCHEDULE, РАСПИСАНИЕ, ПЕЧАТЬ) - выводит расписание полностью.\n"
    instructions += "DEL (DELETE, УДАЛИТЬ, УДАЛИ) - добавляет запись в расписание.\n"
    instructions += "CLEAR (CLR, ОЧИСТИТЬ) - полностью очищает расписание.\n"
    instructions += "HELP (?, ПОМОЩЬ, СОС, SOS) - выводит инструкцию по работе.\n"
    instructions += "QUIT (EXIT, ВЫХОД) - закрыть программу.\n"
    return instructions

def confirm(input_str = ""):
    answer = utils.check_quit(input(input_str + "Вы уверены? Y/N (Д/Н) - ").upper())
    if answer == "Y" or answer == "Д": return True
    else: return False

def schedulebot(username: str):
    while True:
        request = ui.read_request()
        if request[0] == "ADD" or request[0] == "ДОБАВИТЬ" or request[0] == "ДОБАВЬ":
            if activity_isempty(request[1]): ui.print_data("Пустая запись.")
            else:
                if dbi.store_activity(request[1]): ui.print_data("Успешно.")

        elif request[0] == "PRINT" or request[0] == "TIMETABLE" or request[0] == "SCHEDULE" or request[0] == "РАСПИСАНИЕ" or request[0] == "ПЕЧАТЬ":
            ui.print_data(dbi.fetch_activity(request[1]))

        #TODO
        elif request[0] == "FIND" or request[0] == "НАЙТИ" or request[0] == "НАЙДИ":
            if activity_isempty(request[1]): ui.print_data("Пустая запись.")
            else:
                ui.print_data(dbi.fetch_activity(request[1]))

        elif request[0] == "DEL" or request[0] == "DELETE" or request[0] == "УДАЛИТЬ" or request[0] == "УДАЛИ":
            if activity_isempty(request[1]): ui.print_data("Пустая запись.")
            else:
                if dbi.delete_activity(dbi.fetch_activity(request[1])):
                    ui.print_data("Успешно.")

        elif request[0] == "CLEAR" or request[0] == "CLR" or request[0] == "ОЧИСТИТЬ":
            if confirm("Очистить все расписание. "):
                if dbi.clear_schedule(): ui.print_data("Успешно.")

        elif request[0] == "HELP" or request[0] == "?" or request[0] == "ПОМОЩЬ" or request[0] == "СОС" or request[0] == "SOS" or request[0] == "COC":
            ui.print_data(instructions())

        else: print("Нераспознанная команда.\n")