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
from aiogram.exceptions import TelegramBadRequest

BOT_TOKEN = os.getenv("BOT_TOKEN", "8574868400:AAGfluEsJUn5FkJ3NKrzKNyeZhts3lRFcvI")
YOUR_TELEGRAM = os.getenv("YOUR_TELEGRAM", "Worlds_Web")
YOUR_PHONE = os.getenv("YOUR_PHONE", "+375333525727")
YOUR_EMAIL = os.getenv("YOUR_EMAIL", "info@worldweb.by")
YOUR_WEBSITE = os.getenv("YOUR_WEBSITE", "https://worldweb.by")
COMPANY_NAME = "Цифровое Агентство"

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
log = logging.getLogger(__name__)

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()
router = Router()
dp.include_router(router)


# ══════════════════ ОБРАБОТКА ОШИБок ══════════════════

@dp.error()
async def on_error(event):
    err = event.exception
    if isinstance(err, TelegramBadRequest):
        msg = str(err)
        if "message is not modified" in msg:
            log.info("⚠️ Сообщение не изменено (двойное нажатие) — пропускаем")
            return True
        if "query is too old" in msg:
            log.info("⚠️ Старый callback — пропускаем")
            return True
    log.error(f"❌ Необработанная ошибка: {err}")
    return True


# ══════════════════ КЛАВИАТУРЫ ══════════════════

def main_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🌐  Создание сайтов", callback_data="sites"),
         InlineKeyboardButton(text="🛡️  Администрирование", callback_data="admin")],
        [InlineKeyboardButton(text="🔍  SEO-продвижение", callback_data="seo"),
         InlineKeyboardButton(text="🎯  Контекстная реклама", callback_data="ads")],
        [InlineKeyboardButton(text="📦  Комплексные пакеты", callback_data="packages")],
        [InlineKeyboardButton(text="🛠️  Дополнительно", callback_data="extras")],
        [InlineKeyboardButton(text="📋  Полный прайс-лист", callback_data="full_price")],
        [InlineKeyboardButton(text="📞  Контакты", callback_data="contacts"),
         InlineKeyboardButton(text="❓  FAQ", callback_data="faq")],
        [InlineKeyboardButton(text="📝  Оставить заявку", callback_data="brief")],
    ])

def back_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⬅️  Назад в меню", callback_data="back")]
    ])

def back_order(data, text):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=text, callback_data=data)],
        [InlineKeyboardButton(text="⬅️  Назад в меню", callback_data="back")]
    ])

def mgr_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💬  Написать менеджеру", url=f"https://t.me/{YOUR_TELEGRAM}")],
        [InlineKeyboardButton(text="⬅️  Назад в меню", callback_data="back")]
    ])

def sites_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📄  Лендинг — от 700 BYN", callback_data="site_landing")],
        [InlineKeyboardButton(text="🏢  Визитка — от 850 BYN", callback_data="site_vizitka")],
        [InlineKeyboardButton(text="💼  Корпоративный — от 1 400 BYN", callback_data="site_corp")],
        [InlineKeyboardButton(text="🛒  Интернет-магазин — от 2 100 BYN", callback_data="site_shop")],
        [InlineKeyboardButton(text="📝  Заказать сайт", callback_data="brief_site")],
        [InlineKeyboardButton(text="⬅️  Назад", callback_data="back")]
    ])

def admin_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📋  Разовые услуги", callback_data="admin_one")],
        [InlineKeyboardButton(text="📦  Абонементы на сайт", callback_data="admin_site")],
        [InlineKeyboardButton(text="🖥️  Абонементы на сервер", callback_data="admin_srv")],
        [InlineKeyboardButton(text="📝  Подключить", callback_data="brief_admin")],
        [InlineKeyboardButton(text="⬅️  Назад", callback_data="back")]
    ])

def seo_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔍  SEO-аудит — от 250 BYN", callback_data="seo_audit")],
        [InlineKeyboardButton(text="🟢  Старт — от 350 BYN/мес", callback_data="seo_start")],
        [InlineKeyboardButton(text="🔵  Оптима — от 630 BYN/мес", callback_data="seo_optima")],
        [InlineKeyboardButton(text="🟣  Премиум — от 1 050 BYN/мес", callback_data="seo_premium")],
        [InlineKeyboardButton(text="📝  Заказать SEO", callback_data="brief_seo")],
        [InlineKeyboardButton(text="⬅️  Назад", callback_data="back")]
    ])

def ads_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🚀  Настройка — от 180 BYN", callback_data="ads_setup")],
        [InlineKeyboardButton(text="🟢  Базовое — от 105 BYN/мес", callback_data="ads_basic")],
        [InlineKeyboardButton(text="🔵  Стандарт — от 175 BYN/мес", callback_data="ads_stand")],
        [InlineKeyboardButton(text="🟣  Комплекс — от 280 BYN/мес", callback_data="ads_complex")],
        [InlineKeyboardButton(text="📝  Заказать рекламу", callback_data="brief_ads")],
        [InlineKeyboardButton(text="⬅️  Назад", callback_data="back")]
    ])

