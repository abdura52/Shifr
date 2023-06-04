from aiogram import Bot, Dispatcher, executor, types
from time import sleep
from random import shuffle


def DECODE(text: str) -> str:
    with open("l.txt", "r") as f:
        l = f.read()

    with open("keys.py", "r") as f:
        KEY = f.read()
    KEY = eval(KEY[54:])
        
    new = str()
    for i in text:
        for k,v in KEY.items():
            if v == i:
                new += k
                break

    return new

def ENCODE(text: str) -> str:
    with open("l.txt", "r") as f:
        l = f.read()

    with open("keys.py", "r") as f:
        KEY = f.read()
    KEY = eval(KEY[54:])
    
    new = str()
    i = 0
    while i<len(text)-1:
        k = text[i] + text[i+1]
        new += KEY[k]
        i += 2

    return new

API_TOKEN = "5913420263:AAE21ER0dw1xyMOxPJEkf_78540KWu850go"
ADMIN = 6095810791

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['key'])
async def generate_new(message: types.Message):
    if message.from_user.id == ADMIN:
        with open("l.txt", "r") as f:
            key = f.read()
        key = [i for i in key]
        shuffle(key)
        key = "".join(key)

        with open("l.txt", "w") as f:
            f.write(key)
        await message.reply("Yangi key generatsiya qilindi!")

@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    await message.answer("*Salom, shirf botga xush kelibsiz\nEslatma habarlar 3 sekundda avto o'chirib yuboriladi!*", parse_mode='markdown')

@dp.message_handler()
async def translate(message: types.Message):
    try:
        text = DECODE(message.text)
        await message.answer(text=text)
        sleep(2)
        await bot.delete_message(message.from_user.id, message.message_id)
        await bot.delete_message(message.from_user.id, message.message_id + 1)
    except KeyError:
        await message.reply("*Ro'yhatda yo'q belgilardan foydalandingiz!*", parse_mode='markdown')
        sleep(1.5)
        await bot.delete_message(message.from_user.id, message.message_id)
    except:
        text = ENCODE(message.text)
        await message.answer(text=text)
        sleep(2)
        await bot.delete_message(message.from_user.id, message.message_id)
        await bot.delete_message(message.from_user.id, message.message_id + 1)


        

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)