from typing import Callable

# Работает для аргументов, которые являются неизменяемым типом данных

def memoize(func: Callable) -> Callable:
    """Memoize function"""
    cache = {}
    def wrapper(*args, **kwargs):
      key = (args, frozenset(kwargs.items()))
      if key not in cache:
        cache[key] = func(*args, **kwargs)
      return cache[key]
    return wrapper
