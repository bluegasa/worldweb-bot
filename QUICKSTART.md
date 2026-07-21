# 🚀 Быстрый запуск бота на вашем компьютере

## Если у вас Windows:

### Шаг 1: Установите Python
Скачайте с https://python.org (версия 3.10+)
❗️ При установке поставьте галочку "Add Python to PATH"

### Шаг 2: Скачайте файлы
Скачайте всю папку telegram-bot к себе на компьютер

### Шаг 3: Замените контакты в config.py
Откройте config.py в блокноте и замените:
- YOUR_TELEGRAM = "ваш_username"  → ваш Telegram username без @
- YOUR_PHONE = "+375 XX XXX-XX-XX" → ваш номер
- YOUR_EMAIL = "info@yourdomain.com" → ваша почта
- YOUR_WEBSITE = "https://yourdomain.com" → ваш сайт

### Шаг 4: Запустите
Дважды кликните на файл start.bat
Или откройте командную строку в папке бота и введите:
```
pip install aiogram==3.13.1
python bot.py
```

### Готово! 🎉
Откройте @worldwwweb_bot в Telegram и нажмите /start

---

## Если у вас Mac/Linux:

Откройте терминал в папке бота:
```
chmod +x start.sh
./start.sh
```

---

## Чтобы бот работал 24/7 (не только когда включён ПК):

### Вариант 1: Amvera.cloud (бесплатно)
1. Зарегистрируйтесь на amvera.cloud
2. Создайте проект Python
3. Загрузите bot.py, config.py, requirements.txt
4. Бот будет работать 24/7

### Вариант 2: Railway.app (бесплатный тариф)
1. Зарегистрируйтесь на railway.app
2. Создайте новый проект из GitHub
3. Добавьте файлы бота
4. Бот запустится автоматически

### Вариант 3: VPS (от 5$/мес)
1. Арендуйте VPS на activecloud.by, bell.by или timeweb.com
2. Загрузите файлы через SSH
3. Запустите: nohup python3 bot.py &
