# проект 2
import random

answers = [
    "Бесспорно",
    "Мне кажется - да",
    "Пока неясно, попробуй снова",
    "Даже не думай",
    "Предрешено",
    "Вероятнее всего",
    "Спроси позже",
    "Мой ответ - нет",
    "Никаких сомнений",
    "Хорошие перспективы",
    "Лучше не рассказывать",
    "По моим данным - нет",
    "Можешь быть уверен в этом",
    "Да",
    "Сконцентрируйся и спроси опять",
    "Весьма сомнительно",
]

print("Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.")
print("Как я могу к тебе обращаться?")
name = input()
print("Привет,", name)

while name:
    print("Какой у тебя вопрос?")
    question = input()
    print(random.choice(answers))
    print("Хочешь задать еще вопрос?")
    da_net = input()
    if da_net == "да" or da_net == "хочу":
        continue
    else:
        break
print("Возвращайся если возникнут вопросы!")
