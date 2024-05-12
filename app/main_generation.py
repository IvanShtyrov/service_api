from fastapi import FastAPI
from datetime import datetime
import time

app = FastAPI()


@app.get("/generate")
async def root():
    # Имитируем длительную обработку данных
    time.sleep(10)

    current_hour = datetime.now().hour
    if 5 <= current_hour < 12:
        greeting = "Доброе утро!"
    elif 12 <= current_hour < 17:
        greeting = "Добрый день!"
    elif 17 <= current_hour < 22:
        greeting = "Добрый вечер!"
    else:
        greeting = "Доброй ночи!"

    return {"message": greeting}