def packages_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🥉  Запуск — от 850 BYN", callback_data="pkg_start")],
        [InlineKeyboardButton(text="🥈  Рост — от 3 150 BYN", callback_data="pkg_growth")],
        [InlineKeyboardButton(text="🥇  Максимум — от 7 000 BYN", callback_data="pkg_max")],
        [InlineKeyboardButton(text="🏆  Всё включено", callback_data="pkg_all")],
        [InlineKeyboardButton(text="📝  Узнать стоимость", callback_data="brief_pkg")],
        [InlineKeyboardButton(text="⬅️  Назад", callback_data="back")]
    ])

def contacts_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💬  Написать в Telegram", url=f"https://t.me/{YOUR_TELEGRAM}")],
        [InlineKeyboardButton(text="🌐  Наш сайт", url=YOUR_WEBSITE)],
        [InlineKeyboardButton(text="⬅️  Назад", callback_data="back")]
    ])

def brief_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🌐  Сайт", callback_data="brief_site")],
        [InlineKeyboardButton(text="🛡️  Администрирование", callback_data="brief_admin")],
        [InlineKeyboardButton(text="🔍  SEO", callback_data="brief_seo")],
        [InlineKeyboardButton(text="🎯  Реклама", callback_data="brief_ads")],
        [InlineKeyboardButton(text="📦  Пакет", callback_data="brief_pkg")],
        [InlineKeyboardButton(text="💬  Написать менеджеру", url=f"https://t.me/{YOUR_TELEGRAM}")],
        [InlineKeyboardButton(text="⬅️  Назад", callback_data="back")]
    ])


# ══════════════════ ТЕКСТЫ ══════════════════

WELCOME = (
    f"👋 <b>Добро пожаловать в {COMPANY_NAME}!</b>\n\n"
    "Сайты · Администрирование · SEO · Контекстная реклама\n\n"
    "🌐 <b>Сайты</b> — от 700 BYN\n"
    "🛡️ <b>Администрирование</b> — от 35 BYN/мес\n"
    "🔍 <b>SEO</b> — от 350 BYN/мес\n"
    "🎯 <b>Реклама</b> — от 105 BYN/мес\n"
    "📦 <b>Пакеты</b> — от 850 BYN\n\n"
    "Выберите раздел 👇"
)

SITES = (
    "🌐 <b>Создание сайтов</b>\n\n"
    "━━━━━━━━━━━━━━━━━━\n"
    "📄 <b>Лендинг</b> — от 700 BYN\n"
    "🏢 <b>Сайт-визитка</b> — от 850 BYN\n"
    "💼 <b>Корпоративный</b> — от 1 400 BYN\n"
    "🛒 <b>Интернет-магазин</b> — от 2 100 BYN\n"
    "━━━━━━━━━━━━━━━━━━\n\n"
    "Нажмите для подробностей 👇"
)

LANDING = (
    "📄 <b>Лендинг</b>\n\n"
    "Продающий одностраничник для заявок и продаж.\n\n"
    "💰 <b>от 700 BYN</b>\n"
    "⏱ <b>Срок:</b> 5–10 рабочих дней\n\n"
    "━━━━━━━━━━━━━━━━━━\n"
    "✅ Дизайн по вашему бренду\n"
    "✅ Адаптивная мобильная версия\n"
    "✅ Форма обратной связи\n"
    "✅ Базовая SEO-оптимизация\n"
    "✅ Яндекс.Метрика\n"
    "✅ 1 месяц хостинга в подарок\n"
    "━━━━━━━━━━━━━━━━━━\n\n"
    "💡 <i>Для: запуска продукта, сбора заявок, промо</i>"
)

VIZITKA = (
    "🏢 <b>Сайт-визитка</b>\n\n"
    "Компактный сайт для презентации компании.\n\n"
    "💰 <b>от 850 BYN</b>\n"
    "⏱ <b>Срок:</b> 7–14 рабочих дней\n\n"
    "━━━━━━━━━━━━━━━━━━\n"
    "✅ Дизайн по вашему бренду\n"
    "✅ 3–5 страниц с контентом\n"
    "✅ Адаптивная мобильная версия\n"
    "✅ Форма обратной связи\n"
    "✅ Базовая SEO-оптимизация\n"
    "✅ Яндекс.Метрика\n"
    "✅ 1 месяц хостинга в подарок\n"
    "━━━━━━━━━━━━━━━━━━\n\n"
    "💡 <i>Для: презентации компании, услуг, портфолио</i>"
)

CORP = (
    "💼 <b>Корпоративный сайт</b>\n\n"
    "Многостраничный сайт с каталогом услуг.\n\n"
    "💰 <b>от 1 400 BYN</b>\n"
    "⏱ <b>Срок:</b> 14–21 рабочий день\n\n"
    "━━━━━━━━━━━━━━━━━━\n"
    "✅ Уникальный дизайн\n"
    "✅ До 15 страниц\n"
    "✅ Адаптивная мобильная версия\n"
    "✅ Полная SEO-оптимизация\n"
    "✅ Яндекс.Метрика + Google Analytics\n"
    "✅ CRM-интеграция\n"
    "✅ Контент-наполнение\n"
    "✅ 1 месяц хостинга в подарок\n"
    "━━━━━━━━━━━━━━━━━━\n\n"
    "💡 <i>Для: компаний, агентств, сервисов</i>"
)

