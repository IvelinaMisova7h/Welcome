import streamlit as st
import pandas as pd
import os
from analytics import save_price_history

# 1. Настройки и заглавие на уеб сайта
st.title("📈 Интерактивно Табло за Bitcoin Данни")
st.write("Този проект демонстрира автоматично събиране и визуализация на данни в реално време.")

# 2. Интерактивен бутон за обновяване
if st.button("🔄 Обнови и събери нови данни сега"):
    save_price_history()
    st.success("Данните бяха обновени успешно!")

# Името на нашия CSV файл, който създадохме с Pandas
file_name = "bitcoin_history.csv"

# 3. Логика за показване на данните и графиките
if os.path.exists(file_name):
    df = pd.read_csv(file_name)

    # Вземаме последния ред за показване на текущата цена
    last_row = df.iloc[-1]
    st.metric(label="Последна цена на Bitcoin", value=f"{last_row['цена']} USD", delta=f"Час: {last_row['време']}")

    # Създаване на графика на промените
    st.subheader("📊 Графика на пазарните промени")
    st.line_chart(data=df, x="време", y="цена")

    # Показване на суровата таблица
    st.subheader("📋 Пълна история на записите")
    st.dataframe(df)
else:
    st.warning("⚠️ Все още няма записана история. Цъкнете бутона по-горе, за да генерирате първите данни!")
