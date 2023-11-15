from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart

from keyboards.keyboards import game_kb, yes_no_kb
from lexicon.lexicon_ru import LEXICON_RU
from services.services import get_bot_choice, get_winner

router = Router()

# Start button
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text=LEXICON_RU['/start'],
        reply_markup=yes_no_kb
    )

# Help button
@router.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(
        text=LEXICON_RU['/help'],
        reply_markup=yes_no_kb
    )

# Wanna play
@router.message(F.text == LEXICON_RU['yes_button'])
async def process_yes_answer(message: Message):
    await message.answer(
        text=LEXICON_RU['yes'],
        reply_markup=game_kb
    )

# Don't want to play
@router.message(F.text == LEXICON_RU['no_button'])
async def process_no_answer(message: Message):
    await message.answer(
        text=LEXICON_RU['no']
    )

# Made a choice
@router.message(F.text.in_([LEXICON_RU['rock'],
                           LEXICON_RU['paper'],
                           LEXICON_RU['scissors']]))
async def process_game(message: Message):
    bot_choice = get_bot_choice()
    await message.answer(text=f'{LEXICON_RU["bot_choice"]} - '
                         f'{bot_choice}')

    winner = get_winner(message.text, bot_choice)
    await message.answer(
        text=f'{LEXICON_RU[winner]}',
        reply_markup=yes_no_kb
    )