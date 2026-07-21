import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, F, Router
from aiogram.types import (
    Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
)
from aiogram.filters import CommandStart, Command
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

# ===== CONFIG =====
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8574868400:AAGfluEsJUn5FkJ3NKrzKNyeZhts3lRFcvI")
YOUR_TELEGRAM = os.environ.get("YOUR_TELEGRAM", "ваш_username")
YOUR_PHONE = os.environ.get("YOUR_PHONE", "+375 XX XXX-XX-XX")
YOUR_EMAIL = os.environ.get("YOUR_EMAIL", "info@yourdomain.com")
YOUR_WEBSITE = os.environ.get("YOUR_WEBSITE", "https://yourdomain.com")
COMPANY_NAME = "Цифровое Агентство"
COMPANY_DESC = "Сайты · Администрирование · SEO · Контекстная реклама\n💸 Цены на 30% ниже рынка — качество без переплат!"

# ===== LOGGING =====
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)
log = logging.getLogger(__name__)

# ===== INIT =====
bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher()
router = Router()
dp.include_router(router)


# ===== KEYBOARDS =====

def main_menu_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🌐 Сайты", callback_data="sites"),
         InlineKeyboardButton(text="🛡️ Администрирование", callback_data="admin")],
        [InlineKeyboardButton(text="🔍 SEO-продвижение", callback_data="seo"),
         InlineKeyboardButton(text="🎯 Контекстная реклама", callback_data="ads")],
        [InlineKeyboardButton(text="📦 Комплексные пакеты", callback_data="packages")],
        [InlineKeyboardButton(text="🛠️ Дополнительные услуги", callback_data="extras")],
        [InlineKeyboardButton(text="📋 Полный прайс-лист", callback_data="full_price")],
        [InlineKeyboardButton(text="📞 Контакты", callback_data="contacts"),
         InlineKeyboardButton(text="❓ FAQ", callback_data="faq")],
        [InlineKeyboardButton(text="📝 Оставить заявку", callback_data="brief")],
    ])

def back_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⬅️ Назад в меню", callback_data="back")]
    ])

def back_with_action_kb(action_data, action_text):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=action_text, callback_data=action_data)],
        [InlineKeyboardButton(text="⬅️ Назад в меню", callback_data="back")]
    ])

def sites_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📄 Лендинг", callback_data="site_landing")],
        [InlineKeyboardButton(text="🏢 Сайт-визитка", callback_data="site_vizitka")],
        [InlineKeyboardButton(text="💼 Корпоративный", callback_data="site_corp")],
        [InlineKeyboardButton(text="🛒 Интернет-магазин", callback_data="site_shop")],
        [InlineKeyboardButton(text="📝 Заказать сайт", callback_data="brief_site")],
        [InlineKeyboardButton(text="⬅️ Назад в меню", callback_data="back")]
    ])

def admin_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📋 Разовые услуги", callback_data="admin_oneshot")],
        [InlineKeyboardButton(text="📦 Абонементы на сайт", callback_data="admin_site_sub")],
        [InlineKeyboardButton(text="🖥️ Абонементы на сервер", callback_data="admin_server_sub")],
        [InlineKeyboardButton(text="📝 Подключить", callback_data="brief_admin")],
        [InlineKeyboardButton(text="⬅️ Назад в меню", callback_data="back")]
    ])

def seo_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔍 SEO-аудит", callback_data="seo_audit")],
        [InlineKeyboardButton(text="🟢 Старт", callback_data="seo_start")],
        [InlineKeyboardButton(text="🔵 Оптима", callback_data="seo_optima")],
        [InlineKeyboardButton(text="🟣 Премиум", callback_data="seo_premium")],
        [InlineKeyboardButton(text="📝 Заказать SEO", callback_data="brief_seo")],
        [InlineKeyboardButton(text="⬅️ Назад в меню", callback_data="back")]
    ])

def ads_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🚀 Настройка рекламы", callback_data="ads_setup")],
        [InlineKeyboardButton(text="🟢 Ведение Базовое", callback_data="ads_basic")],
        [InlineKeyboardButton(text="🔵 Ведение Стандарт", callback_data="ads_standard")],
        [InlineKeyboardButton(text="🟣 Ведение Комплекс", callback_data="ads_complex")],
        [InlineKeyboardButton(text="📝 Заказать рекламу", callback_data="brief_ads")],
        [InlineKeyboardButton(text="⬅️ Назад в меню", callback_data="back")]
    ])

