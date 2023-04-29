from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

menu = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton("💠 Normal Roulette", callback_data="roulette"),
    InlineKeyboardButton("🔥 Tactical Roulette", callback_data="tactical"),
    InlineKeyboardButton("ℹ️ Info", callback_data="info")
)

tactical = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton('🔥 Tactic: All lost + 1$', callback_data='tactic_1'),
    InlineKeyboardButton('◀️ Back', callback_data='menu')
)

info = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton('◀️ Back', callback_data='menu')
)

bets = InlineKeyboardMarkup(row_width=3).add(
    InlineKeyboardButton('🟢 0', callback_data='0')
).add(
    InlineKeyboardButton('🔴 1', callback_data='1'),
    InlineKeyboardButton('⚫️ 2', callback_data='2'),
    InlineKeyboardButton('🔴 3', callback_data='3'),
    InlineKeyboardButton('⚫️ 4', callback_data='4'),
    InlineKeyboardButton('🔴 5', callback_data='5'),
    InlineKeyboardButton('⚫️ 6', callback_data='6'),
    InlineKeyboardButton('🔴 7', callback_data='7'),
    InlineKeyboardButton('⚫️ 8', callback_data='8'),
    InlineKeyboardButton('🔴 9', callback_data='9'),
    InlineKeyboardButton('⚫️ 10', callback_data='10'),
    InlineKeyboardButton('⚫️ 11', callback_data='11'),
    InlineKeyboardButton('🔴 12', callback_data='12'),
    InlineKeyboardButton('⚫️ 13', callback_data='13'),
    InlineKeyboardButton('🔴 14', callback_data='14'),
    InlineKeyboardButton('⚫️ 15', callback_data='15'),
    InlineKeyboardButton('🔴 16', callback_data='16'),
    InlineKeyboardButton('⚫️ 17', callback_data='17'),
    InlineKeyboardButton('🔴 18', callback_data='18'),
    InlineKeyboardButton('🔴 19', callback_data='19'),
    InlineKeyboardButton('⚫️ 20', callback_data='20'),
    InlineKeyboardButton('🔴 21', callback_data='21'),
    InlineKeyboardButton('⚫️ 22', callback_data='22'),
    InlineKeyboardButton('🔴 23', callback_data='23'),
    InlineKeyboardButton('⚫️ 24', callback_data='24'),
    InlineKeyboardButton('🔴 25', callback_data='25'),
    InlineKeyboardButton('⚫️ 26', callback_data='26'),
    InlineKeyboardButton('🔴 27', callback_data='27'),
    InlineKeyboardButton('⚫️ 28', callback_data='28'),
    InlineKeyboardButton('⚫️ 29', callback_data='29'),
    InlineKeyboardButton('🔴 30', callback_data='30'),
    InlineKeyboardButton('⚫️ 31', callback_data='31'),
    InlineKeyboardButton('🔴 32', callback_data='32'),
    InlineKeyboardButton('⚫️ 33', callback_data='33'),
    InlineKeyboardButton('🔴 34', callback_data='34'),
    InlineKeyboardButton('⚫️ 35', callback_data='35'),
    InlineKeyboardButton('🔴 36', callback_data='36'),
    InlineKeyboardButton('🔸 2~1', callback_data='2_1'),
    InlineKeyboardButton('🔸 2~1', callback_data='2_2'),
    InlineKeyboardButton('🔸 2~1', callback_data='2_3'),
    InlineKeyboardButton('🔹 1-12', callback_data='1_12'),
    InlineKeyboardButton('🔹 13-24', callback_data='13_24'),
    InlineKeyboardButton('🔹 25-36', callback_data='25_36')
).add(
    InlineKeyboardButton('🔸 1-18', callback_data='1_18'),
    InlineKeyboardButton('🔸 19-36', callback_data='19_36')
).add(
    InlineKeyboardButton('🔹 Even', callback_data='even'),
    InlineKeyboardButton('🔹 Odd', callback_data='odd')
).add(
    InlineKeyboardButton('🔴 Red', callback_data='red'),
    InlineKeyboardButton('⚫️ Black', callback_data='black')
).add(
    InlineKeyboardButton('◀️ Back', callback_data='normal')
)

to_normal = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton('◀️ Back', callback_data='roulette')
)
