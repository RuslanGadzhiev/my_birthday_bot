from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon.lexicon import LEXICON_RU

# ------- Создаем клавиатуру через ReplyKeyboardBuilder -------

# Создаем кнопки с ответами согласия и отказа
button_info: KeyboardButton = KeyboardButton(text=LEXICON_RU['info'])
button_games: KeyboardButton = KeyboardButton(text=LEXICON_RU['knb'])
button_vanga: KeyboardButton = KeyboardButton(text=LEXICON_RU['vanga'])
button_luser: KeyboardButton = KeyboardButton(text=LEXICON_RU['luser'])

# Инициализируем билдер для клавиатуры с кнопками "Информация", "Игры" и "Угадай-ка"
start_kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

# Добавляем кнопки в билдер с параметром width=2
start_kb_builder.row(button_info, button_games, button_vanga, button_luser, width=4)

# Создаем клавиатуру с кнопками "Информация", "Игры" и "Угадай-ка"
start_kb = start_kb_builder.as_markup(one_time_keyboard=True, resize_keyboard=True)

# ------- Создаем игровую клавиатуру без использования билдера -------

# Создаем кнопки игровой клавиатуры
button_1: KeyboardButton = KeyboardButton(text=LEXICON_RU['rock'])
button_2: KeyboardButton = KeyboardButton(text=LEXICON_RU['scissors'])
button_3: KeyboardButton = KeyboardButton(text=LEXICON_RU['paper'])

# Создаем игровую клавиатуру с кнопками "Камень 🗿",
# "Ножницы ✂" и "Бумага 📜" как список списков
game_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                                    keyboard=[[button_1],
                                              [button_2],
                                              [button_3]],
                                    resize_keyboard=True)

# Создаем кнопки игровой клавиатуры к Угадай-ке
vanga_button_1: KeyboardButton = KeyboardButton(text=LEXICON_RU['i_want'])
vanga_button_2: KeyboardButton = KeyboardButton(text=LEXICON_RU['not_want'])


# Создаем игровую клавиатуру с кнопками "Хочу",
# "Ну на хер" как список списков
vanga_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                                    keyboard=[[vanga_button_1],
                                              [vanga_button_2]],
                                    resize_keyboard=True)

# Создаем кнопки игровой клавиатуры к Лузер
luser_1: KeyboardButton = KeyboardButton(text=LEXICON_RU['go'])



# Создаем игровую клавиатуру с кнопкой "Погнали"
# "Ну на хер" как список списков
luser_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                                    keyboard=[[luser_1]],
                                    resize_keyboard=True)