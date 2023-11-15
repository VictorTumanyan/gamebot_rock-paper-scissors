import random

from lexicon.lexicon_ru import LEXICON_RU

def get_bot_choice() -> str:
    return random.choice(['rock', 'paper','scissors'])

def _normalize_users_answer(answer: str) -> str:
    for key in LEXICON_RU:
        if LEXICON_RU[key] == answer:
            break
    return key

def get_winner(user_choice: str, bots_choice: str) -> str:
    user_choice = _normalize_users_answer(user_choice)

    rules = {
        'rock': 'scissors',
        'scissors': 'paper',
        'paper': 'rock'
    }

    if user_choice == bots_choice:
        return 'nobody_won'
    if rules[user_choice] == bots_choice:
        return 'user_won'
    return 'bot_won'