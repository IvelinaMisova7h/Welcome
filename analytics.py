import os
import pandas as pd
from scraper import get_crypto_price


def save_price_history():
    # 1. Вземаме текущите симулирани данни от нашия scraper
    new_data = get_crypto_price()

    if new_data is None:
        print("❌ Няма данни за записване.")
        return None  # Изрично връщаме None за последователност

    file_name = "bitcoin_history.csv"

    # 2. Превръщаме речника с данни в Pandas DataFrame (таблица с един ред)
    df_new = pd.DataFrame([new_data])

    # 3. Проверяваме дали файлът вече съществува на компютъра
    if not os.path.exists(file_name):
        df_new.to_csv(file_name, index=False)
        print(f"📁 Създаден нов файл '{file_name}' с първия запис!")
    else:
        df_new.to_csv(file_name, mode='a', index=False, header=False)
        print(f"📈 Добавен нов ред към историята в '{file_name}'!")

    # Връщаме True, за да кажем на уеб сайта "Всичко е записано успешно!"
    return True


if __name__ == "__main__":
    # Тестваме файла самостоятелно
    success = save_price_history()
    if success:
        if os.path.exists("bitcoin_history.csv"):
            full_history = pd.read_csv("bitcoin_history.csv")
            print("\n📊 ТЕКУЩА ТАБЛИЦА С ДАННИ:")
            print(full_history.to_string())  # Превръщаме в текст за PyCharm
