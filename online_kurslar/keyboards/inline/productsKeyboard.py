from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

#1-usul
from keyboards.inline.callback_data import course_callback, book_callback

categoryMenu=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="💻 Kurslar", callback_data="courses"),
            InlineKeyboardButton(text="📚 Kitoblar", callback_data="books"),
        ],
        [
            InlineKeyboardButton(text="🔗 Moxirdev sahifasiga o'tish", url="https://mohirdev.uz/courses/telegram")
        ],
        [
           InlineKeyboardButton(text="🔍 Qidirish", switch_inline_query_current_chat="")
        ],
        [
            InlineKeyboardButton(text=" ✉️Ulashish", switch_inline_query="Zo'r bot ekan")
        ],
    ]
)

#Kurslar uchun keyboard

coursesMenu=InlineKeyboardMarkup(row_width=1)

python=InlineKeyboardButton(text="Python Dasturlash Asoslari", callback_data=course_callback.new(item_name="python"))
coursesMenu.insert(python)

django=InlineKeyboardButton(text="Django Web Dasturlash", callback_data=course_callback.new(item_name="django"))
coursesMenu.insert(django)

telegram=InlineKeyboardButton(text="Mukammal Telegram Bot", callback_data="course:telegram")
coursesMenu.insert(telegram)

algorithm=InlineKeyboardButton(text="Ma'lumotlar Tuzilmasi va Algoritmlar", callback_data="course:algorithm")
coursesMenu.insert(algorithm)

back_button=InlineKeyboardButton(text="Ortga", callback_data="cancel")
coursesMenu.insert(back_button)

# 3-usul

books={
    "Python. Dasturlash Asoslari":"python_book",
    "C++. Dasturlash Tili": "cpp_book",
    "JavaScript. Mukammal Dasturlash": "js_book",
}

booksMenu=InlineKeyboardMarkup(row_width=1)
for key, value in books.items():
    booksMenu.insert(InlineKeyboardButton(text=key, callback_data=book_callback.new(item_name=value)))
booksMenu.insert(back_button)

# Har bir kurs uchun Tugma

telegram_keyboard=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Xarid Qilish", url="https://mohirdev.uz/courses/telegram/")
        ]
    ]
)

algorithm_keyboard=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Ko'rish", url="https://mohirdev.uz/courses/algoritmlar/")
        ]
    ]
)

python_dasturlash_asoslari=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Ko'rish", url="https://mohirdev.uz/courses/python/")
        ]
    ]
)

django_web_dasturlash=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Ko'rish", url="https://mohirdev.uz/courses/django/")
        ]
    ]
)