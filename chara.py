#git config --global user.name "FIRST_NAME LAST_NAME"
#git config --global user.email "MY_NAME@example.com"
import logging
import requests
import datetime
from aiogram import Bot, Dispatcher, executor, types

weather_token = "6e8d79779a0c362f14c60a1c7f363e29"
API_TOKEN = '6156252770:AAEo3TMNCMp96ZCf06Xt1UkQ25xKaiDZJZQ'

logging.basicConfig(level=logging.INFO)

chara_bot = Bot(token=API_TOKEN)
dp = Dispatcher(chara_bot)

@dp.message_handler(commands=['start', 'help'])
async def welcome(message: types.Message):
    await message.reply("Привецтвую! \nЯ Чара, и нет вы не проходили геноцид(наверное) я бот помошник. \nВот чем я могу помочь :з")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons_row1 = ["Weather\U0001F30D", "Anime\U0001F60D"]
    buttons_row2 = ["Undetale\U0001F970", "Deltarune\U0001F30C"]
    keyboard.add(*buttons_row1)
    keyboard.add(*buttons_row2)
    await message.answer("Обери одну з функцій внизу: ", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == "Weather\U0001F30D")
async def name_city(message: types.Message):
    await message.reply("Введіть назву міста: ")

    @dp.message_handler(lambda message: message.text != "Anime\U0001F60D"
                                        and message.text != "Undetale\U0001F970"
                                        and message.text != "Deltarune\U0001F30C")

    async def without_puree(message: types.Message):
        try:
            r1 = requests.get(
                f"http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={weather_token}&units=metric")
            data = r1.json()
            city = data["name"]
            temperature = round(data["main"]["temp"])
            humidity = round(data["main"]["humidity"])
            wind = round(data["wind"]["speed"])
            await message.reply(f"***{datetime.datetime.now().strftime('%b %d %Y %H:%M')}***\n"
                                f"Погода в місті: {city}\n\U0001F321Температура: {temperature} C°\n"
                                f"\U0001F4A7Вологість повітря: {humidity} %\n"
                                f"\U0001F32AВітер: {wind} м/с\n ")
        except:
            await message.reply("\U0001F3D9 Провірте назву міста \U0001F3D9")

@dp.message_handler(lambda message: message.text == "Anime\U0001F60D")
async def name_city(message: types.Message):
    await message.reply("Вот небольшой список прикольных аниме: \n1.О моем перерожении в слизь \n2.Твоя апрельская ложь \n3.Человек-бензопила \n4.Необъятный океан \n5.Реинкарнация безработного \n6.Песнь ночных сов \n7.Лес где мерцают светлячки \n8.Великий из бродячих псов \n9.Евангелион \n10.Синий экзорцист")

@dp.message_handler(lambda message: message.text == "Undetale\U0001F970")
async def name_city(message: types.Message):
    await message.reply("Андертейл топ!")
    await message.reply("РЕШИМОСЬ!")
    await message.reply("Не здавайся!")
    await message.reply("ШОКОЛАД!")
    await message.reply("Будь оКОСТЬенным!")
    await message.reply("мммм ирисково-коричный пирог...")
    await message.reply("ЧЕЛОВЕК Я В ТЕБЯ ВЕРЮ!")
    await message.reply("Давай полежим на полу и почуствуем себя мусором, семейная традиция")
    await message.reply("Ооо да! Это гламур детка!")
    await message.reply("Нья! Давай сражатся")
    await message.reply("Где ножи?")
    await message.reply("Хой! Я тэм! Тэм любит людей! Люди милые :з")
    await message.reply("Наши надежды и мечты в твоих руках!")

@dp.message_handler(lambda message: message.text == "Deltarune\U0001F30C")
async def name_city(message: types.Message):
    await message.reply("Дельтарун топ!")
    await message.reply("ТОБИ ВЫПУСТИ ПРОДОЛЖЕНИЕ!")
    await message.reply("Это что Санс?")
    await message.reply("Ральзей милашка :з")
    await message.reply("КРИС ЛОВИ БАНАН!")
    await message.reply("Ууу темное королевство")
    await message.reply("Ноель и Сьюзи канон!")
    await message.reply("Пошли поедим мел")
    await message.reply("Мммм ирисково-коричный пирог...")
    await message.reply("Блин я в клетке(((")
    await message.reply("Когда новая глaва?")
    await message.reply("Лол это ловушка?")
    await message.reply("Крис положи нож на место 0_0")
    await message.reply("So, I'm with you in the dark...")
    await message.reply("Dont forget")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)