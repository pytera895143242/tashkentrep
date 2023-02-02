from aiogram import types
from misc import dp, bot
from .sqlit import reg_user

content = -1001852312157

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    reg_user(message.chat.id,'1')
    markup = types.InlineKeyboardMarkup()
    bat_a = types.InlineKeyboardButton(text='Далее', callback_data='dalee1')
    markup.add(bat_a)
    await bot.copy_message(chat_id=message.chat.id,from_chat_id=content,message_id=11,reply_markup=markup)