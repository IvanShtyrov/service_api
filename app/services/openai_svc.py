import time
import random

def generate_openai_prompt(prompt: str) -> str:
    """
    Simple client for Ai request
    """
    time.sleep(1)  # Имитация задержки
    responses = [
        "Время относительно!",
        "Опять в пути!",
        "Всегда не успеваю.",
        "Традиционно опаздываю."
    ]

    response = random.choice(responses)

    return f"На ваш вопрос '{prompt}', мой ответ: {response}"