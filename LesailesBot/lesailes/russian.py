from aiogram import types, Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputMedia, WebAppInfo
import asyncio
from random import randint


# TOKEN = "7702041998:AAGYq7SjeufGnJQ4OFAr2zrzqVP7VyD6nCM"
#
# bot = Bot(token=TOKEN)
# dp = Dispatcher()
# user_data = {}



# @dp.message()
async def handle_text_r(message: types.Message, user_data):
    user_id = message.from_user.id
    # if user_id not in user_data or message.text == "/start":
    #     await start(message)
    if "holat" not in user_data[user_id]:
        await shaxarlar(message, user_data)
    elif "shaxar" not in user_data[user_id]:
        await menu(message, user_data)
    elif message.text == "/boshmenu":
        await menu(message, user_data)
    elif message.text == "🛍 Сделать заказ":
        await order(message, user_data)
    elif message.text == "🔥 Акции":
        await sale(message, user_data)
    elif message.text == "🙋🏻‍♂️ Присоединяйтесь к нашей команде":
        await team(message, user_data)
    elif message.text == "☎️ Связаться с Les Ailes":
        await call(message, user_data)
    elif message.text == "⬅️ Назад":
        await menu(message, user_data)
    elif message.text == "📖 История заказов":
        await history(message, user_data)
    elif message.text == "💬 Свяжитесь с нами":
        await bizbilanaloqa(message, user_data)
    elif message.text == "✍️ Оставить отзыв":
        await fikr(message, user_data)
    elif message.text == "◀️ Назад":
        await call(message, user_data)
    elif message.text == "⚙️Настройки ℹ️ Информация":
        await sozlamalar(message, user_data)
    elif message.text == "Изменить имя":
        await ism(message, user_data)
    elif message.text == "🔽 Назад" or message.text == "⤵️ Назад":
        await sozlamalar(message, user_data)
    elif "ismlarr" in user_data[user_id]:
        await checkname(message, user_data)
        await sozlamalar(message, user_data)
    elif message.contact is not None or "+998" in message.text:
        await ask_phone(message, user_data)
    elif "ver_code" in user_data[user_id]:
        await check_code(message, user_data)
    elif message.text == "📱 Изменить номер":
        await history(message, user_data)
    return user_data


# @dp.message(Command("start"))
# async def start(message: types.Message):
#     user_id = message.from_user.id
#     user_data[user_id] = {}
#     button = [
#         [types.KeyboardButton(text="🇷🇺 Русский"), types.KeyboardButton(text="🇺🇿 Узбекча"),
#          types.KeyboardButton(text="🇺🇸 English")],
#     ]
#     keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
#     await message.answer(
#         "Здравствуйте! Добро пожаловать в службу доставки Les Ailes.\n\n"
#         "Hello! Welcome to Les Ailes delivery service.",
#         reply_markup=keyboard)
#     print(1, user_data)


