#Database interface
import os

#TODO: different file for different users
def find_schedule():
    with open("current_username.txt","r", encoding="utf-8") as current_username:
        filename = current_username.read() + ".txt"
    return filename

def check_schedule_exists():
    filename = find_schedule()
    if filename in (os.listdir()): return True
    else: return False

def strlist_toactivity(strlist: list):
    activity = {"day": strlist[0], "time": int(strlist[1]), "name": ""}
    if len(strlist) > 2:
        for i in  range(2, len(strlist)):
            activity["name"] += strlist[i]
            if i != len(strlist) - 1: activity["name"] += " "
    if activity["name"].find("\n") != -1: activity["name"] = activity["name"][:(len(activity["name"]) - 3)]
    return activity

def fetch_activity(activity = {"day": "EMPTY", "time": -1, "name": "EMPTY"}):
    activity_list = []
    with open(find_schedule(), "r", encoding = "utf-8") as schedule:
        for activity_str in schedule:
            activity_list.append(strlist_toactivity(activity_str.split()))
    requested_day = ""
    requested_time = -1
    requested_name = ""
    if activity["day"] != "EMPTY": requested_day = activity["day"]
    if activity["time"] != -1: requested_time = activity["time"]
    if activity["name"] != "EMPTY": requested_name = activity["name"]
    if requested_day != "":
        i = 0
        while i in range(0, len(activity_list)):
            if i not in range (0, len(activity_list)):
                break
            if activity_list[i]["day"] != requested_day and activity_list[i]["day"] != "EMPTY":
                activity_list.pop(i)
                i -=1
            i += 1
    if requested_time != -1:
        i = 0
        while i in range(0,len(activity_list)):
            if i not in range (0, len(activity_list)): break
            if activity_list[i]["time"] != requested_time and activity_list[i]["time"] != -1:
                activity_list.pop(i)    
                i -= 1
            i += 1
    if requested_name != "":
        i = 0
        while i in range(0,len(activity_list)):
            if i not in range (0, len(activity_list)): break
            if activity_list[i]["name"].find(requested_name) == -1:
                activity_list.pop(i)
                i -= 1
            i += 1
    return activity_list

def store_activity(activity: dict):
    with open(find_schedule(), "a", encoding = "utf-8") as schedule:
        schedule.write(activity["day"] + " " + str(activity["time"]) + " " + activity["name"] + "\n")
    return True

#TODO: sort schedule by date and time
def sort_activities():
    return True

def delete_activity(activity_list_input: list):
    full_schedule = fetch_activity()
    i = 0
    while i < len(full_schedule):
        if i >= len(full_schedule): break
        for activity in activity_list_input:
            if full_schedule[i] == activity:
                full_schedule.pop(i)
                i -= 1
                break
        i += 1
    with open(find_schedule(), "w", encoding = "utf-8") as schedule:
        for activity in full_schedule:
            schedule.write(activity["day"] + " " + str(activity["time"]) + " " + activity["name"] + "\n")
    return True

def clear_schedule():
    with open(find_schedule(), "w", encoding = "utf-8") as schedule:
        schedule.write("")
    return True

# store_activity({"day": "ВТОРНИК", "time": 13, "name": "TRAIN MORE"})
# store_activity({"day": "ВТОРНИК", "time": 12, "name": "LEARN"})
# store_activity({"day": "ВОСКРЕСЕНЬЕ", "time": 10, "name": "SNOWBOARD"})
# store_activity({"day": "ПЯТНИЦА", "time": 19, "name": "PARTY!!!"})


#delete_activity(fetch_activity(requested_day="ПЯТНИЦА"))

#print(strlist_toactivity(["ПОНЕДЕЛЬНИК", "12", "TRAIN", "WELL"]))