def packages_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🥉 Запуск — от 850 BYN", callback_data="pkg_start")],
        [InlineKeyboardButton(text="🥈 Рост — от 3 150 BYN", callback_data="pkg_growth")],
        [InlineKeyboardButton(text="🥇 Максимум — от 7 000 BYN", callback_data="pkg_max")],
        [InlineKeyboardButton(text="🏆 Всё включено", callback_data="pkg_all")],
        [InlineKeyboardButton(text="📝 Узнать стоимость", callback_data="brief_package")],
        [InlineKeyboardButton(text="⬅️ Назад в меню", callback_data="back")]
    ])

def contacts_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💬 Написать в Telegram", url=f"https://t.me/{YOUR_TELEGRAM}")],
        [InlineKeyboardButton(text="📞 Позвонить", url=f"tel:{YOUR_PHONE.replace(' ', '')}")],
        [InlineKeyboardButton(text="🌐 Наш сайт", url=YOUR_WEBSITE)],
        [InlineKeyboardButton(text="⬅️ Назад в меню", callback_data="back")]
    ])

def brief_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🌐 Заказать сайт", callback_data="brief_site")],
        [InlineKeyboardButton(text="🛡️ Администрирование", callback_data="brief_admin")],
        [InlineKeyboardButton(text="🔍 SEO-продвижение", callback_data="brief_seo")],
        [InlineKeyboardButton(text="🎯 Контекстная реклама", callback_data="brief_ads")],
        [InlineKeyboardButton(text="📦 Комплексный пакет", callback_data="brief_package")],
        [InlineKeyboardButton(text="💬 Написать менеджеру", url=f"https://t.me/{YOUR_TELEGRAM}")],
        [InlineKeyboardButton(text="⬅️ Назад в меню", callback_data="back")]
    ])


# ===== TEXTS =====

WELCOME_TEXT = f"""
👋 <b>Добро пожаловать в {COMPANY_NAME}!</b>

{COMPANY_DESC}

🏷️ <b>Наши цены на 30% ниже рынка</b> — без потери качества!

Выберите интересующий раздел:

🌐 <b>Сайты</b> — от 700 BYN
🛡️ <b>Администрирование</b> — от 35 BYN/мес
🔍 <b>SEO</b> — от 350 BYN/мес
🎯 <b>Контекстная реклама</b> — от 105 BYN/мес
📦 <b>Пакеты</b> — от 850 BYN
"""

SITES_TEXT = """
🌐 <b>Создание сайтов</b>

🏷️ <i>Цены на 30% ниже рынка белорусских студий</i>

📄 <b>Лендинг</b> — от 700 BYN
🏢 <b>Сайт-визитка</b> — от 850 BYN
💼 <b>Корпоративный</b> — от 1 400 BYN
🛒 <b>Интернет-магазин</b> — от 2 100 BYN
"""

SITE_LANDING = """
📄 <b>Лендинг (одностраничник)</b>

Продающий сайт для привлечения заявок и клиентов.

💰 <b>от 700 BYN</b> <s>(рынок: от 1 000 BYN)</s>
⏱ Срок: 5–10 рабочих дней

✅ Что входит:
• Дизайн по вашему бренду
• Адаптивная мобильная версия
• Форма обратной связи
• Базовая SEO-оптимизация
• Яндекс.Метрика
• 1 месяц хостинга в подарок
"""

SITE_VIZITKA = """
🏢 <b>Сайт-визитка (3–5 страниц)</b>

Компактный сайт для презентации компании и услуг.

💰 <b>от 850 BYN</b> <s>(рынок: от 1 200 BYN)</s>
⏱ Срок: 7–14 рабочих дней

✅ Что входит:
• Дизайн по вашему бренду
• 3–5 страниц с контентом
• Адаптивная мобильная версия
• Форма обратной связи
• Базовая SEO-оптимизация
• Яндекс.Метрика
• 1 месяц хостинга в подарок
"""