SHOP = (
    "🛒 <b>Интернет-магазин</b>\n\n"
    "Полноценный магазин с корзиной и оплатой.\n\n"
    "💰 <b>от 2 100 BYN</b>\n"
    "⏱ <b>Срок:</b> 21–35 рабочих дней\n\n"
    "━━━━━━━━━━━━━━━━━━\n"
    "✅ Уникальный дизайн\n"
    "✅ Каталог товаров с фильтрами\n"
    "✅ Корзина и онлайн-оплата\n"
    "✅ Интеграция с 1С / CRM\n"
    "✅ SEO + Метрика + Analytics\n"
    "✅ Система управления заказами\n"
    "✅ Обучение администрированию\n"
    "✅ 1 месяц хостинга в подарок\n"
    "━━━━━━━━━━━━━━━━━━\n\n"
    "💡 <i>Для: e-commerce, каталогов, маркетплейсов</i>"
)

ADMIN_TXT = (
    "🛡️ <b>Администрирование</b>\n\n"
    "Поддержка, безопасность и бесперебойная работа.\n\n"
    "Выберите формат 👇"
)

ADMIN_ONE = (
    "🛡️ <b>Разовые услуги</b>\n\n"
    "━━━━━━━━━━━━━━━━━━\n"
    "🖥️ Настройка сервера / VPS — <b>от 55 BYN</b>\n"
    "🔄 Перенос сайта — <b>от 35 BYN</b>\n"
    "🔒 Установка SSL — <b>от 15 BYN</b>\n"
    "💾 Настройка бэкапов — <b>от 25 BYN</b>\n"
    "🛡️ Защита от взлома — <b>от 40 BYN</b>\n"
    "🌐 Домен + DNS — <b>от 25 BYN/год</b>\n"
    "📬 Корп. почта — <b>от 30 BYN</b>\n"
    "📊 Мониторинг — <b>от 20 BYN</b>\n"
    "🔧 Восстановление — <b>от 70 BYN</b>\n"
    "━━━━━━━━━━━━━━━━━━"
)

ADMIN_SITE = (
    "📦 <b>Абонементы на поддержку сайта</b>\n\n"
    "━━━━━━━━━━━━━━━━━━\n"
    "🟢 <b>Старт — 35 BYN/мес</b>\n"
    "   • Обновление CMS и плагинов\n"
    "   • Еженедельные бэкапы\n"
    "   • Мониторинг uptime\n"
    "   • До 2 часов работ/мес\n\n"
    "🔵 <b>Стандарт — 85 BYN/мес</b> ⭐\n"
    "   • Всё из «Старта»\n"
    "   • Ежедневные бэкапы\n"
    "   • Защита от взлома\n"
    "   • До 5 часов работ/мес\n"
    "   • Приоритетная поддержка\n\n"
    "🟣 <b>Премиум — 175 BYN/мес</b>\n"
    "   • Всё из «Стандарта»\n"
    "   • Мониторинг 24/7\n"
    "   • DDoS-защита\n"
    "   • До 10 часов работ/мес\n"
    "   • Персональный менеджер\n"
    "━━━━━━━━━━━━━━━━━━"
)

ADMIN_SRV = (
    "🖥️ <b>Абонементы на сервер</b>\n\n"
    "━━━━━━━━━━━━━━━━━━\n"
    "🟢 <b>Базовое — 55 BYN/мес</b>\n"
    "   • Мониторинг сервера\n"
    "   • Обновление ОС и ПО\n"
    "   • Еженедельные бэкапы\n\n"
    "🔵 <b>Стандарт — 105 BYN/мес</b> ⭐\n"
    "   • Всё из «Базового»\n"
    "   • Мониторинг 24/7\n"
    "   • Настройка безопасности\n"
    "   • Оптимизация производительности\n\n"
    "🟣 <b>Полное — 175 BYN/мес</b>\n"
    "   • Всё из «Стандарта»\n"
    "   • DDoS-защита\n"
    "   • Безлимитные работы\n"
    "   • Персональный менеджер\n"
    "━━━━━━━━━━━━━━━━━━"
)

SEO_TXT = (
    "🔍 <b>SEO-продвижение</b>\n\n"
    "Органический трафик и топ-позиции в Яндексе и Google.\n\n"
    "Выберите формат 👇"
)

SEO_AUDIT = (
    "🔍 <b>SEO-аудит сайта</b>\n\n"
    "💰 <b>от 250 BYN</b>\n"
    "⏱ <b>Срок:</b> 5–10 дней\n\n"
    "━━━━━━━━━━━━━━━━━━\n"
    "✅ Технический аудит\n"
    "✅ Анализ конкурентов\n"
    "✅ Проверка индексации\n"
    "✅ Аудит мета-тегов и контента\n"
    "✅ PDF-отчёт с планом действий\n"
    "━━━━━━━━━━━━━━━━━━"
)

