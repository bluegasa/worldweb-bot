# 🚀 ПОШАГОВАЯ ИНСТРУКЦИЯ: Запуск бота на Render.com (бесплатно, 24/7)

## Что у вас уже готово:
✅ Код бота с прайс-листом Беларуси (-30% от рынка)
✅ Все файлы для деплоя
✅ Токен бота: 8574868400:AAGfluEsJUn5FkJ3NKrzKNyeZhts3lRFcvI

---

## ШАГ 1: Создайте аккаунт GitHub (2 минуты)

1. Откройте https://github.com/signup
2. Придумайте логин, email, пароль
3. Подтвердите email

---

## ШАГ 2: Создайте репозиторий на GitHub (1 минута)

1. Нажмите кнопку **"New"** (зелёная) или "+" → "New repository"
2. Repository name: **worldweb-bot**
3. Поставьте ✅ "Add a README file"
4. Нажмите **"Create repository"**

---

## ШАГ 3: Загрузите файлы бота на GitHub

### Вариант А — через браузер (проще):

1. В репозитории нажмите **"Add file"** → **"Upload files"**
2. Перетащите эти файлы из папки telegram-bot:
   - `bot.py`
   - `requirements.txt`
   - `Dockerfile`
   - `.gitignore`
3. Нажмите **"Commit changes"**

### Вариант Б — через командную строку (если установлен git):

Откройте терминал в папке telegram-bot и введите:
```
git remote add origin https://github.com/ВАШ_ЛОГИН/worldweb-bot.git
git branch -M main
git push -u origin main
```

---

## ШАГ 4: Зарегистрируйтесь на Render.com (2 минуты)

1. Откройте https://dashboard.render.com/register
2. Нажмите **"Sign up with GitHub"** — используйте тот же GitHub аккаунт
3. Подтвердите доступ к вашему репозиторию

---

## ШАГ 5: Создайте сервис бота (3 минуты)

1. В панели Render нажмите **"New +"** → **"Web Service"** 
   (если нет Web Service — выберите **"Background Worker"**)
2. Найдите ваш репозиторий **worldweb-bot** и нажмите **"Connect"**
3. Настройки:
   - **Name:** worldweb-bot
   - **Runtime:** Python 3 (или Docker, если есть выбор)
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python bot.py`
   - **Instance Type:** Free ✅
4. Прокрутите вниз до **"Environment Variables"** и добавьте:

| Key | Value |
|-----|-------|
| `BOT_TOKEN` | `8574868400:AAGfluEsJUn5FkJ3NKrzKNyeZhts3lRFcvI` |
| `YOUR_TELEGRAM` | `ваш_username` (БЕЗ @) |
| `YOUR_PHONE` | `+375 29 XXX-XX-XX` |
| `YOUR_EMAIL` | `ваш@email.com` |
| `YOUR_WEBSITE` | `https://ваш-сайт.by` |

5. Нажмите **"Create Web Service"** (или "Apply")

---

## 🎉 Готово!

Render автоматически:
- Скачает код из GitHub
- Установит зависимости
- Запустит бота

Через 2–3 минуты бот будет работать 24/7!

---

## Проверка:
- Откройте @worldwwweb_bot в Telegram
- Нажмите /start
- Вы увидите полное меню с прайс-листом!

---

## Если нужно обновить бота:
1. Измените файлы на GitHub
2. Render автоматически перезапустит бота (2-3 минуты)

---

## Логи бота:
В панели Render → ваш сервис → "Logs" — видны все логи в реальном времени

---

## ⚠️ Важно: Бесплатный тариф Render
- Бот "засыпает" через 15 минут без активности
- Но для Telegram-бота это НЕ проблема — бот просыпается автоматически при новом сообщении
- 750 часов бесплатно в месяц (хватит на 1 бота)
