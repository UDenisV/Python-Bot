# не забудьте вставить токен!!!
import telebot
from telebot import types

bot = telebot.TeleBot('ваш токен')


@bot.message_handler(commands=['start'])
def welcome(message):
    print(message)
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttom1 = types.KeyboardButton("информация")
    buttom2 = types.KeyboardButton("меню")
    buttom3 = types.KeyboardButton("поддержка")

    menu.add(buttom1, buttom2, buttom3)
    bot.send_message(message.chat.id, 'Привет, {0.first_name}!'.format(
        message.from_user), reply_markup=menu)


@bot.message_handler(commands=['lessons'])
def les(message):
    print(message)
    lesson = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttom4 = types.KeyboardButton("понедельник")
    buttom5 = types.KeyboardButton("вторник")
    buttom6 = types.KeyboardButton("среда")
    buttom7 = types.KeyboardButton("четверг")
    buttom8 = types.KeyboardButton("пятница")

    lesson.add(buttom4, buttom5, buttom6, buttom7, buttom8)
    bot.send_message(message.chat.id, 'Выберете день недели',
                     reply_markup=lesson)


@bot.message_handler(content_types=['text', 'document', 'audio'])
def get_messages(message):
    if message.chat.type == 'private':
        if (message.text == 'информация'):
            bot.send_message(
                message.chat.id, 'Данный бот создан для учеников и учителей.Он умеет выполнять множество функций, которые помогают в учебе и преподовании. Команды бота вы можете узнать в Меню')
        elif (message.text == 'поддержка'):
            bot.send_message(
                message.chat.id, 'Контакты создателя:\n1. Почта - ваша почта\n2. Телеграм - ваш телеграм\n3. Дискорд - ваш дискорд')
        elif (message.text == 'меню'):
            bot.send_message(
                message.chat.id, 'Меню комманд:\n1. Посмотреть расписание - /lessons')
        elif (message.text == 'понедельник'):
            bot.send_message(
                message.chat.id, 'Расписание на понедельник:\n1. Русский язык\n2. Алгебра\n3. Литература\n4. Физкультура\n5. Биология')
        elif (message.text == 'вторник'):
            bot.send_message(
                message.chat.id, 'Расписание на вторник:\n1. Английский язык\n2. География\n3. Геометрия\n4. Химия\n5. Теория вероятностей')
        elif (message.text == 'среда'):
            bot.send_message(
                message.chat.id, 'Расписание на среду:\n1. Родной язык\n2. Физика\n3. Русский язык\n4. Алгебра\n5. Геометрия')
        elif (message.text == 'четверг'):
            bot.send_message(
                message.chat.id, 'Расписание на четверг:\n1. Геометрия\n2. Теория вероятностей\n3. Физика\n4. Литература\n5. Физкультура')
        elif (message.text == 'пятница'):
            bot.send_message(
                message.chat.id, 'Расписание на пятницу:\n1. Русский язык\n2. Литература\n3. Химия\n4. Алгебра\n5. Алгебра')


while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(e)
        bot.polling(none_stop=True)