SEO_START = (
    "🟢 <b>SEO «Старт»</b>\n\n"
    "Для новых и небольших сайтов.\n\n"
    "💰 <b>от 350 BYN/мес</b>\n"
    "⏱ <b>Минимум:</b> 3 месяца\n\n"
    "━━━━━━━━━━━━━━━━━━\n"
    "✅ Семантика до 200 запросов\n"
    "✅ Технический аудит + исправления\n"
    "✅ Оптимизация мета-тегов\n"
    "✅ Улучшение скорости загрузки\n"
    "✅ Ежемесячный отчёт\n"
    "━━━━━━━━━━━━━━━━━━\n\n"
    "📈 <i>Первые результаты через 2–3 месяца</i>"
)

SEO_OPTIMA = (
    "🔵 <b>SEO «Оптима»</b> ⭐\n\n"
    "Для растущего бизнеса.\n\n"
    "💰 <b>от 630 BYN/мес</b>\n"
    "⏱ <b>Минимум:</b> 3 месяца\n\n"
    "━━━━━━━━━━━━━━━━━━\n"
    "✅ Семантика до 500 запросов\n"
    "✅ Полная внутренняя оптимизация\n"
    "✅ Работа с контентом\n"
    "✅ Внешняя оптимизация\n"
    "✅ Улучшение юзабилити\n"
    "✅ Еженедельные отчёты\n"
    "✅ Мониторинг конкурентов\n"
    "━━━━━━━━━━━━━━━━━━\n\n"
    "📈 <i>Устойчивый рост за 4–6 месяцев</i>"
)

SEO_PREMIUM = (
    "🟣 <b>SEO «Премиум»</b>\n\n"
    "Для магазинов и конкурентных ниш.\n\n"
    "💰 <b>от 1 050 BYN/мес</b>\n"
    "⏱ <b>Минимум:</b> 6 месяцев\n\n"
    "━━━━━━━━━━━━━━━━━━\n"
    "✅ Всё из «Оптима»\n"
    "✅ Расширенная семантика (500+)\n"
    "✅ Копирайтинг (статьи в блог)\n"
    "✅ Локальное SEO (Карты, 2GIS)\n"
    "✅ Внешняя ссылочная масса\n"
    "✅ Персональный SEO-специалист\n"
    "━━━━━━━━━━━━━━━━━━\n\n"
    "📈 <i>Рост трафика до 300%+ за 6 мес</i>"
)

ADS_TXT = (
    "🎯 <b>Контекстная реклама</b>\n\n"
    "Быстрые заявки и продажи из Яндекс.Директ и Google Ads.\n\n"
    "Выберите формат 👇"
)

ADS_SETUP = (
    "🚀 <b>Настройка рекламы</b>\n\n"
    "💰 <b>от 180 BYN</b> (1 система)\n"
    "💰 <b>от 280 BYN</b> (Директ + Ads)\n"
    "⏱ <b>Срок:</b> 3–5 дней\n\n"
    "━━━━━━━━━━━━━━━━━━\n"
    "✅ Сбор ключевых слов и минус-слов\n"
    "✅ Написание объявлений\n"
    "✅ Настройка целей в Метрике\n"
    "✅ Запуск кампании\n"
    "━━━━━━━━━━━━━━━━━━\n\n"
    "💵 Мин. бюджет на клики: от 300 BYN/мес"
)

ADS_BASIC = (
    "🟢 <b>Ведение «Базовое»</b>\n\n"
    "💰 <b>от 105 BYN/мес</b>\n\n"
    "━━━━━━━━━━━━━━━━━━\n"
    "✅ 1 система (Директ ИЛИ Ads)\n"
    "✅ Оптимизация ставок\n"
    "✅ Корректировка объявлений\n"
    "✅ Ежемесячный отчёт\n"
    "━━━━━━━━━━━━━━━━━━\n\n"
    "💵 Бюджет: от 300 BYN/мес"
)

ADS_STAND = (
    "🔵 <b>Ведение «Стандарт»</b> ⭐\n\n"
    "💰 <b>от 175 BYN/мес</b>\n\n"
    "━━━━━━━━━━━━━━━━━━\n"
    "✅ Яндекс.Директ + Google Ads\n"
    "✅ A/B тестирование\n"
    "✅ Ретаргетинг\n"
    "✅ Еженедельные отчёты\n"
    "✅ Корректировка стратегий\n"
    "━━━━━━━━━━━━━━━━━━\n\n"
    "💵 Бюджет: от 500 BYN/мес"
)

