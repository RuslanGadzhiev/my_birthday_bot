import random
import time

from aiogram import Router
from aiogram.filters import Command, CommandStart, Text
from aiogram.types import Message, FSInputFile
from lexicon.lexicon import LEXICON_RU, LEXICON_NAMES_RU
from config_data.config import load_names
from keyboards.keyboards import game_kb, start_kb, vanga_kb, luser_kb

from services.services import get_bot_choice, get_winner


# Инициализируем роутер уровня модуля
router: Router = Router()


# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'], reply_markup=start_kb)


# Этот хэндлер срабатывает на команду /help
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'], reply_markup=start_kb)


# Этот хэндлер срабатывает на кнопку - "Информация"
@router.message(Text(text=LEXICON_RU['info']))
async def process_info_answer(message: Message):
    await message.answer(text=LEXICON_RU['address'], reply_markup=start_kb)


# Этот хэндлер срабатывает на согласие пользователя играть в игру
@router.message(Text(text=LEXICON_RU['knb']))
async def process_knb_answer(message: Message):
    await message.answer(text=LEXICON_RU['yes'], reply_markup=game_kb)


# Этот хэндлер срабатывает на любую из игровых кнопок
@router.message(Text(text=[LEXICON_RU['rock'],
                           LEXICON_RU['paper'],
                           LEXICON_RU['scissors']]))
async def process_game_button(message: Message):
    bot_choice = get_bot_choice()
    await message.answer(text=f'{LEXICON_RU["bot_choice"]} '
                              f'- {LEXICON_RU[bot_choice]}')
    winner = get_winner(message.text, bot_choice)
    await message.answer(text=LEXICON_RU[winner], reply_markup=start_kb)


# Этот хэндлер срабатывает на кнопку - "Угадай-ка"
@router.message(Text(text=[LEXICON_RU['vanga']]))
async def process_vanga_button(message: Message):
    await message.answer(text=LEXICON_RU['want'], reply_markup=vanga_kb)


# Этот хэндлер срабатывает на кнопку - "Угадай-ка" - "Хочууу!))"
@router.message(Text(text=[LEXICON_RU['i_want']]))
async def process_i_want_button(message: Message):
    name_key = load_names()
    # print(name_key)
    # print(name_key[str(message.from_user.id)])
    await message.answer(text=LEXICON_NAMES_RU[name_key[str(message.from_user.id)]], reply_markup=start_kb)

# Этот хэндлер срабатывает на кнопку - "Угадай-ка" - "Ну на хер!"
@router.message(Text(text=[LEXICON_RU['not_want']]))
async def process_i_want_button(message: Message):
    nu_nah = FSInputFile('gifs/nu_naher.gif')
    await message.answer(text=LEXICON_RU['nu_nah'], reply_markup=start_kb)


# Этот хэндлер срабатывает на кнопку - "Лузер"
@router.message(Text(text=[LEXICON_RU['luser']]))
async def process_vanga_button(message: Message):
    await message.answer(text=LEXICON_RU['luser_go'], reply_markup=luser_kb)


# Этот хэндлер срабатывает на кнопку "Погнали"
@router.message(Text(text=[LEXICON_RU['go']]))
async def process_game_button(message: Message):
    losers: list[str] = ['Рус', 'Эльдос', 'Леха', 'Вадос', 'Олег', 'Макс', 'Андрюха Х', 'Андрюха Ч']
    while len(losers) > 1:
        not_lose = random.choice(losers)
        losers.pop(losers.index(not_lose))
        time.sleep(1)
        await message.answer(text=f'{not_lose} - не лузер)')
    else:
        await message.answer(text=f'Поздравляю - {losers.pop()} - Ты Лошара!!! 🚽', reply_markup=start_kb)
