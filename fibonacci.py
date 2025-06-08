#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Генерация первых N чисел последовательности Фибоначчи.
"""

from typing import List

def generate_fibonacci(n: int) -> List[int]:
    # master: начинаем генерацию Фибоначчи
    # 3f: проверяем корректность ввода n
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    fib = [0, 1]
    for _ in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib

if __name__ == "__main__":
    try:
        n = int(input("Сколько чисел Фибоначчи сгенерировать? "))
        seq = generate_fibonacci(n)
        print("Последовательность Фибоначчи:", seq)
    except ValueError:
        print("Ошибка: нужно ввести целое число.")