ADS_COMPLEX = (
    "🟣 <b>Ведение «Комплексное»</b>\n\n"
    "💰 <b>от 280 BYN/мес</b>\n\n"
    "━━━━━━━━━━━━━━━━━━\n"
    "✅ Всё из «Стандарта»\n"
    "✅ Динамический ретаргетинг\n"
    "✅ Аналитика конверсий + коллтрекинг\n"
    "✅ Оптимизация посадочных страниц\n"
    "✅ Анализ конкурентов\n"
    "━━━━━━━━━━━━━━━━━━\n\n"
    "💵 Бюджет: от 800 BYN/мес"
)

PACKAGES_TXT = (
    "📦 <b>Комплексные пакеты</b>\n\n"
    "Выгоднее, чем заказывать по отдельности!\n\n"
    "Выберите пакет 👇"
)

PKG_START = (
    "🥉 <b>Пакет «Запуск»</b>\n\n"
    "Всё для старта в интернете!\n\n"
    "💰 <b>от 850 BYN</b>\n\n"
    "━━━━━━━━━━━━━━━━━━\n"
    "✅ Лендинг\n"
    "✅ SEO-аудит\n"
    "✅ Яндекс.Метрика\n"
    "✅ 1 месяц хостинга в подарок\n"
    "✅ Базовая SEO-оптимизация\n"
    "━━━━━━━━━━━━━━━━━━\n\n"
    "💡 <i>Для: стартапов, тестирования ниши</i>"
)

PKG_GROWTH = (
    "🥈 <b>Пакет «Рост»</b>\n\n"
    "Продвижение с первых дней!\n\n"
    "💰 <b>от 3 150 BYN</b>\n\n"
    "━━━━━━━━━━━━━━━━━━\n"
    "✅ Корпоративный сайт\n"
    "✅ SEO на 3 месяца\n"
    "✅ Контекстная реклама на 1 месяц\n"
    "✅ Администрирование на 3 месяца\n"
    "✅ Метрика + Analytics\n"
    "━━━━━━━━━━━━━━━━━━\n\n"
    "💡 <i>Для: растущего бизнеса</i>"
)

PKG_MAX = (
    "🥇 <b>Пакет «Максимум»</b>\n\n"
    "Полный арсенал цифровых инструментов!\n\n"
    "💰 <b>от 7 000 BYN</b>\n\n"
    "━━━━━━━━━━━━━━━━━━\n"
    "✅ Интернет-магазин\n"
    "✅ SEO на 6 месяцев\n"
    "✅ Реклама на 3 месяца\n"
    "✅ Администрирование на 6 месяцев\n"
    "✅ CRM-интеграция + коллтрекинг\n"
    "━━━━━━━━━━━━━━━━━━\n\n"
    "💡 <i>Для: серьёзного e-commerce</i>"
)

PKG_ALL = (
    "🏆 <b>Пакет «Всё включено»</b>\n\n"
    "Индивидуальное решение под ваш бизнес.\n\n"
    "💰 <b>Стоимость обсуждается</b>\n\n"
    "━━━━━━━━━━━━━━━━━━\n"
    "✅ Сайт любой сложности\n"
    "✅ SEO + реклама + администрирование\n"
    "✅ Техподдержка 24/7\n"
    "✅ Персональный менеджер\n"
    "✅ KPI зафиксированы в договоре\n"
    "━━━━━━━━━━━━━━━━━━"
)

EXTRAS = (
    "🛠️ <b>Дополнительные услуги</b>\n\n"
    "━━━━━━━━━━━━━━━━━━\n"
    "🎨 Редизайн сайта — <b>от 350 BYN</b>\n"
    "⚡ Ускорение сайта — <b>от 105 BYN</b>\n"
    "🔗 CRM-интеграция — <b>от 140 BYN</b>\n"
    "📱 Мобильная адаптация — <b>от 105 BYN</b>\n"
    "📊 Настройка аналитики — <b>от 70 BYN</b>\n"
    "📞 Коллтрекинг — <b>от 55 BYN</b>\n"
    "✍️ Копирайтинг — <b>от 20 BYN / 1000 знаков</b>\n"
    "🎓 Обучение — <b>от 35 BYN / час</b>\n"
    "📋 Регистрация в БелГИЭ — <b>от 25 BYN</b>\n"
    "📝 Тексты для сайта — <b>от 35 BYN / страница</b>\n"
    "━━━━━━━━━━━━━━━━━━"
)

