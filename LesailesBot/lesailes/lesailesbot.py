import aiogram
from aiogram import types, Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputMedia, WebAppInfo, message
import asyncio
from random import randint

from pyexpat.errors import messages

from funtions import *

from russian import handle_text_r

TOKEN = "7702041998:AAGYq7SjeufGnJQ4OFAr2zrzqVP7VyD6nCM"

bot = Bot(token=TOKEN)
dp = Dispatcher()
user_data = {}


@dp.message()
async def handle_text(message: types.Message):
    user_id = message.from_user.id
    if user_id not in user_data or message.text == "/start":
        await start(message)
    elif "holat" not in user_data[user_id]:
        await shaxarlar(message)
    elif "shaxar" not in user_data[user_id]:
        await menu(message)
    elif message.text == "/boshmenu":
        await menu(message)
    elif message.text == "🛍 Buyurtma berish" or message.text == "↙️ Ortga":
        await order(message)
    elif message.text == "🔥 Aksiya":
        await sale(message)
    elif message.text == "🙋🏻‍♂️ Jamoamizga qo'shiling":
        await team(message)
    elif message.text == "☎️ Les Ailes bilan aloqa":
        await call(message)
    elif message.text == "⬅️ Ortga":
        await menu(message)
    elif message.text == "📖 Buyurtmalar tarixi":
        await history(message)
    elif message.text == "💬 Biz bilan aloqaga chiqing":
        await bizbilanaloqa(message)
    elif message.text == "✍️ Fikr bildirish":
        await fikr(message)
    elif message.text == "◀️ Ortga":
        await call(message)
    elif message.text == "⚙️Sozlash ℹ️ Ma'lumotlar":
        await sozlamalar(message)
    elif message.text == "Isimni o'zgartirish":
        await ism(message)
    elif message.text == "🔽 Ortga" or message.text == "⤵️ Ortga":
        await sozlamalar(message)
    elif "ismlarr" in user_data[user_id]:
        await checkname(message)
        await sozlamalar(message)
    elif message.contact is not None or "+998" in message.text:
        await ask_phone(message)
    elif "ver_code" in user_data[user_id]:
        await check_code(message)
    elif message.text == "📱 Raqamni o'zgartirish":
        await history(message)
    elif message.text == "🏃 Olib ketish":
        await olibketish(message)
    elif message.text == "🌐 Bu yerda buyurtma berish":
        await website(message)
    elif message.text == "Filialni tanlang" or message.text == "↩️ Ortga":
        await filialnitanlash(message)
    elif message.text == "🚙 Yetkazib berish":
        await yetkazibberish(message)
    elif message.text == "🗺 Mening manzillarim":
        await manzil(message)
    elif message.text in lists or message.text == "↪️ Ortga":
        await asosiymenu(message)
    # elif message.text not in lists:
    #     await yopiqmanzil(message)
    elif message.text in main_menu or message.text == "↖️ Ortga":
        await menu_tekshiruv(message)
    elif message.text in taom:
        await savat(message)
    elif message.text in ichimliklar:
        await ichimlik_zakaz(message)
    elif message.text == "📥 Savat":
        await show_cart(message)
    # elif message.text == "📥Savatga qo'shish✅":
    #     await mybasket(message)


