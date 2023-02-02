from aiogram import types
from misc import dp, bot
from .sqlit import reg_user
import asyncio
import random

reg_user(1,1)
content = -1001852312157

@dp.callback_query_handler(lambda call: True, state = '*')
async def answer_push_inline_button(call):
    if call.data == 'dalee1':
        await bot.answer_callback_query(call.id)
        await bot.copy_message(chat_id=call.message.chat.id, from_chat_id=content, message_id=13)
        await asyncio.sleep(420) # 7 минут
        await bot.copy_message(chat_id=call.message.chat.id, from_chat_id=content, message_id=17)
        await asyncio.sleep(86400)  #24 часа
        await bot.copy_message(chat_id=call.message.chat.id, from_chat_id=content, message_id=20)
        await asyncio.sleep(86400)  # 24 часа
        await bot.copy_message(chat_id=call.message.chat.id, from_chat_id=content, message_id=22)
        await asyncio.sleep(86400)  # 24 часа
        await bot.copy_message(chat_id=call.message.chat.id, from_chat_id=content, message_id=24)
        await asyncio.sleep(86400)  # 24 часа
        await bot.copy_message(chat_id=call.message.chat.id, from_chat_id=content, message_id=26)