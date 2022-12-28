# response = requests.get('https://api.gismeteo.net/v2/weather/current/4368/', headers={"X-Gismeteo-Token":"56b30cb255.3443075","Accept-Encoding":"gzip"})
# print(response.text)


# response = requests.get('https://api.gismeteo.net/v2/weather/current/4368/', headers={"X-Gismeteo-Token":"56b30cb255.3443075","Accept-Encoding":"gzip"})
# response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric&lang=ru").text
# API_key = '4321a3d417b53045aa1b6617c529c910'
# city_name = 'Kazan'


import requests
from bs4 import BeautifulSoup as bs

def temp_str_2int(temp_str: str):
    for i in temp_str:
        if not i.isdigit() and i != "-": temp_str = temp_str[1:]
        else: break
    for i in temp_str:
        if not i.isdigit() and i != "-":
            temp_str = temp_str[:i.find(temp_str) - 1]
            break
    return int(temp_str)


url = "https://pogoda.mail.ru/prognoz/kazan/"
response = requests.get(url).text
#print(response)
with open("response.txt","w",encoding="utf-8") as file:
    file.write(response)


soup = bs(response, 'html.parser')
news = list(soup.findAll('span', class_="news-feed__item__title news-feed__item_in-main"))
news.extend(list(soup.findAll('span', class_="main__feed__title")))
news = list_tostr(news)

today_temp_index = response.find('<meta name="mrc__share_title" content="') + 81
today_temp_str = response[today_temp_index:today_temp_index+3]
print(temp_str_2int(today_temp_str))