SITE_CORP = """
💼 <b>Корпоративный сайт</b>

Многостраничный сайт с каталогом услуг и разделами.

💰 <b>от 1 400 BYN</b> <s>(рынок: от 2 000 BYN)</s>
⏱ Срок: 14–21 рабочий день

✅ Что входит:
• Уникальный дизайн
• До 15 страниц
• Адаптивная мобильная версия
• Полная SEO-оптимизация
• Яндекс.Метрика + Google Analytics
• CRM-интеграция
• Контент-наполнение
• 1 месяц хостинга в подарок
"""

SITE_SHOP = """
🛒 <b>Интернет-магазин</b>

Полноценный магазин с корзиной, оплатой и CRM.

💰 <b>от 2 100 BYN</b> <s>(рынок: от 3 000 BYN)</s>
⏱ Срок: 21–35 рабочих дней

✅ Что входит:
• Уникальный дизайн
• Каталог товаров с фильтрами
• Корзина и онлайн-оплата
• Интеграция с 1С / CRM
• SEO + Яндекс.Метрика + Analytics
• Система управления заказами
• Обучение администрированию
• 1 месяц хостинга в подарок
"""

ADMIN_TEXT = """
🛡️ <b>Администрирование</b>

🏷️ <i>Цены на 30% ниже рынка</i>

Поддержка, безопасность и бесперебойная работа.
"""

ADMIN_ONESHOT = """
🛡️ <b>Разовые услуги администрирования</b>

🖥️ Настройка сервера / VPS — <b>от 55 BYN</b>
🔄 Перенос сайта — <b>от 35 BYN</b>
🔒 Установка SSL — <b>от 15 BYN</b>
💾 Настройка бэкапов — <b>от 25 BYN</b>
🛡️ Защита от взлома — <b>от 40 BYN</b>
🌐 Домен + DNS — <b>от 25 BYN/год</b>
📬 Корпоративная почта — <b>от 30 BYN</b>
📊 Мониторинг — <b>от 20 BYN</b>
🔧 Восстановление после взлома — <b>от 70 BYN</b>
📦 Установка CMS — <b>от 40 BYN</b>
"""

ADMIN_SITE_SUB = """
🛡️ <b>Абонементы на поддержку сайта</b>

🟢 <b>Старт — 35 BYN/мес</b>
• Обновление CMS и плагинов
• Еженедельные бэкапы
• Мониторинг uptime
• До 2 часов работ в месяц

🔵 <b>Стандарт — 85 BYN/мес</b> ⭐
• Всё из «Старта»
• Ежедневные бэкапы
• Защита от взлома
• До 5 часов работ в месяц
• Приоритетная поддержка

🟣 <b>Премиум — 175 BYN/мес</b>
• Всё из «Стандарта»
• Мониторинг 24/7
• DDoS-защита
• До 10 часов работ в месяц
• Персональный менеджер

<i><s>Рынок: 50 / 120 / 250 BYN</s></i>
"""

ADMIN_SERVER_SUB = """
🖥️ <b>Абонементы на администрирование сервера</b>

🟢 <b>Базовое — 55 BYN/мес</b>
• Мониторинг сервера
• Обновление ОС и ПО
• Еженедельные бэкапы
• Реагирование на сбои

🔵 <b>Стандарт — 105 BYN/мес</b> ⭐
• Всё из «Базового»
• Мониторинг 24/7
• Настройка безопасности
• Оптимизация производительности

🟣 <b>Полное — 175 BYN/мес</b>
• Всё из «Стандарта»
• DDoS-защита
• Безлимитные работы
• Персональный менеджер
"""

SEO_TEXT = """
🔍 <b>SEO-продвижение</b>

🏷️ <i>Цены на 30% ниже рынка</i>

Органический трафик и топ-позиции в Яндексе и Google.
"""

SEO_AUDIT = """
🔍 <b>SEO-аудит сайта</b>

💰 <b>от 250 BYN</b> <s>(рынок: от 350 BYN)</s>
⏱ Срок: 5–10 дней

✅ Что входит:
• Технический аудит
• Анализ конкурентов
• Проверка индексации
• Аудит мета-тегов и контента
• PDF-отчёт с планом действий
"""

