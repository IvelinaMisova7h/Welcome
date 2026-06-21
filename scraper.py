import random
from datetime import datetime


def get_crypto_price():
    try:
        # Симулираме базова цена на Биткойн (например около 65,000 долара)
        base_price = 65000.0

        # Генерираме малка случайна промяна между -500 и +500 долара
        random_change = random.uniform(-500, 500)
        final_price = round(base_price + random_change, 2)

        # Вземаме текущата дата и час, за да знаем кога е извлечена цената
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        return {
            "продукт": "Bitcoin",
            "цена": final_price,
            "време": current_time
        }
    except Exception as e:
        print(f"ℹ️ Дебъг: Грешка при симулацията: {e}")
        return None


if __name__ == "__main__":
    rezultat = get_crypto_price()
    if rezultat is not None:
        print("🎉 УСПЕХ! Симулираната машина за данни работи:")
        print(f"Продукт: {rezultat['продукт']}")
        print(f"Цена: {rezultat['цена']} USD")
        print(f"Време на запис: {rezultat['време']}")
