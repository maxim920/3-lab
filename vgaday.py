from random import randint 

print ("Введите ваше число 1 до 5")
print ("Попробуй угадать мое число ")
your = input(" > ")
my = (randint(1,5))

print ("Твое число", your)
print ("Мое число ", my)

if your == my:
    print ("Ты выиграл")
if your != my:
    print ("Ты проиграл")