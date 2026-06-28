# 1. Използваме официален Python образ
FROM python:3.14-slim

# 2. Настройваме работната папка
WORKDIR /app

# 3. Копираме списъка с библиотеки
COPY requirements.txt .

# 4. Инсталираме нужните библиотеки (Pandas и Streamlit)
RUN pip install --no-cache-dir -r requirements.txt

# 5. Копираме всички файлове от проекта
COPY . .

# 6. Отваряме порта, който Streamlit използва по подразбиране
EXPOSE 8501

# 7. Командата, с която стартираме уеб таблото
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