SEO_START = """
🟢 <b>SEO «Старт»</b>

💰 <b>от 350 BYN/мес</b> <s>(рынок: от 500 BYN)</s>
⏱ Минимум 3 месяца

✅ Что входит:
• Семантика до 200 запросов
• Технический аудит и исправления
• Оптимизация мета-тегов
• Улучшение скорости загрузки
• Ежемесячный отчёт
"""

SEO_OPTIMA = """
🔵 <b>SEO «Оптима»</b> ⭐

💰 <b>от 630 BYN/мес</b> <s>(рынок: от 900 BYN)</s>
⏱ Минимум 3 месяца

✅ Что входит:
• Семантика до 500 запросов
• Полная внутренняя оптимизация
• Работа с контентом
• Внешняя оптимизация
• Еженедельные отчёты
• Мониторинг конкурентов
"""

SEO_PREMIUM = """
🟣 <b>SEO «Премиум»</b>

💰 <b>от 1 050 BYN/мес</b> <s>(рынок: от 1 500 BYN)</s>
⏱ Минимум 6 месяцев

✅ Что входит:
• Всё из «Оптима»
• Расширенная семантика (500+)
• Копирайтинг (статьи в блог)
• Локальное SEO (Карты, 2GIS)
• Внешняя ссылочная масса
• Персональный SEO-специалист
"""

ADS_TEXT = """
🎯 <b>Контекстная реклама</b>

🏷️ <i>Цены на 30% ниже рынка</i>

Быстрые заявки из Яндекс.Директ и Google Ads.
"""

ADS_SETUP = """
🚀 <b>Настройка контекстной рекламы</b>

💰 <b>от 180 BYN</b> (1 система) <s>(рынок: от 250 BYN)</s>
💰 <b>от 280 BYN</b> (Директ + Ads) <s>(рынок: от 400 BYN)</s>
⏱ Срок: 3–5 дней

✅ Что входит:
• Сбор ключевых слов и минус-слов
• Написание объявлений
• Настройка целей в Метрике
• Запуск кампании

💵 Мин. бюджет на клики: от 300 BYN/мес
"""

ADS_BASIC = """
🟢 <b>Ведение «Базовое»</b>

💰 <b>от 105 BYN/мес</b> <s>(рынок: от 150 BYN)</s>

✅ Что входит:
• 1 система (Директ ИЛИ Ads)
• Оптимизация ставок
• Корректировка объявлений
• Ежемесячный отчёт
"""

ADS_STANDARD = """
🔵 <b>Ведение «Стандарт»</b> ⭐

💰 <b>от 175 BYN/мес</b> <s>(рынок: от 250 BYN)</s>

✅ Что входит:
• Яндекс.Директ + Google Ads
• A/B тестирование
• Ретаргетинг
• Еженедельные отчёты
"""

ADS_COMPLEX = """
🟣 <b>Ведение «Комплексное»</b>

💰 <b>от 280 BYN/мес</b> <s>(рынок: от 400 BYN)</s>

✅ Что входит:
• Всё из «Стандарта»
• Динамический ретаргетинг
• Аналитика конверсий + коллтрекинг
• Оптимизация посадочных страниц
• Анализ конкурентов
"""

PACKAGES_TEXT = """
📦 <b>Комплексные пакеты</b>

🏷️ <i>Ещё выгоднее, чем по отдельности!</i>
"""

PKG_START = """
🥉 <b>Пакет «Запуск»</b>

💰 <b>от 850 BYN</b> <s>(по отдельности: от 1 200 BYN)</s>

✅ Включено:
• Лендинг
• SEO-аудит
• Яндекс.Метрика
• 1 месяц хостинга
• Базовая SEO-оптимизация
"""

PKG_GROWTH = """
🥈 <b>Пакет «Рост»</b>

💰 <b>от 3 150 BYN</b> <s>(по отдельности: от 4 500 BYN)</s>

✅ Включено:
• Корпоративный сайт
• SEO на 3 месяца
• Контекстная реклама на 1 месяц
• Администрирование на 3 месяца
• Яндекс.Метрика + Analytics
"""

PKG_MAX = """
🥇 <b>Пакет «Максимум»</b>

💰 <b>от 7 000 BYN</b> <s>(по отдельности: от 10 000 BYN)</s>

✅ Включено:
• Интернет-магазин
• SEO на 6 месяцев
• Контекстная реклама на 3 месяца
• Администрирование на 6 месяцев
• CRM-интеграция + коллтрекинг
"""