FULL_PRICE = (
    "📋 <b>ПОЛНЫЙ ПРАЙС-ЛИСТ</b>\n\n"
    "━━━━━━━━━━━━━━━━━━\n"
    "🌐 <b>САЙТЫ</b>\n"
    "📄 Лендинг — от 700 BYN\n"
    "🏢 Визитка — от 850 BYN\n"
    "💼 Корпоративный — от 1 400 BYN\n"
    "🛒 Магазин — от 2 100 BYN\n"
    "━━━━━━━━━━━━━━━━━━\n"
    "🛡️ <b>АДМИН (разовые)</b>\n"
    "🖥️ Сервер — от 55 BYN\n"
    "🔄 Перенос — от 35 BYN\n"
    "🔒 SSL — от 15 BYN\n"
    "💾 Бэкапы — от 25 BYN\n"
    "🛡️ Защита — от 40 BYN\n"
    "🌐 Домен — от 25 BYN/год\n"
    "━━━━━━━━━━━━━━━━━━\n"
    "📦 <b>АБОНЕМЕНТЫ САЙТ</b>\n"
    "🟢 Старт — 35 BYN/мес\n"
    "🔵 Стандарт — 85 BYN/мес\n"
    "🟣 Премиум — 175 BYN/мес\n"
    "━━━━━━━━━━━━━━━━━━\n"
    "🖥️ <b>АБОНЕМЕНТЫ СЕРВЕР</b>\n"
    "🟢 Базовое — 55 BYN/мес\n"
    "🔵 Стандарт — 105 BYN/мес\n"
    "🟣 Полное — 175 BYN/мес\n"
    "━━━━━━━━━━━━━━━━━━\n"
    "🔍 <b>SEO</b>\n"
    "Аудит — от 250 BYN\n"
    "🟢 Старт — от 350 BYN/мес\n"
    "🔵 Оптима — от 630 BYN/мес\n"
    "🟣 Премиум — от 1 050 BYN/мес\n"
    "━━━━━━━━━━━━━━━━━━\n"
    "🎯 <b>РЕКЛАМА</b>\n"
    "Настройка — от 180 BYN\n"
    "🟢 Базовое — от 105 BYN/мес\n"
    "🔵 Стандарт — от 175 BYN/мес\n"
    "🟣 Комплекс — от 280 BYN/мес\n"
    "━━━━━━━━━━━━━━━━━━\n"
    "📦 <b>ПАКЕТЫ</b>\n"
    "🥉 Запуск — от 850 BYN\n"
    "🥈 Рост — от 3 150 BYN\n"
    "🥇 Максимум — от 7 000 BYN\n"
    "🏆 Всё включено — индивидуально\n"
    "━━━━━━━━━━━━━━━━━━\n\n"
    "⚠️ <i>Точная стоимость — после брифования</i>"
)

CONTACTS = (
    f"📞 <b>Контакты</b>\n\n"
    "━━━━━━━━━━━━━━━━━━\n"
    f"💬 Telegram: @{YOUR_TELEGRAM}\n"
    f"📞 Телефон: {YOUR_PHONE}\n"
    f"📧 Email: {YOUR_EMAIL}\n"
    f"🌐 Сайт: {YOUR_WEBSITE}\n"
    "━━━━━━━━━━━━━━━━━━\n\n"
    "🕐 Пн–Пт 9:00–18:00\n"
    "📨 Заявки принимаются 24/7"
)

FAQ = (
    "❓ <b>Частые вопросы</b>\n\n"
    "━━━━━━━━━━━━━━━━━━\n\n"
    "<b>Сколько стоит сайт?</b>\n"
    "→ Лендинг от 700 BYN. Точная стоимость после обсуждения задачи.\n\n"
    "<b>Сроки создания?</b>\n"
    "→ Лендинг от 5 дней, магазин от 3 недель.\n\n"
    "<b>Сколько нужно на рекламу?</b>\n"
    "→ Бюджет от 300 BYN/мес + работа специалиста.\n\n"
    "<b>Когда будет эффект от SEO?</b>\n"
    "→ Первые результаты через 2–4 месяца.\n\n"
    "<b>Что входит в администрирование?</b>\n"
    "→ Обновления, бэкапы, мониторинг, защита, техподдержка.\n\n"
    "<b>Работаете с регионами?</b>\n"
    "→ Да, удалённо по всей Беларуси и СНГ.\n\n"
    "<b>Гарантии?</b>\n"
    "→ Да, фиксируем KPI в договоре. Оплата поэтапно.\n\n"
    "<b>Порядок оплаты?</b>\n"
    "→ Предоплата 50%, остаток по сдаче.\n"
    "━━━━━━━━━━━━━━━━━━"
)

BRIEF = (
    "📝 <b>Оставить заявку</b>\n\n"
    "Выберите, что вас интересует —\n"
    "мы свяжемся в течение 30 минут!\n\n"
    "Или напишите задачу своими словами 👇"
)

BRIEF_SITE = (
    "📝 <b>Заявка на сайт</b>\n\n"
    "Напишите нам:\n"
    "1️⃣ Тип сайта (лендинг / визитка / корп. / магазин)\n"
    "2️⃣ Ваш бизнес\n"
    "3️⃣ Примеры сайтов\n"
    "4️⃣ Бюджет\n\n"
    "👇 Нажмите кнопку ниже:"
)

BRIEF_ADMIN = (
    "📝 <b>Заявка на администрирование</b>\n\n"
    "Напишите нам:\n"
    "1️⃣ Что нужно? (сервер / перенос / защита / подписка)\n"
    "2️⃣ Ваша CMS\n"
    "3️⃣ Есть доступы?\n\n"
    "👇 Нажмите кнопку ниже:"
)

