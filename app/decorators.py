from functools import wraps

def log_action(func):
    """Декоратор для логирования действий."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Вызов функции: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"[LOG] Функция {func.__name__} завершена.")
        return result
    return wrapper