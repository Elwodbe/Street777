from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

menu_kb = ReplyKeyboardMarkup(
            [
                [KeyboardButton["🍽Menyu"],
                 [KeyboardButton(text='📖Buyurtmalar tarixi')],[KeyboardButton(text='✍️Fikr bildirish')],
                 [KeyboardButton(text='ℹ️Malumot')] , [KeyboardButton(text = 'Biz bilan aloqa ☎️')] ,
                 [KeyboardButton(text = '⚙️Sozlamalar')]]
            ]
        )




# menu_kb = ReplyKeyboardMarkup(
#     keyboard=[
#         [KeyboardButton(text='Меню🍽')],
#         [KeyboardButton(text='Мои заказы📖')] , [KeyboardButton(text = 'Оставить отзыв✍️')] ,
#         [KeyboardButton(text='Информация ℹ️')] , [KeyboardButton(text = 'Обратная связь ℹ️')] ,
#         [KeyboardButton(text = 'Настройка⚙️')]
#     ],
#     resize_keyboard=True
# )