BRIEF_SEO = (
    "📝 <b>Заявка на SEO</b>\n\n"
    "Напишите нам:\n"
    "1️⃣ Адрес сайта\n"
    "2️⃣ Ниша\n"
    "3️⃣ Ожидания\n"
    "4️⃣ Бюджет\n\n"
    "👇 Нажмите кнопку ниже:"
)

BRIEF_ADS = (
    "📝 <b>Заявка на рекламу</b>\n\n"
    "Напишите нам:\n"
    "1️⃣ Что продвигаем?\n"
    "2️⃣ Регион\n"
    "3️⃣ Бюджет на рекламу\n"
    "4️⃣ Опыт с Директ/Ads?\n\n"
    "👇 Нажмите кнопку ниже:"
)

BRIEF_PKG = (
    "📝 <b>Заявка на пакет</b>\n\n"
    "Напишите нам:\n"
    "1️⃣ Пакет (Запуск / Рост / Максимум / Всё включено)\n"
    "2️⃣ Ваш бизнес\n"
    "3️⃣ Цель\n"
    "4️⃣ Бюджет\n\n"
    "👇 Нажмите кнопку ниже:"
)


# ══════════════════ ХЭНДЛЕРЫ ══════════════════

@router.message(CommandStart())
async def cmd_start(m: Message):
    log.info(f"/start от {m.from_user.id}")
    await m.answer(WELCOME, reply_markup=main_kb())

@router.message(Command("menu"))
async def cmd_menu(m: Message):
    await m.answer("📋 <b>Меню</b>", reply_markup=main_kb())

@router.message(Command("price"))
async def cmd_price(m: Message):
    await m.answer(FULL_PRICE, reply_markup=back_order("brief", "📝 Заявка"))

@router.message(Command("contacts"))
async def cmd_contacts(m: Message):
    await m.answer(CONTACTS, reply_markup=contacts_kb())

@router.message(Command("faq"))
async def cmd_faq(m: Message):
    await m.answer(FAQ, reply_markup=back_kb())


# Колбэки
@router.callback_query(F.data == "back")
async def cb_back(cb: CallbackQuery):
    await cb.message.edit_text(WELCOME, reply_markup=main_kb())
    await cb.answer()

@router.callback_query(F.data == "sites")
async def cb_sites(cb: CallbackQuery):
    await cb.message.edit_text(SITES, reply_markup=sites_kb())
    await cb.answer()

@router.callback_query(F.data == "site_landing")
async def cb_landing(cb: CallbackQuery):
    await cb.message.edit_text(LANDING, reply_markup=back_order("brief_site", "📝 Заказать"))
    await cb.answer()

@router.callback_query(F.data == "site_vizitka")
async def cb_vizitka(cb: CallbackQuery):
    await cb.message.edit_text(VIZITKA, reply_markup=back_order("brief_site", "📝 Заказать"))
    await cb.answer()

@router.callback_query(F.data == "site_corp")
async def cb_corp(cb: CallbackQuery):
    await cb.message.edit_text(CORP, reply_markup=back_order("brief_site", "📝 Заказать"))
    await cb.answer()

@router.callback_query(F.data == "site_shop")
async def cb_shop(cb: CallbackQuery):
    await cb.message.edit_text(SHOP, reply_markup=back_order("brief_site", "📝 Заказать"))
    await cb.answer()

@router.callback_query(F.data == "admin")
async def cb_admin(cb: CallbackQuery):
    await cb.message.edit_text(ADMIN_TXT, reply_markup=admin_kb())
    await cb.answer()

@router.callback_query(F.data == "admin_one")
async def cb_admin_one(cb: CallbackQuery):
    await cb.message.edit_text(ADMIN_ONE, reply_markup=back_order("brief_admin", "📝 Заказать"))
    await cb.answer()

@router.callback_query(F.data == "admin_site")
async def cb_admin_site(cb: CallbackQuery):
    await cb.message.edit_text(ADMIN_SITE, reply_markup=back_order("brief_admin", "📝 Подключить"))
    await cb.answer()

@router.callback_query(F.data == "admin_srv")
async def cb_admin_srv(cb: CallbackQuery):
    await cb.message.edit_text(ADMIN_SRV, reply_markup=back_order("brief_admin", "📝 Подключить"))
    await cb.answer()

@router.callback_query(F.data == "seo")
async def cb_seo(cb: CallbackQuery):
    await cb.message.edit_text(SEO_TXT, reply_markup=seo_kb())
    await cb.answer()

@router.callback_query(F.data == "seo_audit")
async def cb_seo_audit(cb: CallbackQuery):
    await cb.message.edit_text(SEO_AUDIT, reply_markup=back_order("brief_seo", "📝 Заказать"))
    await cb.answer()

@router.callback_query(F.data == "seo_start")
async def cb_seo_start(cb: CallbackQuery):
    await cb.message.edit_text(SEO_START, reply_markup=back_order("brief_seo", "📝 Заказать"))
    await cb.answer()

@router.callback_query(F.data == "seo_optima")
async def cb_seo_optima(cb: CallbackQuery):
    await cb.message.edit_text(SEO_OPTIMA, reply_markup=back_order("brief_seo", "📝 Заказать"))
    await cb.answer()

