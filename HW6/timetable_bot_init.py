import core
import ui
import dbi

def set_username(name = "schedule"):
    with open("current_username.txt","w",encoding="utf-8") as current_username:
        current_username.write(name)

def greetings():
    print("\n Weekly schedule console bot v 1.0 \n")
    print("print 'quit' or 'exit' or 'выход' to close program\n")

def initialize():
    username = input("Введите имя пользователя (без пробелов и служебных символов): ")
    if username.find(" ") != -1: username = username[:(username.find(" "))]
    set_username(username.lower())
    if not dbi.check_schedule_exists():
        print("Вы еще не заводили свое недельное расписания, " + username + ". Либо уже удалили его.")
        dbi.clear_schedule()
    else: print("С возвращением, " + username)
    ui.print_data("Введите команду ? для получения инструкций.")
    core.schedulebot(username)


greetings()
initialize()