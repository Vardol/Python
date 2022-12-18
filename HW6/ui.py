import utils

day_list_eng_full = ("MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY")
day_list_eng_short = ("MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN")
day_list_rus_full = ("ПОНЕДЕЛЬНИК", "ВТОРНИК", "СРЕДА", "ЧЕТВЕРГ", "ПЯТНИЦА", "СУББОТА", "ВОСКРЕСЕНЬЕ")
day_list_rus_short = ("ПН", "ВТ", "СР", "ЧТ", "ПТ", "СБ", "ВС")
day_list_full_collection = [day_list_eng_full, day_list_eng_short, day_list_rus_full, day_list_rus_short]
day_column_width = 15
time_column_width = 10

def find_day(input_str: str, day_list_collection = day_list_full_collection, additional_daylist = ["","","","","","",""]):
    if additional_daylist[0] != "":
        for i in range(0,len(additional_daylist)):
            additional_daylist[i] = additional_daylist[i].upper()
        day_list_collection.append(additional_daylist)
    result = -1
    for i in range(0, len(day_list_collection)):
        for j in range (0, 7):
            if input_str == day_list_collection[i][j]:
                if result == -1: result = j
                else: result = -2
    if result in range (0, 7): return result
    else: return -1


def read_request(prompting_msg = "Введите запрос:\n"):
    request_str_list = utils.check_quit(input(prompting_msg)).upper().split()
    command = request_str_list.pop(0)
    command = command.upper()
    return (command, form_activity(request_str_list))


# def read_activity(prompting_msg = "Введите событие (день, время, название):\n"):
#     return form_activity(utils.check_quit(input(prompting_msg)).upper().split())

#TODO: длительность, описание
def form_activity(input_str_list: list, day_list_format = day_list_rus_full):
    activity = {"day": "EMPTY", "time": -1, "name": ""}
    for text in input_str_list:
        if not isinstance(text,str):
            activity["name"] = "EMPTY"
            return activity
        day_index = find_day(text.upper())
        if day_index != -1: activity["day"] = day_list_format[day_index]
        elif text.isdigit(): activity["time"] = int(text)
        else: activity["name"] += text + " "

    empty_name = True
    if activity["name"] != "":
        for char in activity["name"]:
            if char != " ":
                empty_name = False
                break

    if empty_name:
        activity["name"] = "EMPTY"
        return activity

    if activity["name"][len(activity["name"]) - 1] == " ":
        activity["name"] = utils.str_replace_char_byindex(activity["name"], len(activity["name"]) - 1,".")
    elif activity["name"][len(activity["name"]) - 1] != ".": activity["name"] += "."
    if activity["time"] not in range(0,24): activity["time"] = -1
    return activity

def convert_activity_tostr(activity: dict):
    output_str = activity["day"]
    if activity["day"] == "EMPTY": output_str = "ежедневно"
    output_str += " " * max(0,(day_column_width - len(output_str)))
    if activity["time"] == -1: output_str += "весь день" + " " * max(0,(time_column_width - len("весь день")))
    else:
        if activity["time"] < 10: output_str += "0"
        output_str += str(activity["time"]) + " " * max(0,(time_column_width - 2))
    if activity["name"] == "EMPTY": output_str += "н/д"
    else: output_str += activity["name"]
    return output_str

def activity_header():
    output_str = "\n"
    output_str += "ДЕНЬ"
    output_str += " " * max(0,(day_column_width - len("ДЕНЬ")))
    output_str += "ВРЕМЯ" + " " * max(0,(time_column_width - len("ВРЕМЯ")))
    output_str += "АКТИВНОСТЬ"
    output_str += "\n___________________________________________________________________________________"
    return output_str

def print_data(data):
    if isinstance(data,list) and len(data)>0 and isinstance(data[0], dict):
        print(activity_header())
        for activity in data:
            print(convert_activity_tostr(activity))
        print("___________________________________________________________________________________\n")
    elif isinstance(data, dict):
        print(activity_header())
        print(convert_activity_tostr(data))
        print("___________________________________________________________________________________\n")
    else: print(data)