PKG_ALL = """
🏆 <b>Пакет «Всё включено»</b>

💰 <b>Стоимость обсуждается</b>

✅ Включено:
• Сайт любой сложности
• SEO + реклама + администрирование
• Техподдержка 24/7
• Персональный менеджер
• KPI в договоре
"""

EXTRAS_TEXT = """
🛠️ <b>Дополнительные услуги</b>

🏷️ <i>На 30% ниже рынка</i>

🎨 Редизайн сайта — <b>от 350 BYN</b>
⚡ Ускорение сайта — <b>от 105 BYN</b>
🔗 CRM-интеграция — <b>от 140 BYN</b>
📱 Мобильная адаптация — <b>от 105 BYN</b>
📊 Настройка аналитики — <b>от 70 BYN</b>
📞 Коллтрекинг — <b>от 55 BYN</b>
✍️ Копирайтинг — <b>от 20 BYN / 1000 знаков</b>
🎓 Обучение — <b>от 35 BYN / час</b>
📋 Регистрация в БелГИЭ — <b>от 25 BYN</b>
📝 Тексты для сайта — <b>от 35 BYN / страница</b>
"""

FULL_PRICE = """
📋 <b>ПОЛНЫЙ ПРАЙС-ЛИСТ</b>
🏷️ <i>Цены на 30% ниже рынка</i>

━━━━━━━━━━━━━━━━━━
🌐 <b>САЙТЫ</b>
📄 Лендинг — от 700 BYN
🏢 Визитка — от 850 BYN
💼 Корпоративный — от 1 400 BYN
🛒 Магазин — от 2 100 BYN
━━━━━━━━━━━━━━━━━━
🛡️ <b>АДМИН (разовые)</b>
🖥️ Сервер — от 55 BYN
🔄 Перенос — от 35 BYN
🔒 SSL — от 15 BYN
💾 Бэкапы — от 25 BYN
🛡️ Защита — от 40 BYN
🌐 Домен — от 25 BYN/год
━━━━━━━━━━━━━━━━━━
📦 <b>АБОНЕМЕНТЫ САЙТ</b>
🟢 Старт — 35 BYN/мес
🔵 Стандарт — 85 BYN/мес
🟣 Премиум — 175 BYN/мес
━━━━━━━━━━━━━━━━━━
🖥️ <b>АБОНЕМЕНТЫ СЕРВЕР</b>
🟢 Базовое — 55 BYN/мес
🔵 Стандарт — 105 BYN/мес
🟣 Полное — 175 BYN/мес
━━━━━━━━━━━━━━━━━━
🔍 <b>SEO</b>
Аудит — от 250 BYN
🟢 Старт — от 350 BYN/мес
🔵 Оптима — от 630 BYN/мес
🟣 Премиум — от 1 050 BYN/мес
━━━━━━━━━━━━━━━━━━
🎯 <b>РЕКЛАМА</b>
Настройка — от 180 BYN
🟢 Базовое — от 105 BYN/мес
🔵 Стандарт — от 175 BYN/мес
🟣 Комплекс — от 280 BYN/мес
━━━━━━━━━━━━━━━━━━
📦 <b>ПАКЕТЫ</b>
🥉 Запуск — от 850 BYN
🥈 Рост — от 3 150 BYN
🥇 Максимум — от 7 000 BYN
🏆 Всё включено — индивидуально
━━━━━━━━━━━━━━━━━━

⚠️ <i>Точная стоимость — после брифования.</i>
💸 <i>Все цены уже на 30% ниже рынка!</i>
"""

CONTACTS_TEXT = f"""
📞 <b>Контакты</b>

💬 Telegram: @{YOUR_TELEGRAM}
📞 Телефон: {YOUR_PHONE}
📧 Email: {YOUR_EMAIL}
🌐 Сайт: {YOUR_WEBSITE}

🕐 Пн–Пт 9:00–18:00
📨 Заявки 24/7
"""

