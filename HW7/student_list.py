# 2)Нужно напистаь программу
# В ней используем классы - имя студента name, номер группы group и список полученных оценок progress.
# В самой программе вводим список всех студентов.
# В программе нужно вывести список студентов, отсортированный по имени, А так же студентов, у которых низкие оценки

class Student:
    def __init__(self, name: str, group_id: int, progress = []):
        self.name = name
        self.group_id = group_id
        self.progress = []
        self.avg_score = 0
        if len(progress) > 0:
            for score in progress:
                if isinstance(score, int):
                    self.avg_score += score
                    self.progress.append(score)
            self.avg_score /= len(self.progress)
        else: self.avg_score = None

    def refresh_avg_score(self):
        if len(self.progress) > 0:
            self.avg_score = 0
            for score in self.progress:
                self.avg_score += score
            self.avg_score /= len(self.progress)

    def add_score(self, score: int):
        self.progress.append(score)
        self.refresh_avg_score()

    def __str__(self):
        return f"Имя - {self.name}, Группа - {self.group_id}, средний балл - {self.avg_score}, оценки:{str(self.progress)}"

    def __len__(self):
        return 1

def generate_random_student(name = "", group_id = 0, progress = [], number_of_scores = 0, additional_name_list = (), additional_surname_list = ()):
    import random
    r = random
    name_list = ("Василий", "Петр", "Дмитрий", "Марат", "Мухтар", "Иван", "Евгений", "Казбек", "Ибрагим", "Джон", *additional_name_list)
    surname_list = ("Михайлов", "Васечкин", "Иванов", "Сванидзе", "Меладзе", "Шагиахметов", "Сулейманов", "Петров", "Григорян", "Леннон", *additional_surname_list)
    group_list = [101,102,103,201,202,203,301,302,303,401,402,403,501,502,503]
    score_list = [2,3,4,5,5,4,5,4,5,4,3,2,2,3,5,4,5,3,2,4,5,4,3,3,5,4,5,5,3,4,5,4,3,2,4,5,2,3,4]
    if name == "": name = str(name_list[r.randint(0, len(name_list)-1)] + " " + surname_list[r.randint(0, len(surname_list)-1)])
    if group_id == 0: group_id = group_list[r.randint(0,len(group_list)-1)]
    if len(progress) == 0:
        import time
        if number_of_scores == 0: number_of_scores = r.randint(5,10)
        while number_of_scores > 0:
            randm_score = score_list[random.randint(0,len(score_list) - 1)]
            #Как ни бился, для каждого студента генерится почему-то та же последовательность оценок
            #я и напрямую генерил int в диапазона 2 - 5, и потом список составил из которого отбирал по случайному индексу значения
            #и таймер ожидания добавлял, на случай, если от времени функция работает.
            #но все равно оценки одинаковые у всех генерятся...

            progress.append(randm_score)
            time.sleep(0.5)
            number_of_scores -= 1
    return Student(name, group_id, progress)

def compare_str_byabc(left_str: str, right_str: str, direction = "<"):
    if len(left_str) == 0 or len(right_str) == 0: return False
    if direction == "<":
        if len(left_str) == 0 and len(right_str) != 0: return True
        elif len(left_str) != 0 and len(right_str) == 0: return False
        else:
            if left_str[0] < right_str[0]: return True
            elif left_str[0] > right_str[0]: return False
            else: return compare_str_byabc(left_str[1:], right_str[1:], direction)
    elif direction == ">":
        if len(left_str) != 0 and len(right_str) == 0: return True
        elif len(left_str) == 0 and len(right_str) != 0: return False
        else:
            if left_str[0] > right_str[0]: return True
            elif left_str[0] < right_str[0]: return False
            else: return compare_str_byabc(left_str[1:], right_str[1:], direction)
            

def sort_student_list_byname(student_list: list):
    for i in range(0, len(student_list)):
        for j in range(i + 1, len(student_list)):
            if compare_str_byabc(student_list[j].name, student_list[i].name, "<"):
                swap_value = student_list[i]
                student_list[i] = student_list[j]
                student_list[j] = swap_value
    return student_list

def filter_student_byavgscore(student_list: list, avg_score_cap = 3.5):
    result = []
    for student in student_list:
        if student.avg_score <= avg_score_cap: result.append(student)
    return result

student_group_101 = []
for i in range(0, 31):
    student_group_101.append(generate_random_student(group_id = 101))

low_score = 3.6
sorted_list = (sort_student_list_byname(student_group_101))
low_score_student_list = filter_student_byavgscore(sorted_list,low_score)

print("Сгенерированный список:")
for i in range(0, 31):
    print(student_group_101[i])
print("_______________________________________________________________________\nОтсортированный список:")
for i in range(0, 31):
    print(sorted_list[i])
print(f"_______________________________________________________________________\nСписок студентов со средней оценкой ниже {low_score}:", end = "")
if len(low_score_student_list) > 0:
    print("\n")
    for i in range(0, len(low_score_student_list) - 1):
        print(low_score_student_list[i])
else: print(" нет таких!")