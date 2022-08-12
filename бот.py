import logging
import aiogram
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5438990312:AAFIs3EKYGHhinHA8GQjBzxFKxliRUtXu_o'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(lambda message: message.text == "/start")
async def start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup()
    button_1 = types.KeyboardButton(text="Поливальные установки")
    keyboard.add(button_1)
    button_2 = "Люки теплосети"
    keyboard.add(button_2)
    button_3 = "Инструкция подключения"
    keyboard.add(button_3)
    button_4 = "Управление"
    keyboard.add(button_4)
    button_5 = "Обновить"
    keyboard.add(button_5)
    await message.answer("Просмотр состояние оборудавания:", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == "Обновить")
async def obnov(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup()
    button_1 = types.KeyboardButton(text="Поливальные установки")
    keyboard.add(button_1)
    button_2 = "Люки теплосети"
    keyboard.add(button_2)
    button_3 = "Инструкция подключения"
    keyboard.add(button_3)
    button_4 = "Управление"
    keyboard.add(button_4)
    button_5 = "Обновить"
    keyboard.add(button_5)
    await message.answer("Просмотр состояние оборудавания:", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Назад")
async def nope(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup()
    button_1 = types.KeyboardButton(text="Поливальные установки")
    keyboard.add(button_1)
    button_2 = "Люки теплосети"
    keyboard.add(button_2)
    button_3 = "Инструкция подключения"
    keyboard.add(button_3)
    button_4 = "Управление"
    keyboard.add(button_4)
    button_5 = "Обновить"
    keyboard.add(button_5)
    await message.answer("Просмотр состояние оборудавания:", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Поливальные установки")
async def any_text_message1(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup()
    button_1 = types.KeyboardButton(text="Доп информация")
    keyboard.add(button_1)
    button_2 = "Назад"
    keyboard.add(button_2)
    await message.answer(f"Все установки кроме 7-ой и 9-ой находятся в хорошем состоянии, установка номер 7 требуем проверки, установка номер 9 требует ремонт.", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Доп информация")
async def any_text_message2(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup()
    button_1 = types.KeyboardButton(text="Назад")
    keyboard.add(button_1)
    await message.answer(f"✅ #1 установка: состояние в норме проверка не требуется.",reply_markup=keyboard)
    await message.answer(f"✅ #2 установка: состояние в норме проверка не требуется.",reply_markup=keyboard)
    await message.answer(f"✅ #3 установка: состояние в норме проверка не требуется.",reply_markup=keyboard)
    await message.answer(f"✅ #4 установка: состояние в норме проверка не требуется.",reply_markup=keyboard)
    await message.answer(f"✅ #5 установка: состояние в норме проверка не требуется.",reply_markup=keyboard)
    await message.answer(f"✅ #6 установка: состояние в норме проверка не требуется.",reply_markup=keyboard)
    await message.answer(f"⚠️ #7 установка: состояние в норме, но требуется проверка.",reply_markup=keyboard)
    await message.answer(f"✅ #8 установка: состояние в норме проверка не требуется.",reply_markup=keyboard)
    await message.answer(f"❌ #9 установка: требуется ремонт. Советую позвонить по номеру +7(960)07-44-121",reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Люки теплосети")
async def any_text_message3(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup()
    button_1 = types.KeyboardButton(text="Доп. информация")
    keyboard.add(button_1)
    button_2 = "Назад"
    keyboard.add(button_2)
    await message.answer(f"Все люки кроме 2-го и 5-го находятся в хорошем состоянии, люк номер 2 отсутсвует, люк номер 5 требует проверки.", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Доп. информация")
async def any_text_message4(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup()
    button_1 = types.KeyboardButton(text="Назад")
    keyboard.add(button_1)
    await message.answer(f"✅ #1 люк: состояние в норме проверка не требуется.",reply_markup=keyboard)
    await message.answer(f"✅ #2 люк: состояние в норме проверка не требуется.",reply_markup=keyboard)
    await message.answer(f"⚠ #3 люк: люк не найден.",reply_markup=keyboard)
    await message.answer(f"✅ #4 люк: состояние в норме проверка не требуется.",reply_markup=keyboard)
    await message.answer(f"✅ #5 люк: состояние в норме проверка не требуется.",reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Инструкция подключения")
async def any_text_message5(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup()
    button_1 = types.KeyboardButton(text="Назад")
    keyboard.add(button_1)
    await message.answer(f"Для подключения нашего бота к вашим поливательным устройствам и люкам теплосети, вам нужно скачать наше приложение, купить специализированные датчики, и подключить их к вашим устройствам. Инструкция по подключению на упаковке",reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Управление")
async def any_text_message6(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup()
    button_1 = types.KeyboardButton(text="Настроить полив")
    keyboard.add(button_1)
    button_2 = "Остановить полив"
    keyboard.add(button_2)
    button_3 = "Назад"
    keyboard.add(button_3)
    await message.answer("Управление поливальными установками:", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Настроить полив")
async def any_text_message7(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup()
    button_1 = types.KeyboardButton(text="Назад")
    keyboard.add(button_1)
    await message.answer("❗ Устройство не подключено!", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Остановить полив")
async def any_text_message8(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup()
    button_1 = types.KeyboardButton(text="Назад")
    keyboard.add(button_1)
    await message.answer("❗️ Устройство не подключено!", reply_markup=keyboard)
    
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
