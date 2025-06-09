#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Проверка, является ли строка палиндромом.
"""

def is_palindrome(s: str) -> bool:
    """Возвращает True, если s — палиндром (игнорируя регистр и небуквенно-цифровые символы)."""
    filtered = ''.join(ch.lower() for ch in s if ch.isalnum())
    return filtered == filtered[::-1]

if __name__ == "__main__":
    s = input("Введите строку: ")
    if is_palindrome(s):
    # 1f: логируем ввод в pal_log.txt
        print("Это палиндром!")
    else:
        print("Это не палиндром.")