@dp.message(Command("start"))
async def start(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id] = {}
    button = [
        [types.KeyboardButton(text="🇷🇺 Русский"), types.KeyboardButton(text="🇺🇿 O'zbekcha"),
         types.KeyboardButton(text="🇺🇸 English")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer(
        "Assalomu alaykum! Les Ailes yetkazib berish xizmatiga xush kelibsiz.\n\n"
        "Здравствуйте! Добро пожаловать в службу доставки Les Ailes.\n\n"
        "Hello! Welcome to Les Ailes delivery service.",
        reply_markup=keyboard)
    print(1, user_data)


async def shaxarlar(message: types.Message):
    user_id = message.from_user.id
    language = message.text
    if message.text == '🇷🇺 Русский':
        await handle_text_r(message, user_data)
    else:
        user_data[user_id]["holat"] = language
        button = [
            [types.KeyboardButton(text="Toshkent"), types.KeyboardButton(text="Andijon")],
            [types.KeyboardButton(text="Samarqand"), types.KeyboardButton(text="Farg'ona")],
            [types.KeyboardButton(text="Buxoro"), types.KeyboardButton(text="Marg'ilon")],
            [types.KeyboardButton(text="Nukus"), types.KeyboardButton(text="Xorazm")],
            [types.KeyboardButton(text="Chirchiq"), types.KeyboardButton(text="Qo'qon")],
        ]
        keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
        await message.answer("Qaysi shaharda yashaysiz? \nIltimos, shaharni tanlang:", reply_markup=keyboard)
        print(2, user_data)

city = [
    "Toshkent", "Andijon",
    "Samarqand", "Farg'ona",
    "Buxoro", "Marg'ilon",
    "Nukus", "Xorazm",
    "Chirchiq", "Qo'qon"
]

async def menu(message: types.Message):
    user_id = message.from_user.id
    if message.text in city:
        boshmenu = message.text
        user_data[user_id]["shaxar"] = boshmenu
    else:
        user_data[user_id]["shaxar01"] = message.text
    button = [
        [types.KeyboardButton(text="🛍 Buyurtma berish")],
        [types.KeyboardButton(text="📖 Buyurtmalar tarixi")],
        [types.KeyboardButton(text="⚙️Sozlash ℹ️ Ma'lumotlar"), types.KeyboardButton(text="🔥 Aksiya")],
        [types.KeyboardButton(text="🙋🏻‍♂️ Jamoamizga qo'shiling"),
         types.KeyboardButton(text="☎️ Les Ailes bilan aloqa")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("Bosh menyu", reply_markup=keyboard)
    print(3, user_data)


async def order(message: types.Message):
    user_id = message.from_user.id
    buyurtma = message.text
    user_data[user_id]["holat"] = buyurtma
    button = [
        [types.KeyboardButton(text="🏃 Olib ketish"), types.KeyboardButton(text="🚙 Yetkazib berish")],
        [types.KeyboardButton(text="⬅️ Ortga")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("Buyurtmani o'zingiz 🙋‍♂️ olib keting yoki Yetkazib berishni 🚙 tanlang", reply_markup=keyboard)
    print(3, user_data)


async def sale(message: types.Message):
    user_id = message.from_user.id
    aksiya = message.text
    user_data[user_id]["holat"] = "aksiya"
    await message.answer("Shahringizda hali aksiyalar mavjud emas")
    print(4, user_data)


async def team(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "team"
    buttons = [
        [types.InlineKeyboardButton(text="O'tish", url="https://t.me/@HavoqandJamoa_Bot")],
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons, resize_keyboard=True)
    await message.answer(
        "Ahil jamoamizda ishlashga taklif qilamiz! \nTelegramdan chiqmay, shu yerning o'zida anketani \nto'ldirish uchun quyidagi tugmani bosing.",
        reply_markup=keyboard)


async def call(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "call"
    button = [
        [types.KeyboardButton(text="💬 Biz bilan aloqaga chiqing"), types.KeyboardButton(text="✍️ Fikr bildirish")],
        [types.KeyboardButton(text="⬅️ Ortga")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("Agar siz bizga yozsangiz yoki sharh qoldirmoqchi bo'lsangiz, xursand bo'lamiz.",
                         reply_markup=keyboard)
    print(5, user_data)


async def bizbilanaloqa(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "bizbilanaloqa"
    buttons = [
        [types.InlineKeyboardButton(text="💬 Biz bilan aloqaga chiqing", url="https://t.me/@lesaileshelpbot")],
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons, resize_keyboard=True)
    await message.answer("Agar biron-bir savol yoki taklif bo'lsa, bizga aloqaga chiqing.", reply_markup=keyboard)
    print(6, user_data)


async def history(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "history"
    button = [
        [types.KeyboardButton(text="📞 Mening raqamim", request_contact=True),types.KeyboardButton(text="⬅️ Ortga")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("Avval ro'yxatdan o'ting.")
    await message.answer("Ro'yxatdan o'tish uchun telefon raqamingizni kiriting!\nMisol uchun, +998xx xxx xx xx",reply_markup=keyboard)


async def ask_phone(message: types.Message):
    user_id = message.from_user.id
    i = '+1234567890'
    ok = True
    if message.contact is not None:
        phone_c = message.contact.phone_number
        user_data[user_id]['phone'] = phone_c
        ver_code = randint(100000, 999999)
        user_data[user_id]['ver_code'] = ver_code
        await message.answer(f"Nomeringizga tasdiqlash kodi yuborildi \nIltimos kodni kiriting: {ver_code}")
    elif len(message.text) == 13 and message.text[0:4] == '+998':
        for symbol in message.text:
            if symbol not in i:
                await message.answer('Hato nomer kiritildi')
                ok = False
                break
        if ok == True:
            phone = message.text
            user_data[user_id]['phone'] = phone
            ver_code = randint(100000, 999999)
            user_data[user_id]['ver_code'] = ver_code
            await message.answer(f"Nomeringizga tasdiqlash kodi yuborildi \nIltimos kodni kiriting: {ver_code}")

    else:
        await message.answer('Hato nomer kiritildi')
        print(user_data)

    print(7, user_data)

async def check_code(message: types.Message):
    user_id = message.from_user.id
    code = message.text
    ver_code = user_data[user_id]["ver_code"]
    if str(ver_code) == code:
        user_data[user_id]["status"] = "verified"
        await message.answer("Nomeringiz tasdiqlandi")
        await menu(message)
    else:
        await message.answer("Kod xato terildi. Yana urinib ko'ring")
    del user_data[user_id]['ver_code']
    print(user_data)


async def sozlamalar(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "sozlamalar"
    button = [
        [types.KeyboardButton(text="Isimni o'zgartirish"), types.KeyboardButton(text="📱 Raqamni o'zgartirish")],
        [types.KeyboardButton(text="🏙 Shaharni o'zgartirish"), types.KeyboardButton(text="🇺🇿 Tilni o'zgartirish")],
        [types.KeyboardButton(text="ℹ️ Filallar haqida ma'lumot"), types.KeyboardButton(text="📄 Ommaviy taklif")],
        [types.KeyboardButton(text="⬅️ Ortga")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("Harakatni tanlang:", reply_markup=keyboard)
    print(8, user_data)


async def ism(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]['ismlarr'] = "ism"
    # user_data[user_id]['name'] = "change name"
    button = [
        [types.KeyboardButton(text="🔽 Ortga")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("Iltimos, ismingiz va familiyangizni kiriting.", reply_markup=keyboard)
    print(9, user_data)


async def checkname(message: types.Message):
    user_id = message.from_user.id
    checkname = message.text
    user_data[user_id]["name"] = checkname
    await message.answer("✅ Tayyor")
    del user_data[user_id]['ismlarr']



async def fikr(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = fikr
    button = [
        [types.KeyboardButton(text="◀️ Ortga"), types.KeyboardButton(text="✅ Tasdiqlash")],
    ]
    buttons = [
        [types.InlineKeyboardButton(text="Mahsulot", callback_data="mahsulot")],
        [types.InlineKeyboardButton(text="1😣", callback_data="sticker"),
         types.InlineKeyboardButton(text="2☹️", callback_data="sticker"),
         types.InlineKeyboardButton(text="3😐", callback_data="sticker"),
         types.InlineKeyboardButton(text="4😑", callback_data="sticker"),
         types.InlineKeyboardButton(text="5😍", callback_data="sticker"), ],
        [types.InlineKeyboardButton(text="Xizmat", callback_data="xizmat")],
        [types.InlineKeyboardButton(text="1👊🏻", callback_data="sticker"),
         types.InlineKeyboardButton(text="2👎🏻", callback_data="sticker"),
         types.InlineKeyboardButton(text="3👌🏻", callback_data="sticker"),
         types.InlineKeyboardButton(text="4🤙🏻", callback_data="sticker"),
         types.InlineKeyboardButton(text="5👍🏻", callback_data="sticker"), ],
        [types.InlineKeyboardButton(text="Yetkazib berish", callback_data="yetkazib berish")],
        [types.InlineKeyboardButton(text="1🐌", callback_data="sticker"),
         types.InlineKeyboardButton(text="2🐢", callback_data="sticker"),
         types.InlineKeyboardButton(text="3🛺", callback_data="sticker"),
         types.InlineKeyboardButton(text="4🏎", callback_data="sticker"),
         types.InlineKeyboardButton(text="5🚀", callback_data="sticker"), ],
    ]
    keyboards = types.InlineKeyboardMarkup(inline_keyboard=buttons, resize_keyboard=True)
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("✅ Les Ailes xizmati sharhi.", reply_markup=keyboards)
    await message.answer("Tanlovingiz uchun rahmat va biz ishimizni 5 balli tizimda baholashingizdan mamnun bo'lamiz.",
                         reply_markup=keyboard)
    print(8, user_data)


async def olibketish(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "olibketish"
    button = [
        [types.KeyboardButton(text="↙️ Ortga"),types.KeyboardButton(text="📍 Eng yaqin fillialni tanlang")],
        [types.KeyboardButton(text="🌐 Bu yerda buyurtma berish"), types.KeyboardButton(text="Filialni tanlang")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("Qayerdasiz 👀? Agar lokatsiyangizni📍 yuborsangiz, sizga eng yaqin filialni aniqlaymiz",reply_markup=keyboard)



async def website(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "website"

    # Tugmalarni aniqlash
    button = [
        [types.InlineKeyboardButton(text="O'tish", url="https://lesailes.uz/")],
    ]
    keyboards = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)

    # Rasm yuborish va matn bilan havolani qo'shish
    file_path = "images/images.png"
    caption_text = (
        "O'z joylashuvingiz bilan buyurtma bering -\n"
        "[https://lesailes.uz/](https://lesailes.uz/)"
    )

    await message.reply_photo(
        caption=caption_text,
        photo=types.FSInputFile(path=file_path),
        parse_mode="Markdown",  # Markdown formatida matnni formatlash
        reply_markup=keyboards  # Tugmalarni rasm bilan yuborish
    )

lists = {"Yunusobod":"Yunusobod \nA. Donish ko‘chasi, 80",
         "S.Rahimova":"S.Rahimov\nмахалля Яккабог, Чиланзарский район, Ташкент",
         "M-5":"M-5\nSh. Rashidov shox k. 16A",
         "Asia Nukus":"Asia Nukus\nMKAD, 19",
         "Farhod":"Farhod\nUchtepa t. G9A, 21/2",
         "Ko‘kcha":"Ko‘kcha\nShayxontohur t.\nKo‘kcha darvoza 3A",
         "Oybek":"Oybek\nShahrisabz ko‘chasi, 10b",
         "Samarqand Darvoza savdo markazi":"Samarqand Darvoza savdo markazi\nToshkent shahar, Qoratosh ko'chasi, 5A",
         "Chilonzor":"Chilonzor\n2-blok, 2-uy",
         "Next":"Next\nBobur ko‘chasi, 6-uy",
         "Zenit":"Zenit\n7-й квартал, 49, массив Юнусабад, Юнусабадский район, Ташкент",
         "Sergeli":"Sergeli\nGolden life KSM",
         "Buyuk ipak yo'li": "Buyuk ipak yo'li\n",
         }




async def filialnitanlash(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "filialnitanlash"
    button = [
        [types.KeyboardButton(text="Yunusobod"),types.KeyboardButton(text="S.Rahimova")],
        [types.KeyboardButton(text="Atlas"),types.KeyboardButton(text="M-5")],
        [types.KeyboardButton(text="Asia Nukus"),types.KeyboardButton(text="Farhod")],
        [types.KeyboardButton(text="Ko‘kcha"),types.KeyboardButton(text="Oybek")],
        [types.KeyboardButton(text="Parus"),types.KeyboardButton(text="Samarqand Darvoza")],
        [types.KeyboardButton(text="Chilonzor"),types.KeyboardButton(text="Next")],
        [types.KeyboardButton(text="Zenit"),types.KeyboardButton(text="Atlas")],
        [types.KeyboardButton(text="Buyuk ipak yo'li"),types.KeyboardButton(text="Sergili")],
        [types.KeyboardButton(text="↙️ Ortga")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("Qaysi filialdan olib ketishni tanlang",reply_markup=keyboard)



main_menu = [
    "🍱 Setlar", "🍗 Tovuq", "🍟 Sneklar", "🌯 Lesterlar",
    "🍔 Burgerlar", "🌭 Longerlar/Hot-dog", "🥤 Ichimliklar","🥗 Salatlar","🍩 Ponchiklar",
    "👶 Bolajonlarga", "🍅 Souslar",
]



async def asosiymenu(message: types.Message):
    user_id = message.from_user.id
    location = message.text
    if location == '↖️ Ortga' or location == '↪️ Ortga':
        loc = 'salom'
    else:
        loc = lists[location]
        await message.answer(f"{loc}")
        await bot.send_location(chat_id=message.from_user.id,
                                longitude=69.338328,
                                latitude=41.344346)
    user_data[user_id]["holat"] = "asosiymenu"
    button = [
        [types.KeyboardButton(text="↩️ Ortga"), types.KeyboardButton(text="📥 Savat")],
        [types.KeyboardButton(text="🍱 Setlar"), types.KeyboardButton(text="🍗 Tovuq")],
        [types.KeyboardButton(text="🍟 Sneklar"), types.KeyboardButton(text="🌯 Lesterlar")],
        [types.KeyboardButton(text="🍔 Burgerlar"), types.KeyboardButton(text="🌭 Longerlar/Hot-dog")],
        [types.KeyboardButton(text="🥤 Ichimliklar"), types.KeyboardButton(text="🥗 Salatlar")],
        [types.KeyboardButton(text="🍩 Ponchiklar"), types.KeyboardButton(text="👶 Bolajonlarga")],
        [types.KeyboardButton(text="🍅 Souslar")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("Nimadan boshlaymiz?", reply_markup=keyboard)




async def yetkazibberish(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "yetkazibberish"
    button = [
        [types.KeyboardButton(text="📍 Eng yaqin fillialni tanlang")],
        [types.KeyboardButton(text="↙️ Ortga"),types.KeyboardButton(text="🗺 Mening manzillarim")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("Buyurtmangizni qayerga yetkazib berish "
                         "kerak 🚙?\nAgar lokatsiyangizni📍 yuborsangiz, sizga "
                         "eng yaqin filialni va yetkazib berish xarajatlarini aniqlaymiz 💵",reply_markup=keyboard)



async def yopiqmanzil(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "yopiqmanzil"
    await message.answer("Afsuski, bu filial yopiq. 😔\n"
                             "Buyurtmani ish soatlarida berishga ishonch hosil qiling.\n"
                             "Les Ailes yetkazib berish xizmatini tanlaganingiz uchun tashakkur.")


async def manzil(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "manzil"
    await message.answer("Sizda saqlangan manzillar yo'q")


taom = [
    'Kombo set', '1+1 Sezar burger',"Qiyqiriq set",
    'Klassik set', "Do'stlar 1x", "Lester set",
    "Snek set", "Do'stlar 2x, achchiq", "4 Friends Klassik burger",
    "4 Friends Lester chiz", "Do'stlar 4x, achchiq", "1+1 Barbekyu burger", "Yangi set",
    "Skulll set", "Do'stlar 1x, achchiq", "Longer rings set", "Big set",
    "4 Friends Hot-dog", "4 Friends Longer chiz", "Do'stlar 4x"
]

async def menu_tekshiruv(message: types.Message):
    user_id = message.from_user.id
    choice = message.text
    if choice == '🍱 Setlar':
        await taomlar(message)
    elif choice == '🥤 Ichimliklar':
        await ichimlik(message)
    elif choice == '↖️ Ortga':
        await asosiymenu(message)

ichimliklar = {
    'Montella 0.33': 15000,
    'Qora choy': 8000,
    "Ko'k choy": 10000,
    'Qora Limonli choy': 12000,
    "Ko'k limonli choy": 13000,
    "Espresso": 5000
}

async def ichimlik(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "ichimlik"
    button = [
        [types.KeyboardButton(text="↪️ Ortga"), types.KeyboardButton(text="📥 Savat")],
        [types.KeyboardButton(text='Montella 0.33'), types.KeyboardButton(text='Qora choy')],
        [types.KeyboardButton(text="Ko'k choy"), types.KeyboardButton(text='Qora Limonli choy')],
        [types.KeyboardButton(text="Ko'k limonli choy"), types.KeyboardButton(text="Espresso")],
        [types.KeyboardButton(text="Do'stlar 1x"), types.KeyboardButton(text="Do'stlar 1x, achchiq")],
        [types.KeyboardButton(text="Qiyqiriq set"), types.KeyboardButton(text="Longer rings set")],
        [types.KeyboardButton(text="Lester set"), types.KeyboardButton(text="Big set")],
        [types.KeyboardButton(text="Snek set"), types.KeyboardButton(text="Do'stlar 2x")],
        [types.KeyboardButton(text="Do'stlar 2x, achchiq"), types.KeyboardButton(text="4 Friends Hot-dog")],
        [types.KeyboardButton(text="4 Friends Klassik burger"), types.KeyboardButton(text="4 Friends Longer chiz")],
        [types.KeyboardButton(text="4 Friends Lester chiz"), types.KeyboardButton(text="Do'stlar 4x")],
        [types.KeyboardButton(text="Do'stlar 4x, achchiq")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("Nimadan boshlaymiz?", reply_markup=keyboard)


async def ichimlik_zakaz(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "ichimlik_zakaz"
    item = message.text
    price = ichimliklar[item]
    name = item
    buttons = [
        [types.KeyboardButton(text="↖️ Ortga"), types.KeyboardButton(text="📥Savatga qo'shish✅")],
    ]
    keyboards = types.ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
    button = [
        [types.InlineKeyboardButton(text="-", callback_data=f"minus_{item}"),
         types.InlineKeyboardButton(text="1", callback_data=f"miqdor_{item}"),
         types.InlineKeyboardButton(text="+", callback_data=f"plus_{item}"),],
        [types.InlineKeyboardButton(text="📥Savatga qo'shish✅", callback_data=f"add_{item}"), ],
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)

    # Rasm yuborish va matn bilan havolani qo'shish
    file_path_c = "images/1+1.jpg"
    caption_text_c = (

        f"Nomi: {name}"
        f"Narxi: {price}so'm"
    )
    # Rasm yuborish va matn bilan havolani qo'shish 2
    file_path_s = "images/cezar.jpg"
    caption_text_s = (
        f"Nomi: {name}"
        f"Narxi: {price}so'm"
    )
    file_path_a = "images/klassic.jpg"
    caption_text_a = (

        f"Nomi: {name}"
        f"Narxi: {price}so'm"
    )
    file_path_z = "images/school.jpg"
    caption_text_z = (

        f"Nomi: {name}"
        f"Narxi: {price}so'm"
    )
    file_path_x = "images/yangi set.jpg"
    caption_text_x = (

        f"Nomi: {name}"
        f"Narxi: {price}so'm"
    )
    file_path = "images/komboset.jpg"
    caption_text = (

        f"Nomi: {name}"
        f"Narxi: {price}so'm"
    )


    await message.answer("Miqdorni belgilang",reply_markup=keyboards)
    if message.text == 'Montella 0.33':
        await message.reply_photo(
            caption=caption_text,
            photo=types.FSInputFile(path=file_path),
            parse_mode="Markdown",  # Markdown formatida matnni formatlash
            reply_markup=keyboard  # Tugmalarni rasm bilan yuborish
        )
    elif message.text == 'Qora choy':
        await message.reply_photo(
            caption=caption_text_c,
            photo=types.FSInputFile(path=file_path_c),
            parse_mode="Markdown",  # Markdown formatida matnni formatlash
            reply_markup=keyboard  # Tugmalarni rasm bilan yuborish
        )
    elif message.text == "Ko'k choy":
        await message.reply_photo(
            caption=caption_text_a,
            photo=types.FSInputFile(path=file_path_a),
            parse_mode="Markdown",  # Markdown formatida matnni formatlash
            reply_markup=keyboard  # Tugmalarni rasm bilan yuborish
        )
    elif message.text == 'Qora Limonli choy':
        await message.reply_photo(
            caption=caption_text_s,
            photo=types.FSInputFile(path=file_path_s),
            parse_mode="Markdown",  # Markdown formatida matnni formatlash
            reply_markup=keyboard  # Tugmalarni rasm bilan yuborish
        )
    elif message.text == "Ko'k limonli choy":
        await message.reply_photo(
            caption=caption_text_x,
            photo=types.FSInputFile(path=file_path_x),
            parse_mode="Markdown",  # Markdown formatida matnni formatlash
            reply_markup=keyboard  # Tugmalarni rasm bilan yuborish
        )
    elif message.text == "Espresso":
        await message.reply_photo(
            caption=caption_text_z,
            photo=types.FSInputFile(path=file_path_z),
            parse_mode="Markdown",  # Markdown formatida matnni formatlash
            reply_markup=keyboard  # Tugmalarni rasm bilan yuborish
        )

    else:
        await message.answer("Hi")

async def taomlar(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "taomlar"
    button = [
        [types.KeyboardButton(text="↪️ Ortga"), types.KeyboardButton(text="📥 Savat")],
        [types.KeyboardButton(text="Kombo set"), types.KeyboardButton(text="1+1 Barbekyu burger")],
        [types.KeyboardButton(text="1+1 Sezar burger"), types.KeyboardButton(text="Yangi set")],
        [types.KeyboardButton(text="Klassik set"), types.KeyboardButton(text="Skulll set")],
        [types.KeyboardButton(text="Do'stlar 1x"), types.KeyboardButton(text="Do'stlar 1x, achchiq")],
        [types.KeyboardButton(text="Qiyqiriq set"), types.KeyboardButton(text="Longer rings set")],
        [types.KeyboardButton(text="Lester set"), types.KeyboardButton(text="Big set")],
        [types.KeyboardButton(text="Snek set"), types.KeyboardButton(text="Do'stlar 2x")],
        [types.KeyboardButton(text="Do'stlar 2x, achchiq"), types.KeyboardButton(text="4 Friends Hot-dog")],
        [types.KeyboardButton(text="4 Friends Klassik burger"), types.KeyboardButton(text="4 Friends Longer chiz")],
        [types.KeyboardButton(text="4 Friends Lester chiz"), types.KeyboardButton(text="Do'stlar 4x")],
        [types.KeyboardButton(text="Do'stlar 4x, achchiq")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("Nimadan boshlaymiz?", reply_markup=keyboard)





async def savat(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["holat"] = "savat"
    item = message.text
    price = 22000
    name = item
    buttons = [
        [types.KeyboardButton(text="↖️ Ortga"), types.KeyboardButton(text="📥Savatga qo'shish✅")],
    ]
    keyboards = types.ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
    button = [
        [types.InlineKeyboardButton(text="-", callback_data=f"minus_{item}"),
         types.InlineKeyboardButton(text="1", callback_data=f"miqdor_{item}"),
         types.InlineKeyboardButton(text="+", callback_data=f"plus_{item}"),],
        [types.InlineKeyboardButton(text="📥Savatga qo'shish✅", callback_data=f"add_{item}"), ],
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)

    # Rasm yuborish va matn bilan havolani qo'shish
    file_path_c = "images/1+1.jpg"
    caption_text_c = (

        f"Nomi: {name}"
        f"Narxi: {price}so'm"
    )
    # Rasm yuborish va matn bilan havolani qo'shish 2
    file_path_s = "images/cezar.jpg"
    caption_text_s = (
        f"Nomi: {name}"
        f"Narxi: {price}so'm"
    )
    file_path_a = "images/klassic.jpg"
    caption_text_a = (

        f"Nomi: {name}"
        f"Narxi: {price}so'm"
    )
    file_path_z = "images/school.jpg"
    caption_text_z = (

        f"Nomi: {name}"
        f"Narxi: {price}so'm"
    )
    file_path_x = "images/yangi set.jpg"
    caption_text_x = (

        f"Nomi: {name}"
        f"Narxi: {price}so'm"
    )
    file_path = "images/komboset.jpg"
    caption_text = (

        f"Nomi: {name}"
        f"Narxi: {price}so'm"
    )


    await message.answer("Miqdorni belgilang",reply_markup=keyboards)
    if message.text == 'Kombo set':
        await message.reply_photo(
            caption=caption_text,
            photo=types.FSInputFile(path=file_path),
            parse_mode="Markdown",  # Markdown formatida matnni formatlash
            reply_markup=keyboard  # Tugmalarni rasm bilan yuborish
        )
    elif message.text == '1+1 Barbekyu burger':
        await message.reply_photo(
            caption=caption_text_c,
            photo=types.FSInputFile(path=file_path_c),
            parse_mode="Markdown",  # Markdown formatida matnni formatlash
            reply_markup=keyboard  # Tugmalarni rasm bilan yuborish
        )
    elif message.text == '1+1 Sezar burger':
        await message.reply_photo(
            caption=caption_text_a,
            photo=types.FSInputFile(path=file_path_a),
            parse_mode="Markdown",  # Markdown formatida matnni formatlash
            reply_markup=keyboard  # Tugmalarni rasm bilan yuborish
        )
    elif message.text == 'Klassik set':
        await message.reply_photo(
            caption=caption_text_s,
            photo=types.FSInputFile(path=file_path_s),
            parse_mode="Markdown",  # Markdown formatida matnni formatlash
            reply_markup=keyboard  # Tugmalarni rasm bilan yuborish
        )
    elif message.text == 'Skulll set':
        await message.reply_photo(
            caption=caption_text_x,
            photo=types.FSInputFile(path=file_path_x),
            parse_mode="Markdown",  # Markdown formatida matnni formatlash
            reply_markup=keyboard  # Tugmalarni rasm bilan yuborish
        )
    elif message.text == 'Yangi set':
        await message.reply_photo(
            caption=caption_text_z,
            photo=types.FSInputFile(path=file_path_z),
            parse_mode="Markdown",  # Markdown formatida matnni formatlash
            reply_markup=keyboard  # Tugmalarni rasm bilan yuborish
        )

    else:
        await message.answer("Hi")

count = 1
@dp.callback_query(lambda c: c.data.startswith(('plus', 'minus', 'add')))
async def checkcallback(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    price = 22000
    name = "Fri kartoshkasiCoca-cola 0.5\n"
    command, item = callback.data.split('_')
    global count

    if command == 'plus':
        count += 1
    elif command == 'minus':
        if count > 1:
            count -= 1
    elif command == 'add':
        if 'basket' not in user_data[user_id]:
            user_data[user_id]['basket'] = {item: count}
        else:
            if item in user_data[user_id]['basket']:
                user_data[user_id]['basket'][item] += count
            else:
                user_data[user_id]['basket'][item] = count

        count = 1  # Reset count after adding item to the basket
        await callback.message.answer(f"Mahsulot {name} savatga muvaffaqiyatli qo'shildi ✅\n"
                                    "Davom etamizmi?")

    print(f"Count:{count}")
    button = [
        [types.InlineKeyboardButton(text=f"-", callback_data=f"minus_{item}"),
         types.InlineKeyboardButton(text=f"{count}", callback_data=f"miqdor_{item}"),
         types.InlineKeyboardButton(text=f"+", callback_data=f"plus_{item}"), ],
        [types.InlineKeyboardButton(text=f"📥Savatga qo'shish✅", callback_data=f"add_{item}"), ],
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    price = price * count  # Update the price based on count
    try:
        print(user_data)
        await callback.message.edit_caption(
            caption="Kombo set\n\n"
                    f"Nomi: {name}\n"
                    f"Narxi: {price} so'm",
            reply_markup=keyboard
        )
    except aiogram.exceptions.TelegramBadRequest as e:
        if "message is not modified" in str(e):
            print("Xabar o'zgarmaganligi sababli yangilash o'tkazib yuborildi.")
        else:
            print(f"Xato yuz berdi: {e}")



async def show_cart(message: types.Message):
    user_id = message.from_user.id
    if user_id not in user_data or not user_data[user_id].get("basket"):
        button = [
            [types.KeyboardButton(text="⬅️ Ortga"), types.KeyboardButton(text="Оформить заказ ✅")],
            [types.KeyboardButton(text="🔄 Очистить")],
        ]
        keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
        await message.answer("🛒 Sizning savatingiz bo'sh", reply_markup=keyboard )
        return
    cart_items = user_data[user_id]["basket"]
    total_price = 0
    cart_text = "🛒 Sizning savatingiz:\n\n"
    for idx, (item_name, item_count) in enumerate(cart_items.items(), start=1):
        item_price = 22000  # This is the price for each item
        total_price += item_price * item_count  # Multiply price by the count
        cart_text += f"{idx}. {item_name} x{item_count} — {item_price * item_count} so'm\n"


    cart_text += f"\n💵 Jami: {total_price} so'm"
    button = [
        [types.KeyboardButton(text="⬅️ Ortga"), types.KeyboardButton(text="Оформить заказ ✅")],
        [types.KeyboardButton(text="🔄 Очистить")],
    ]
    button_in = [
        [types.InlineKeyboardButton(text="+", callback_data="plus")],
    ]
    keyboards = types.InlineKeyboardMarkup(inline_keyboard=button_in, resize_keyboard=True)
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer(f'"❌ Наименование" - удалить одну позицию\n\n'
                         f'" - и +" - уменьшить или увеличить количество продукта\n\n'
                         f'"🔄 Очистить" - полная очистка корзины',reply_markup=keyboard)
    await message.answer(cart_text,reply_markup=keyboards)
    print(3, user_data)





async def main():
    print('The bot is running...')
    await dp.start_polling(bot)


asyncio.run(main())