FAQ_TEXT = """
❓ <b>Частые вопросы</b>

<b>Почему дешевле?</b>
→ Небольшая студия без раздутого штата. Меньше накладных = ниже цены.

<b>Сколько стоит сайт?</b>
→ Лендинг от 700 BYN. Точная стоимость после брифования.

<b>Сроки создания?</b>
→ Лендинг от 5 дней, магазин от 3 недель.

<b>Бюджет на рекламу?</b>
→ От 300 BYN/мес + работа специалиста.

<b>Эффект от SEO?</b>
→ Первые результаты через 2–4 месяца.

<b>Входит в админ?</b>
→ Обновления, бэкапы, мониторинг, защита.

<b>Регионы?</b>
→ Да, удалённо по всей Беларуси и СНГ.

<b>Гарантии?</b>
→ KPI в договоре. Оплата поэтапно.

<b>Порядок оплаты?</b>
→ Предоплата 50%, остаток по сдаче.
"""

BRIEF_TEXT = """
📝 <b>Оставить заявку</b>

Выберите услугу — свяжемся в течение 30 минут:

💡 <i>Или напишите задачу своими словами!</i>
"""

BRIEF_SITE = """
📝 <b>Заявка на сайт</b>

Напишите:
1️⃣ Тип сайта (лендинг / визитка / корпоративный / магазин)
2️⃣ Ваш бизнес
3️⃣ Примеры сайтов
4️⃣ Бюджет
"""

BRIEF_ADMIN = """
📝 <b>Заявка на администрирование</b>

Напишите:
1️⃣ Что нужно? (сервер / перенос / защита / подписка)
2️⃣ Ваша CMS
3️⃣ Доступы к хостингу
"""

BRIEF_SEO = """
📝 <b>Заявка на SEO</b>

Напишите:
1️⃣ Адрес сайта
2️⃣ Ниша
3️⃣ Ожидаемый результат
4️⃣ Бюджет
"""

BRIEF_ADS = """
📝 <b>Заявка на рекламу</b>

Напишите:
1️⃣ Что продвигаем?
2️⃣ Регион
3️⃣ Бюджет на рекламу
4️⃣ Опыт с Директ/Ads
"""

BRIEF_PACKAGE = """
📝 <b>Заявка на пакет</b>

Напишите:
1️⃣ Какой пакет? (Запуск / Рост / Максимум / Всё включено)
2️⃣ Ваш бизнес
3️⃣ Цель
4️⃣ Бюджет
"""


# ===== HANDLERS =====

@router.message(CommandStart())
async def cmd_start(message: Message):
    log.info(f"/start from user {message.from_user.id}")
    await message.answer(WELCOME_TEXT, reply_markup=main_menu_kb())

@router.message(Command("menu"))
async def cmd_menu(message: Message):
    await message.answer("📋 <b>Главное меню</b>", reply_markup=main_menu_kb())

@router.message(Command("price"))
async def cmd_price(message: Message):
    await message.answer(FULL_PRICE, reply_markup=back_with_action_kb("brief", "📝 Заявка"))

@router.message(Command("contacts"))
async def cmd_contacts(message: Message):
    await message.answer(CONTACTS_TEXT, reply_markup=contacts_kb())

@router.message(Command("faq"))
async def cmd_faq(message: Message):
    await message.answer(FAQ_TEXT, reply_markup=back_kb())

# Callbacks
@router.callback_query(F.data == "back")
async def cb_back(callback: CallbackQuery):
    await callback.message.edit_text(WELCOME_TEXT, reply_markup=main_menu_kb())
    await callback.answer()

@router.callback_query(F.data == "sites")
async def cb_sites(callback: CallbackQuery):
    await callback.message.edit_text(SITES_TEXT, reply_markup=sites_kb())
    await callback.answer()

@router.callback_query(F.data == "admin")
async def cb_admin(callback: CallbackQuery):
    await callback.message.edit_text(ADMIN_TEXT, reply_markup=admin_kb())
    await callback.answer()

@router.callback_query(F.data == "seo")
async def cb_seo(callback: CallbackQuery):
    await callback.message.edit_text(SEO_TEXT, reply_markup=seo_kb())
    await callback.answer()

@router.callback_query(F.data == "ads")
async def cb_ads(callback: CallbackQuery):
    await callback.message.edit_text(ADS_TEXT, reply_markup=ads_kb())
    await callback.answer()

@router.callback_query(F.data == "packages")
async def cb_packages(callback: CallbackQuery):
    await callback.message.edit_text(PACKAGES_TEXT, reply_markup=packages_kb())
    await callback.answer()

