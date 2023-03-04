from django import template


register = template.Library()

@register.filter()
def censor(text):
    try:
        text = text.replace("Яндекс", "Я*****")
        text = text.replace("RuStore", "R******")
        return text
    except TypeError as e:
        print(f'Ошибка {e}. Тип данных должен быть str.')

# слова заменяются в публикациях .../news/2 и .../news/4