import telebot

from telebot import types
import random

Name='Alex'
food=10
gold=0
stamin=10


TOKEN=''
Bot=telebot.TeleBot(TOKEN)

@Bot.message_handler(commands=['info'])
def info(message):
    Bot.send_message(message.chat.id,message.text)
    Bot.send_message(message.chat.id,message)
    print('test')



# @TOKEN.message_handler(commands=['translate'])

# def translate(message):
#     markup = types.InlineKeyboardMarkup()
#     markup.add(types.InlineKeyboardButton("Первая кнопка",url='https://translate.yandex.ru/'))
#     TOKEN.send_message(message.chat.id,'Ты чего спроси нормально !',reply_markup=markup)
#     print('test')

def print_stat(stat):
    # return ("|" * stat)
    return (stat)
def print_info(message):
    Bot.send_message(message.chat.id,f"{Name} Золото={gold}  \nСытость={print_stat(food)} \nСилы=      {print_stat(stamin)}")

@Bot.message_handler(commands=['game'])

def game(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=3)
    print('test')
    do_task = types.KeyboardButton('Сделать задание!')
    sleep = types.KeyboardButton('Отдохнуть')
    eat = types.KeyboardButton('Поесть')
    markup.add(do_task,sleep,eat)
    Bot.send_message(message.chat.id,f"{Name} Золото={gold}  \nСытость={print_stat(food)} \n \tСилы={print_stat(stamin)}")
    
    
    
    
@Bot.message_handler()
def user_text(message):
    global food , gold ,stamin
    if(food <= 0 or gold <= -1 or stamin <= 0):
        Bot.send_message(message.chat.id,"Вы проиграли")
        died=open("d:\\bot\main\youdied.jpg",'rb')
        Bot.send_photo(message.chat.id,died)
        exit(0)

    
    if message.text == "Сделать задание!":
        rnd = random.randint (0,10)
        print(rnd)
        if rnd == 10:
            Bot.send_message(message.chat.id,"Ого большая награда +5 золотых")
            food-=2
            gold+=5
            stamin-=2
            print_info(message)
        elif rnd <= 1:
            Bot.send_message(message.chat.id,"Блин тебе не повезло!")
            food-=2
            stamin-=2
            print_info(message)
        else:
            Bot.send_message(message.chat.id,f"Молодец хорошо поработал! +{round(rnd/3)} золотых")
            food-=2
            gold+=round(rnd/3)
            stamin-=2
            print_info(message)
    if message.text == "Отдохнуть":
        gold=gold-1
        stamin=stamin+10
        if stamin>10:
            stamin=10
        print_info(message)
    if message.text == "Поесть":
        gold=gold-1
        food=food+10
        if food>10:
            food=10
        print_info(message)
    
# @TOKEN.message_handler()
# def user_text(message):
#     if message.text == "Привет":
#         if message.chat.last_name is None: # message.chat.last_name == None
#             TOKEN.send_message(message.chat.id,f"Приветики {message.chat.first_name}")
#         else:
#             TOKEN.send_message(message.chat.id,f"Приветики {message.chat.first_name} {message.chat.last_name} ")


#     elif message.text == "Пока" :
#         TOKEN.send_message(message.chat.id,'Bye bye')
#     else:
#         TOKEN.send_message(message.chat.id,'Ты чего спроси нормально !')



Bot.polling(non_stop=True)
