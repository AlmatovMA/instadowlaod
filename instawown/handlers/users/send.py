from aiogram import types
from loader import dp, Bot
from aiogram.dispatcher.filters import Text
from insta import instadown
@dp.message_handler(Text(startswith="https://www.instagram.com/"))
async def send_media(message:types.Message):
    link = message.text
    data = instadown(link=link)
    if data == 'формат не опознан':
        await message.answer('bu URL manzil orkali hech narsa topa olmadik')
    else:
        if data['type']=='image':
            await message.answer_photo(photo=data['media'])
        elif data['type']=='story-image':
            await message.answer_photo(photo=data['media'])
        elif data['type']=='video':
            await message.answer_video(video=data['media'])
        elif data['type']=='story-video':
            await message.answer_video(video=data['media'])
        elif data['type']=='carousel':
            for i in data['media']:
             await message.answer_document(document=i)
        else:
            await message.answer('bu URL manzil orkali hech narsa topa olmadik')
