import requests
from bs4 import BeautifulSoup as bs

#метод для извлечени русского текста из str
def extract_rus_text(input_str: str):
    rus_dict = ("абвгдеёжзийклмнопрстуфхцчшщъыьэюя")
    start_index = 0
    end_index = len(input_str) - 1
    for i in range(0, len(input_str)):
        if input_str[i].lower() in rus_dict:
            start_index = i
            break
    for i in range(len(input_str) - 1, -1, -1):
        if input_str[i].lower() in rus_dict:
            end_index = i + 1
            break
    return input_str[start_index:end_index]

#метод для конвертации всех элементов списка в str
def list_tostr(input_lst: list):
    result = []
    for element in input_lst:
        result.append(str(element))
    return result

#метод для удаления дубликатов из списка
def filter_list_for_duplicates(input_lst: list):
    result = []
    for element in input_lst:
        if element not in result: result.append(element)
    return result


url = "https://rt.rbc.ru"
response = requests.get(url).text

#для удобства пишу ответ в файл
with open("response.txt","w",encoding="utf-8") as file:
    file.write(response)

soup = bs(response, 'html.parser') #делаю суп
news = list(soup.findAll('span', class_="news-feed__item__title news-feed__item_in-main")) #забираю список новостей по основному классу
news.extend(list(soup.findAll('span', class_="main__feed__title"))) #забираю список новостей по второму классу, добавляю к первому

#дальше соответственно конвертирую все в строки, вытаскиваю русский текст, убираю дубли и вывожу на экран.
news = list_tostr(news)
for i in range(0, len(news)):
    news[i] = extract_rus_text(news[i]) + "."

news = filter_list_for_duplicates(news)

def main():
    return news    
    
#for text in news:
#    print(text)
    