from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from lexicon.lexicon_ru import LEXICON_RU

# Creating agree/disagree keyboard with builder
button_yes = KeyboardButton(text=LEXICON_RU['yes_button'])
button_no = KeyboardButton(text=LEXICON_RU['no_button'])

yes_no_kb_builder = ReplyKeyboardBuilder()

yes_no_kb_builder.row(button_yes, button_no, width=2)

yes_no_kb: ReplyKeyboardBuilder = yes_no_kb_builder.as_markup(
    one_time_keyboard=True,
    resize_keyboard=True
)

# Creating choice keyboard without builder
button_rock = KeyboardButton(text=LEXICON_RU['rock'])
button_paper = KeyboardButton(text=LEXICON_RU['paper'])
button_scissors = KeyboardButton(text=LEXICON_RU['scissors'])

game_kb = ReplyKeyboardMarkup(
    keyboard=[
        [button_rock],
        [button_paper],
        [button_scissors]
        ],
    resize_keyboard=True
)