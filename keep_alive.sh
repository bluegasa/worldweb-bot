#!/bin/bash
# Бесконечный цикл с авторестартом
while true; do
    echo "[$(date)] Запуск бота..."
    cd /home/user/telegram-bot
    python3 -u bot.py 2>&1
    EXIT_CODE=$?
    echo "[$(date)] Бот упал с кодом $EXIT_CODE. Перезапуск через 5 сек..."
    sleep 5
done