@router.callback_query(F.data == "extras")
async def cb_extras(callback: CallbackQuery):
    await callback.message.edit_text(EXTRAS_TEXT, reply_markup=back_with_action_kb("brief", "📝 Заказать"))
    await callback.answer()

@router.callback_query(F.data == "full_price")
async def cb_full_price(callback: CallbackQuery):
    await callback.message.edit_text(FULL_PRICE, reply_markup=back_with_action_kb("brief", "📝 Заявка"))
    await callback.answer()

@router.callback_query(F.data == "contacts")
async def cb_contacts(callback: CallbackQuery):
    await callback.message.edit_text(CONTACTS_TEXT, reply_markup=contacts_kb())
    await callback.answer()

@router.callback_query(F.data == "faq")
async def cb_faq(callback: CallbackQuery):
    await callback.message.edit_text(FAQ_TEXT, reply_markup=back_kb())
    await callback.answer()

@router.callback_query(F.data == "brief")
async def cb_brief(callback: CallbackQuery):
    await callback.message.edit_text(BRIEF_TEXT, reply_markup=brief_kb())
    await callback.answer()

# Sites
@router.callback_query(F.data == "site_landing")
async def cb_site_landing(callback: CallbackQuery):
    await callback.message.edit_text(SITE_LANDING, reply_markup=back_with_action_kb("brief_site", "📝 Заказать"))
    await callback.answer()

@router.callback_query(F.data == "site_vizitka")
async def cb_site_vizitka(callback: CallbackQuery):
    await callback.message.edit_text(SITE_VIZITKA, reply_markup=back_with_action_kb("brief_site", "📝 Заказать"))
    await callback.answer()

@router.callback_query(F.data == "site_corp")
async def cb_site_corp(callback: CallbackQuery):
    await callback.message.edit_text(SITE_CORP, reply_markup=back_with_action_kb("brief_site", "📝 Заказать"))
    await callback.answer()

@router.callback_query(F.data == "site_shop")
async def cb_site_shop(callback: CallbackQuery):
    await callback.message.edit_text(SITE_SHOP, reply_markup=back_with_action_kb("brief_site", "📝 Заказать"))
    await callback.answer()

# Admin
@router.callback_query(F.data == "admin_oneshot")
async def cb_admin_oneshot(callback: CallbackQuery):
    await callback.message.edit_text(ADMIN_ONESHOT, reply_markup=back_with_action_kb("brief_admin", "📝 Заказать"))
    await callback.answer()

@router.callback_query(F.data == "admin_site_sub")
async def cb_admin_site_sub(callback: CallbackQuery):
    await callback.message.edit_text(ADMIN_SITE_SUB, reply_markup=back_with_action_kb("brief_admin", "📝 Подключить"))
    await callback.answer()

@router.callback_query(F.data == "admin_server_sub")
async def cb_admin_server_sub(callback: CallbackQuery):
    await callback.message.edit_text(ADMIN_SERVER_SUB, reply_markup=back_with_action_kb("brief_admin", "📝 Подключить"))
    await callback.answer()

# SEO
@router.callback_query(F.data == "seo_audit")
async def cb_seo_audit(callback: CallbackQuery):
    await callback.message.edit_text(SEO_AUDIT, reply_markup=back_with_action_kb("brief_seo", "📝 Заказать"))
    await callback.answer()

@router.callback_query(F.data == "seo_start")
async def cb_seo_start(callback: CallbackQuery):
    await callback.message.edit_text(SEO_START, reply_markup=back_with_action_kb("brief_seo", "📝 Заказать"))
    await callback.answer()

@router.callback_query(F.data == "seo_optima")
async def cb_seo_optima(callback: CallbackQuery):
    await callback.message.edit_text(SEO_OPTIMA, reply_markup=back_with_action_kb("brief_seo", "📝 Заказать"))
    await callback.answer()

@router.callback_query(F.data == "seo_premium")
async def cb_seo_premium(callback: CallbackQuery):
    await callback.message.edit_text(SEO_PREMIUM, reply_markup=back_with_action_kb("brief_seo", "📝 Заказать"))
    await callback.answer()

