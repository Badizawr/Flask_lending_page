import sqlite3

data = {
    'carouselExampleIndicators': [
        {
            'short_title': 'Slider',
            'img': 'https://via.placeholder.com/1024x500',
            'altimg': 'image 1',
            'title': 'Title Test 1',
            'contenttext': 'some text for slider 1 ',
            'author': None,
            'timestampdata': None
        },
        {
            'short_title': 'Slider',
            'img': 'https://via.placeholder.com/1024x500',
            'altimg': 'image 2',
            'title': 'Title Test 2',
            'contenttext': 'some text for slider 2 ',
            'author': None,
            'timestampdata': None
        }
    ],
    'cards': [
        {
            'short_title': 'miniCards',
            'img': 'https://via.placeholder.com/150',
            'altimg': 'mini img 2',
            'title': 'mini card 2',
            'contenttext': 'text for mini card 2',
            'author': None,
            'timestampdata': None
        },
        {
            'short_title': 'miniCards',
            'img': 'https://via.placeholder.com/150',
            'altimg': 'mini img 1',
            'title': 'mini card 1',
            'contenttext': 'text for mini card 1',
            'author': None,
            'timestampdata': None
        }
    ]
}

# Создание или подключение к базе данных
conn = sqlite3.connect('database.db')

# Создание курсора
c = conn.cursor()

# Создание таблицы Content
c.execute('''CREATE TABLE IF NOT EXISTS content (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             idblock TEXT,
             short_title TEXT,
             img TEXT,
             altimg TEXT,
             title TEXT,
             contenttext TEXT,
             author TEXT,
             timestampdata DATETIME)''')

for section, items in data.items():
    for item in items:
        c.execute("INSERT INTO content (idblock, short_title, img, altimg, title, contenttext, author, timestampdata) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                  (section, item['short_title'], item['img'], item['altimg'], item['title'], item['contenttext'], item['author'], item['timestampdata']))

# Фиксация изменений в базе данных
conn.commit()

# Создание таблицы Users
c.execute('''CREATE TABLE IF NOT EXISTS users (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             username TEXT,
             password TEXT)''')

# Закрытие соединения с базой данных
conn.close()