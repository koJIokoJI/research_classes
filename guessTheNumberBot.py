from random import randint
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message


# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
BOT_TOKEN = '7661070271:AAF_ZVAmE28l0CNAHOyawMEwkYeSLE54M5A'

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

user = {"in_game": False,
        "secret_number": None,
        "attempts": None,
        "total_games": 0,
        "wins": 0}


def get_random_number() -> int:
    return randint(1, 100)


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands='start'))
async def process_start_command(message: Message):
    await message.answer(f"привет, {message.chat.first_name}\n\nсыграем в игру 'угадай число'?\n\nправила игры: /help")


@dp.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer("я загадываю число от 1 до 100, вы угадываете\n\nу вас есть 5 попыток\n\nсогласны?")


@dp.message(Command(commands='stat'))
async def process_stat_command(message: Message):
    await message.answer(f"всего игр сыграно: {user['total_games']}\n\nигр выйграно: {user['wins']}")


@dp.message(Command(commands='cancel'))
async def process_cancel_command(message: Message):
    if user['in_game']:
        user['in_game'] = False
        await message.answer("вы вышли из игры. если хотите снова: \"игра\"")
    else:
        await message.answer("мы и так не играем. хочешь? \"игра\"")


@dp.message(F.text.lower().in_(['да', 'давай', 'сыграем', 'игра', 'играть', 'хочу', 'хочу сыграть']))
async def process_positive_answer(message: Message):
    if not user['in_game']:
        user['in_game'] = True
        user['secret_number'] = get_random_number()
        user['attempts'] = 5
        await message.answer(f"вы в игре\n\nчисло загадано")
    else:
        await message.answer("мы уже в игре.\n\nчтобы выйти: /cancel")
      
        
@dp.message(F.text.lower().in_(['нет', 'не', 'не хочу', 'не буду', 'неа']))
async def process_negative_answer(message: Message):
    if not user['in_game']:
        await message.answer("жаль\n\nчтобы сыграть: \"игра\"")
    else:
        await message.answer("мы уже в игре\n\nвводите числа\nчтобы выйти из игры: /cancel")
        

@dp.message(lambda x: x.text and x.text.isdigit() and 1 <= int(x.text) <= 100)
async def process_numbers_answer(message: Message):
    gn = user['secret_number']
    guess = int(message.text)
    if user['in_game']:
        if user['attempts'] > 0:
            if guess > gn:
                user['attempts'] -= 1
                await message.answer(f"загаданное число меньше\n\nколичество попыток: {user['attempts']}")
            elif guess < gn:
                user['attempts'] -= 1
                await message.answer(f"загаданное число больше\n\nколичество попыток: {user['attempts']}")
            else:
                user['secret_number'] = None
                user['in_game'] = False
                user['wins'] += 1
                user['total_games'] += 1
                await message.answer("вы победили")
        else:
            user['in_game'] = False
            user['total_games'] += 1
            await message.answer(f"вы проиграли\n\nзагаданное число: {user['secret_number']}")
    else:
        await message.answer("начните игру")
        
        
@dp.message()
async def process_other_answer(message: Message):
    if user['in_game']:
        await message.answer("мы в игре")
    else:
        await message.answer("я игрок")


if __name__ == '__main__':
    dp.run_polling(bot)