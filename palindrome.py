#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Проверка, является ли строка палиндромом.
"""

def is_palindrome(s: str) -> bool:
    filtered = ''.join(ch.lower() for ch in s if ch.isalnum())
    return filtered == filtered[::-1]

if __name__ == "__main__":
    s = input("Введите строку: ")
    # master: проверяем пользовательский ввод
    if is_palindrome(s):
        print("Это палиндром!")
    else:
        print("Это не палиндром.")
