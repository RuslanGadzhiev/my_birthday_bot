from dataclasses import dataclass
from typing import Dict, Any

from environs import Env


@dataclass
class NamesConfig:
    rus: str  # Руслан
    eldar: str  # Эльдар
    lexa: str  # Леха Вол
    andryuha_x: str  # Хирный
    maxim: str  # Макс
    oleg: str  # Хирный
    andryuha_che: str  # Хирный
    vados: str  # Вадос


@dataclass
class TgBot:
    token: str  # Токен для доступа к телеграм-боту


@dataclass
class Config:
    tg_bot: TgBot
    # names: NamesConfig


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(tg_bot=TgBot(token=env('BOT_TOKEN')))


def load_names(path: str | None = None) -> dict[str: str]:
    env = Env()
    env.read_env(path)
    names = NamesConfig(rus=env('RUS'),
                        eldar=env('ELDAR'),
                        lexa=env('LEXA'),
                        andryuha_x=env('ANDRYUHA_X'),
                        maxim=env('MAX'),
                        oleg=env('OLEG'),
                        andryuha_che=env('ANDRYUHA_CHE'),
                        vados=env('VADOS'))

    names_dict: dict[str: str] = {
        names.rus: 'rus',
        names.eldar: 'eldar',
        names.lexa: 'lexa',
        names.andryuha_x: 'andryuha_x',
        names.maxim: 'maxim',
        names.oleg: 'oleg',
        names.andryuha_che: 'andryuha_che',
        names.vados: 'vados'
    }
    return names_dict

# Для проверки загрузки данных из ДБ
# # Создаем экземпляр класса Env
# env: Env = Env()
#
# # Добавляем в переменные окружения данные, прочитанные из файла .env
# env.read_env()
#
# # Создаем экземпляр класса Config и наполняем его данными из переменных окружения
# config = Config(tg_bot=TgBot(token=env('BOT_TOKEN')),
#                 names=NamesConfig(rus=env('RUS'),
#                                   eldar=env('ELDAR'),
#                                   lexa=env('LEXA'),
#                                   andryuha_x=env('ANDRYUHA_X'),
#                                   maxim=env('MAX'),
#                                   oleg=env('OLEG'),
#                                   andryuha_che=env('ANDRYUHA_CHE'),
#                                   vados=env('VADOS')))
#
# # Выводим значения полей экземпляра класса Config на печать,
# # чтобы убедиться, что все данные, получаемые из переменных окружения, доступны
# print('BOT_TOKEN:', config.tg_bot.token)
# print()
# print('RUS:', config.names.rus)
# print('ELDAR:', config.names.eldar)
# print('LEXA:', config.names.lexa)
# print('ANDRYUHA_X:', config.names.andryuha_x)
# print('MAX:', config.names.maxim)
# print('OLEG:', config.names.oleg)
# print('ANDRYUHA_CHE:', config.names.andryuha_che)
# print('VADOS:', config.names.vados)