async def shaxarlar(message: types.Message, user_data):
    user_id = message.from_user.id
    language = message.text
    # if message.text == '🇷🇺 Русский':
    #     await til()
    # else:
    user_data[user_id]["holat"] = language
    button = [
        [types.KeyboardButton(text="Ташкент"), types.KeyboardButton(text="Андижан")],
        [types.KeyboardButton(text="Самарканд"), types.KeyboardButton(text="Фергана")],
        [types.KeyboardButton(text="Бухара"), types.KeyboardButton(text="Маргилан")],
        [types.KeyboardButton(text="Нукус"), types.KeyboardButton(text="Хоразм")],
        [types.KeyboardButton(text="Чирчик"), types.KeyboardButton(text="Коканд")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("В каком городе вы живете? \nПожалуйста, выберите город:", reply_markup=keyboard)
    print(2, user_data)


city = [
    "Ташкент", "Андижан",
    "Самарканд", "Фергана",
    "Бухара", "Маргилан",
    "Нукус", "Хоразм",
    "Чирчик", "Коканд"
]


async def menu(message: types.Message, user_data):
    user_id = message.from_user.id
    if message.text in city:
        boshmenu = message.text
        user_data[user_id]["shaxar"] = boshmenu
    else:
        user_data[user_id]["shaxar01"] = message.text
    button = [
        [types.KeyboardButton(text="🛍 Сделать заказ")],
        [types.KeyboardButton(text="📖 История заказов")],
        [types.KeyboardButton(text="⚙️Настройки ℹ️ Информация"), types.KeyboardButton(text="🔥 Акции")],
        [types.KeyboardButton(text="🙋🏻‍♂️ Присоединяйтесь к нашей команде"),
         types.KeyboardButton(text="☎️ Связаться с Les Ailes")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("Главное меню", reply_markup=keyboard)
    print(3, user_data)


async def order(message: types.Message, user_data):
    user_id = message.from_user.id
    buyurtma = message.text
    user_data[user_id]["holat"] = buyurtma
    button = [
        [types.KeyboardButton(text="🏃 Забрать сам"), types.KeyboardButton(text="🚙 Доставка")],
        [types.KeyboardButton(text="⬅️ Назад")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("Заберите заказ самостоятельно 🙋‍♂️ или выберите доставку 🚙", reply_markup=keyboard)
    print(3, user_data)


async def sale(message: types.Message, user_data):
    user_id = message.from_user.id
    aksiya = message.text
    user_data[user_id]["holat"] = "акция"
    await message.answer("На данный момент акции в вашем городе нет")
    print(4, user_data)


async def team(message: types.Message, user_data):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "team"
    buttons = [
        [types.InlineKeyboardButton(text="Перейти", url="https://t.me/@HavoqandJamoa_Bot")],
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons, resize_keyboard=True)
    await message.answer(
        "Мы приглашаем вас присоединиться к нашей дружной команде! \nДля того, чтобы заполнить анкету, нажмите на кнопку.",
        reply_markup=keyboard)


async def call(message: types.Message, user_data):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "call"
    button = [
        [types.KeyboardButton(text="💬 Связаться с нами"), types.KeyboardButton(text="✍️ Оставить отзыв")],
        [types.KeyboardButton(text="⬅️ Назад")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("Если вы хотите связаться с нами или оставить комментарий, будем рады.",
                         reply_markup=keyboard)
    print(5, user_data)


async def bizbilanaloqa(message: types.Message, user_data):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "bizbilanaloqa"
    buttons = [
        [types.InlineKeyboardButton(text="💬 Связаться с нами", url="https://t.me/@lesaileshelpbot")],
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons, resize_keyboard=True)
    await message.answer("Если у вас есть вопрос или предложение, свяжитесь с нами.", reply_markup=keyboard)
    print(6, user_data)


async def history(message: types.Message, user_data):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "history"
    button = [
        [types.KeyboardButton(text="📞 Мой номер", request_contact=True)],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("Пожалуйста, пройдите регистрацию.")
    await message.answer("Для регистрации введите свой номер телефона!\nПример: +998xx xxx xx xx", reply_markup=keyboard)


async def ask_phone(message: types.Message, user_data):
    user_id = message.from_user.id
    i = '+1234567890'
    ok = True
    if message.contact is not None:
        phone_c = message.contact.phone_number
        user_data[user_id]['phone'] = phone_c
        ver_code = randint(100000, 999999)
        user_data[user_id]['ver_code'] = ver_code
        await message.answer(f"Код подтверждения отправлен на ваш номер \nПожалуйста, введите код: {ver_code}")
    elif len(message.text) == 13 and message.text[0:4] == '+998':
        for symbol in message.text:
            if symbol not in i:
                await message.answer('Неверно введен номер')
                ok = False
                break
        if ok == True:
            phone = message.text
            user_data[user_id]['phone'] = phone
            ver_code = randint(100000, 999999)
            user_data[user_id]['ver_code'] = ver_code
            await message.answer(f"Код подтверждения отправлен на ваш номер \nПожалуйста, введите код: {ver_code}")

    else:
        await message.answer('Неверно введен номер')
        print(user_data)

    print(7, user_data)


async def check_code(message: types.Message, user_data):
    user_id = message.from_user.id
    code = message.text
    ver_code = user_data[user_id]["ver_code"]
    if str(ver_code) == code:
        user_data[user_id]["status"] = "verified"
        await message.answer("Ваш номер подтвержден")
        await menu(message)
    else:
        await message.answer("Неверно введен код. Попробуйте снова")
    del user_data[user_id]['ver_code']
    print(user_data)


async def sozlamalar(message: types.Message, user_data):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "sozlamalar"
    button = [
        [types.KeyboardButton(text="Изменить имя"), types.KeyboardButton(text="📱 Изменить номер")],
        [types.KeyboardButton(text="🏙 Изменить город"), types.KeyboardButton(text="🇺🇿 Изменить язык")],
        [types.KeyboardButton(text="ℹ️ Информация о филиалах"), types.KeyboardButton(text="📄 Общее предложение")],
        [types.KeyboardButton(text="⬅️ Назад")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("Выберите действие:", reply_markup=keyboard)
    print(8, user_data)


async def ism(message: types.Message, user_data):
    user_id = message.from_user.id
    user_data[user_id]['ismlarr'] = "ism"
    button = [
        [types.KeyboardButton(text="🔽 Назад")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("Пожалуйста, введите ваше имя и фамилию.", reply_markup=keyboard)
    print(9, user_data)


async def checkname(message: types.Message, user_data):
    user_id = message.from_user.id
    checkname = message.text
    user_data[user_id]["name"] = checkname
    await message.answer("✅ Готово")
    del user_data[user_id]['ismlarr']


async def fikr(message: types.Message, user_data):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = fikr
    button = [
        [types.KeyboardButton(text="◀️ Назад"), types.KeyboardButton(text="✅ Подтвердить")],
    ]
    buttons = [
        [types.InlineKeyboardButton(text="Продукт", callback_data="mahsulot")],
        [types.InlineKeyboardButton(text="1😣", callback_data="sticker"),
         types.InlineKeyboardButton(text="2☹️", callback_data="sticker"),
         types.InlineKeyboardButton(text="3😐", callback_data="sticker"),
         types.InlineKeyboardButton(text="4😑", callback_data="sticker"),
         types.InlineKeyboardButton(text="5😍", callback_data="sticker"), ],
        [types.InlineKeyboardButton(text="Сервис", callback_data="xizmat")],
        [types.InlineKeyboardButton(text="1👊🏻", callback_data="sticker"),
         types.InlineKeyboardButton(text="2👎🏻", callback_data="sticker"),
         types.InlineKeyboardButton(text="3👌🏻", callback_data="sticker"),
         types.InlineKeyboardButton(text="4🤙🏻", callback_data="sticker"),
         types.InlineKeyboardButton(text="5👍🏻", callback_data="sticker"), ],
        [types.InlineKeyboardButton(text="Доставка", callback_data="yetkazib berish")],
        [types.InlineKeyboardButton(text="1🐌", callback_data="sticker"),
         types.InlineKeyboardButton(text="2🐢", callback_data="sticker"),
         types.InlineKeyboardButton(text="3🛺", callback_data="sticker"),
         types.InlineKeyboardButton(text="4🏎", callback_data="sticker"),
         types.InlineKeyboardButton(text="5🚀", callback_data="sticker"), ],
    ]
    keyboards = types.InlineKeyboardMarkup(inline_keyboard=buttons, resize_keyboard=True)
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("✅ Отзывы о сервисе Les Ailes.", reply_markup=keyboards)
    await message.answer("Спасибо за ваш выбор! Пожалуйста, оцените наш сервис по 5-бальной шкале.", reply_markup=keyboard)
    print(8, user_data)


# async def main():
#     print('Бот работает...')
#     # await dp.start_polling(bot)
#
#
# asyncio.run(main())
# rus tili qo'shildi
