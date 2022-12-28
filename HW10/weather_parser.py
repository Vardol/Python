# response = requests.get('https://api.gismeteo.net/v2/weather/current/4368/', headers={"X-Gismeteo-Token":"56b30cb255.3443075","Accept-Encoding":"gzip"})
# print(response.text)


# response = requests.get('https://api.gismeteo.net/v2/weather/current/4368/', headers={"X-Gismeteo-Token":"56b30cb255.3443075","Accept-Encoding":"gzip"})
# response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric&lang=ru").text
# API_key = '4321a3d417b53045aa1b6617c529c910'
# city_name = 'Kazan'


import requests
from bs4 import BeautifulSoup as bs

def list_tostr(input_lst: list):
    result = []
    for element in input_lst:
        result.append(str(element))
    return result

def temp_str_cropper(temp_str: str):
    if not temp_str[0].isdigit() and temp_str[0] != "-": temp_str = temp_str_cropper(temp_str[1:])
    if not temp_str[len(temp_str) - 1].isdigit(): temp_str = temp_str_cropper(temp_str[:(len(temp_str) - 1)])
    return temp_str


url = "https://pogoda.mail.ru/prognoz/kazan/"
response = requests.get(url).text
#print(response)
with open("response.txt","w",encoding="utf-8") as file:
    file.write(response)

# <div class="day__temperature" title="Днем">-6°
# 											<span class="day__temperature__night" title="Ночью">-11°</span>
# 										</div>

def tod_weather():
    soup = bs(response, 'html.parser')
    weather = str(soup.find('div', class_="information__content__temperature"))
    return temp_str_cropper(weather[weather.find("°")-3:weather.find("°")])

def tom_weather():
    soup = bs(response, 'html.parser')
    weather = soup.find('a', class_="day__link")
    weather = weather.find('div', class_="day__temperature")
    weather_night = str(weather.find('span', class_="day__temperature__night"))
    weather_day = str(weather)
    weather_day = weather_day[:weather_day.find("span")]
    return str(f"днем {temp_str_cropper(weather_day)}, ночью {temp_str_cropper(weather_night)}.")


# today_temp_index = response.find('<meta name="mrc__share_title" content="') + 80
# today_temp_str = response[today_temp_index:today_temp_index+4]
# print(temp_str_cropper(today_temp_str))