# Ads
@router.callback_query(F.data == "ads_setup")
async def cb_ads_setup(callback: CallbackQuery):
    await callback.message.edit_text(ADS_SETUP, reply_markup=back_with_action_kb("brief_ads", "📝 Настроить"))
    await callback.answer()

@router.callback_query(F.data == "ads_basic")
async def cb_ads_basic(callback: CallbackQuery):
    await callback.message.edit_text(ADS_BASIC, reply_markup=back_with_action_kb("brief_ads", "📝 Заказать"))
    await callback.answer()

@router.callback_query(F.data == "ads_standard")
async def cb_ads_standard(callback: CallbackQuery):
    await callback.message.edit_text(ADS_STANDARD, reply_markup=back_with_action_kb("brief_ads", "📝 Заказать"))
    await callback.answer()

@router.callback_query(F.data == "ads_complex")
async def cb_ads_complex(callback: CallbackQuery):
    await callback.message.edit_text(ADS_COMPLEX, reply_markup=back_with_action_kb("brief_ads", "📝 Заказать"))
    await callback.answer()

# Packages
@router.callback_query(F.data == "pkg_start")
async def cb_pkg_start(callback: CallbackQuery):
    await callback.message.edit_text(PKG_START, reply_markup=back_with_action_kb("brief_package", "📝 Заказать"))
    await callback.answer()

@router.callback_query(F.data == "pkg_growth")
async def cb_pkg_growth(callback: CallbackQuery):
    await callback.message.edit_text(PKG_GROWTH, reply_markup=back_with_action_kb("brief_package", "📝 Заказать"))
    await callback.answer()

@router.callback_query(F.data == "pkg_max")
async def cb_pkg_max(callback: CallbackQuery):
    await callback.message.edit_text(PKG_MAX, reply_markup=back_with_action_kb("brief_package", "📝 Заказать"))
    await callback.answer()

@router.callback_query(F.data == "pkg_all")
async def cb_pkg_all(callback: CallbackQuery):
    await callback.message.edit_text(PKG_ALL, reply_markup=back_with_action_kb("brief_package", "📝 Обсудить"))
    await callback.answer()

# Briefs
@router.callback_query(F.data == "brief_site")
async def cb_brief_site(callback: CallbackQuery):
    await callback.message.edit_text(BRIEF_SITE, reply_markup=InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💬 Написать менеджеру", url=f"https://t.me/{YOUR_TELEGRAM}")],
        [InlineKeyboardButton(text="⬅️ Назад", callback_data="back")]
    ]))
    await callback.answer()

@router.callback_query(F.data == "brief_admin")
async def cb_brief_admin(callback: CallbackQuery):
    await callback.message.edit_text(BRIEF_ADMIN, reply_markup=InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💬 Написать менеджеру", url=f"https://t.me/{YOUR_TELEGRAM}")],
        [InlineKeyboardButton(text="⬅️ Назад", callback_data="back")]
    ]))
    await callback.answer()

@router.callback_query(F.data == "brief_seo")
async def cb_brief_seo(callback: CallbackQuery):
    await callback.message.edit_text(BRIEF_SEO, reply_markup=InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💬 Написать менеджеру", url=f"https://t.me/{YOUR_TELEGRAM}")],
        [InlineKeyboardButton(text="⬅️ Назад", callback_data="back")]
    ]))
    await callback.answer()

@router.callback_query(F.data == "brief_ads")
async def cb_brief_ads(callback: CallbackQuery):
    await callback.message.edit_text(BRIEF_ADS, reply_markup=InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💬 Написать менеджеру", url=f"https://t.me/{YOUR_TELEGRAM}")],
        [InlineKeyboardButton(text="⬅️ Назад", callback_data="back")]
    ]))
    await callback.answer()

@router.callback_query(F.data == "brief_package")
async def cb_brief_package(callback: CallbackQuery):
    await callback.message.edit_text(BRIEF_PACKAGE, reply_markup=InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💬 Написать менеджеру", url=f"https://t.me/{YOUR_TELEGRAM}")],
        [InlineKeyboardButton(text="⬅️ Назад", callback_data="back")]
    ]))
    await callback.answer()


# ===== MAIN =====

async def main():
    log.info(f"🤖 Бот {COMPANY_NAME} запущен!")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