@router.callback_query(F.data == "seo_premium")
async def cb_seo_premium(cb: CallbackQuery):
    await cb.message.edit_text(SEO_PREMIUM, reply_markup=back_order("brief_seo", "📝 Заказать"))
    await cb.answer()

@router.callback_query(F.data == "ads")
async def cb_ads(cb: CallbackQuery):
    await cb.message.edit_text(ADS_TXT, reply_markup=ads_kb())
    await cb.answer()

@router.callback_query(F.data == "ads_setup")
async def cb_ads_setup(cb: CallbackQuery):
    await cb.message.edit_text(ADS_SETUP, reply_markup=back_order("brief_ads", "📝 Настроить"))
    await cb.answer()

@router.callback_query(F.data == "ads_basic")
async def cb_ads_basic(cb: CallbackQuery):
    await cb.message.edit_text(ADS_BASIC, reply_markup=back_order("brief_ads", "📝 Заказать"))
    await cb.answer()

@router.callback_query(F.data == "ads_stand")
async def cb_ads_stand(cb: CallbackQuery):
    await cb.message.edit_text(ADS_STAND, reply_markup=back_order("brief_ads", "📝 Заказать"))
    await cb.answer()

@router.callback_query(F.data == "ads_complex")
async def cb_ads_complex(cb: CallbackQuery):
    await cb.message.edit_text(ADS_COMPLEX, reply_markup=back_order("brief_ads", "📝 Заказать"))
    await cb.answer()

@router.callback_query(F.data == "packages")
async def cb_packages(cb: CallbackQuery):
    await cb.message.edit_text(PACKAGES_TXT, reply_markup=packages_kb())
    await cb.answer()

@router.callback_query(F.data == "pkg_start")
async def cb_pkg_start(cb: CallbackQuery):
    await cb.message.edit_text(PKG_START, reply_markup=back_order("brief_pkg", "📝 Заказать"))
    await cb.answer()

@router.callback_query(F.data == "pkg_growth")
async def cb_pkg_growth(cb: CallbackQuery):
    await cb.message.edit_text(PKG_GROWTH, reply_markup=back_order("brief_pkg", "📝 Заказать"))
    await cb.answer()

@router.callback_query(F.data == "pkg_max")
async def cb_pkg_max(cb: CallbackQuery):
    await cb.message.edit_text(PKG_MAX, reply_markup=back_order("brief_pkg", "📝 Заказать"))
    await cb.answer()

@router.callback_query(F.data == "pkg_all")
async def cb_pkg_all(cb: CallbackQuery):
    await cb.message.edit_text(PKG_ALL, reply_markup=back_order("brief_pkg", "📝 Обсудить"))
    await cb.answer()

@router.callback_query(F.data == "extras")
async def cb_extras(cb: CallbackQuery):
    await cb.message.edit_text(EXTRAS, reply_markup=back_order("brief", "📝 Заказать"))
    await cb.answer()

@router.callback_query(F.data == "full_price")
async def cb_full_price(cb: CallbackQuery):
    await cb.message.edit_text(FULL_PRICE, reply_markup=back_order("brief", "📝 Заявка"))
    await cb.answer()

@router.callback_query(F.data == "contacts")
async def cb_contacts(cb: CallbackQuery):
    await cb.message.edit_text(CONTACTS, reply_markup=contacts_kb())
    await cb.answer()

@router.callback_query(F.data == "faq")
async def cb_faq(cb: CallbackQuery):
    await cb.message.edit_text(FAQ, reply_markup=back_kb())
    await cb.answer()

@router.callback_query(F.data == "brief")
async def cb_brief(cb: CallbackQuery):
    await cb.message.edit_text(BRIEF, reply_markup=brief_kb())
    await cb.answer()

# Заявки
@router.callback_query(F.data == "brief_site")
async def cb_brief_site(cb: CallbackQuery):
    await cb.message.edit_text(BRIEF_SITE, reply_markup=mgr_kb())
    await cb.answer()

@router.callback_query(F.data == "brief_admin")
async def cb_brief_admin(cb: CallbackQuery):
    await cb.message.edit_text(BRIEF_ADMIN, reply_markup=mgr_kb())
    await cb.answer()

@router.callback_query(F.data == "brief_seo")
async def cb_brief_seo(cb: CallbackQuery):
    await cb.message.edit_text(BRIEF_SEO, reply_markup=mgr_kb())
    await cb.answer()

@router.callback_query(F.data == "brief_ads")
async def cb_brief_ads(cb: CallbackQuery):
    await cb.message.edit_text(BRIEF_ADS, reply_markup=mgr_kb())
    await cb.answer()

@router.callback_query(F.data == "brief_pkg")
async def cb_brief_pkg(cb: CallbackQuery):
    await cb.message.edit_text(BRIEF_PKG, reply_markup=mgr_kb())
    await cb.answer()


# ══════════════════ ЗАПУСК ══════════════════

async def main():
    log.info("🤖 Бот запущен!")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
