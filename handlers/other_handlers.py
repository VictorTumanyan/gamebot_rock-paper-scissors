from aiogram import Router
from aiogram.types import Message
from lexicon.lexicon_ru import LEXICON_RU

router = Router()

# Handler for all messages, which not included in previous handlers
@router.message()
async def send_answer(message: Message):
    await message.answer(text=LEXICON_RU['other_answer'])