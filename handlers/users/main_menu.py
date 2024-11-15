from aiogram import types
from loader import dp

@dp.message_handler(text = "☎️ Biz bilan aloqa")
async def contact(message: types.Message):
    text = """Agar sizda Savollar/Shikoyatlar/Takliflar bo'lsa bizga 
yozishingiz mumkin: @Street77tech_bot

☎️ Telefon raqam: 71-200-73-73 / 71 200-86-86"""
    await message.answer(text)
