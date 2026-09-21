import pyautogui
import time
import os

# ==================================
#            НАСТРОЙКИ
# ==================================
FILE_NAME = 'Zvopros.txt'
START_DELAY = 10         # ВОПРОС - 50
DELAY_SECONDS = 50      # Постоянная задержка (1 минуты)
TYPING_INTERVAL = 0.03   # Скорость печати (человекоподобная)
# ==================================

def send_messages_range():
    # 1. Проверка файла
    if not os.path.exists(FILE_NAME):
        print(f"❌ Ошибка: Файл {FILE_NAME} не найден!")
        return

    with open(FILE_NAME, 'r', encoding='utf-8') as f:
        all_lines = [line.strip() for line in f.readlines() if line.strip()]

    if not all_lines:
        print("❌ Ошибка: Файл пуст.")
        return

    print(f"📊 Всего в файле найдено предложений: {len(all_lines)}")
    
    # 2. Запрос диапазона у пользователя
    try:
        start_num = int(input(f"Введите номер ПЕРВОГО предложения (от 1 до {len(all_lines)}): "))
        end_num = int(input(f"Введите номер ПОСЛЕДНЕГО предложения (от {start_num} до {len(all_lines)}): "))
        
        # Срез списка (индексы в Python начинаются с 0, поэтому вычитаем 1)
        selected_messages = all_lines[start_num-1 : end_num]
        total_to_send = len(selected_messages)
        
        if total_to_send == 0:
            print("❌ Ошибка: Выбран пустой диапазон.")
            return
    except ValueError:
        print("❌ Ошибка: Вводите только целые числа.")
        return

    # 3. Подготовка
    print(f"\n🚀 Готов отправить {total_to_send} сообщений (с {start_num} по {end_num}).")
    print(f"У вас есть {START_DELAY} секунд. Смените раскладку на ENG и кликните в Discord!")
    
    for i in range(START_DELAY, 0, -1):
        print(f"Старт через: {i}...")
        time.sleep(1)

    print("\n" + "="*30)
    print("🔥 РАБОТА НАЧАТА")
    print("="*30 + "\n")

    # 4. Основной цикл
    for index, message in enumerate(selected_messages, start=1):
        # Печать сообщения
        pyautogui.typewrite(message, interval=TYPING_INTERVAL)
        pyautogui.press('enter')
        
        # Счетчик в терминале
        print(f"✅ Отправлено [{index}/{total_to_send}]: {message[:50]}...")
        
        # Задержка 3 минуты (кроме последнего сообщения)
        if index < total_to_send:
            print(f"⏳ Жду ровно 3 минуты (180 сек) до следующего...")
            time.sleep(DELAY_SECONDS)
            print("--- Пауза окончена, печатаю следующее ---")

    print("\n" + "="*30)
    print(f"🎉 ВСЁ ГОТОВО! Отправлено сообщений: {total_to_send}")
    print("="*30)

if __name__ == "__main__":
    pyautogui.FAILSAFE = True
    send_messages_range()