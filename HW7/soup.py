# Написать программу, где создадим класс Soup (для определения типа супа), принимающий 1 аргумент - который отвечает за основной продукт к выбираемому супу.
# В этом классе создать метод show_my_soup(), выводящий на печать «Суп - {Основной продукт}» в случае наличия добавки
# Это как доп к этой задаче - иначе отобразится следующая фраза: «Обычный кипяток»

class Soup:
    def __init__(self, ingredient = ""):
        self.name = "Кипяток"
        self.ingredient = ingredient
        if isinstance(ingredient, str) and ingredient.lower()  == "капуста": self.name = "Щи"
        if isinstance(ingredient, str) and ingredient.lower()  == "свекла": self.name = "Свекольник"
        if isinstance(ingredient, str) and ingredient.lower()  == "картошка": self.name = "Картофельный"
        if isinstance(ingredient, str) and ingredient.lower()  == "лук": self.name = "Луковая водичка"
        if isinstance(ingredient, str) and ingredient.lower()  == "мясо": self.name = "Мясной бульон"
        if isinstance(ingredient, str) and ingredient.lower()  == "курица": self.name = "Куриный бульон"
        if isinstance(ingredient, str) and ingredient.lower()  == "рыба": self.name = "Уха"

    def show_my_soup(self):
        print(f"Суп - {self.ingredient}")

    def __str__(self) -> str:
        return self.name

schi = Soup("Капуста")
bulgone = Soup("Мясо")

print(schi)
print(bulgone)

schi.show_my_soup()
bulgone.show_my_soup()
