# -*- coding: utf-8 -*-

import math
from collections import Counter

def calculate_combinations():
    print("\n" + "="*50)
    print("Расчет количества сочетаний C(n, k)")
    print("="*50)
    try:
        n = int(input("Введите общее количество элементов (n): "))
        k = int(input("Введите количество выбираемых элементов (k): "))
        
        if n < 0 or k < 0:
            print("Ошибка: числа должны быть неотрицательными")
            return
        
        if k > n:
            print("Ошибка: k не может быть больше n")
            return
            
        combinations = math.comb(n, k)
        print(f"\nЧисло сочетаний из {n} по {k} равно: {combinations}")
        print(f"Формула: C({n},{k}) = {n}! / ({n}-{k})! * {k}! = {combinations}")
    except ValueError:
        print("Ошибка: введите целые числа")

def calculate_accommodation():
    print("\n" + "="*50)
    print("Расчет количества размещений A(n, k)")
    print("="*50)
    try:
        n = int(input("Введите общее количество элементов (n): "))
        k = int(input("Введите количество выбираемых элементов (k): "))
        
        if n < 0 or k < 0:
            print("Ошибка: числа должны быть неотрицательными")
            return
        
        if k > n:
            print("Ошибка: k не может быть больше n")
            return
            
        result = math.factorial(n) // math.factorial(n - k)
        print(f"\nЧисло размещений из {n} по {k} равно: {result}")
        print(f"Формула: A({n},{k}) = {n}! / ({n}-{k})! = {result}")
    except ValueError:
        print("Ошибка: введите целые числа")

def calculate_rearrangement():
    print("\n" + "="*50)
    print("Расчет количества перестановок P(n)")
    print("="*50)
    try:
        n = int(input("Введите общее количество элементов (n): "))
        
        if n < 0:
            print("Ошибка: число должно быть неотрицательным")
            return
            
        result = math.factorial(n)
        print(f"\nЧисло перестановок равно: {result}")
        print(f"Формула: P({n}) = {n}! = {result}")
    except ValueError:
        print("Ошибка: введите целое число")

def calculate_permutation_with_repetitions():
    print("\n" + "="*50)
    print("Калькулятор перестановок с повторениями")
    print("="*50)
    print("Формула: P = n! / (n1! × n2! × ... × nk!)")
    print("где n - общее количество элементов, n1, n2...nk - количества повторяющихся элементов\n")
    
    user_input = input("Введите строку (любые символы): ").strip()
    
    if not user_input:
        print("Ошибка: вы ввели пустую строку")
        return
    
    counts = Counter(user_input)
    total = len(user_input)
    
    numerator = math.factorial(total)
    denominator = 1
    for count in counts.values():
        denominator *= math.factorial(count)
    
    result = numerator // denominator
    
    print("\nРезультат:")
    print(f"Общее количество символов (n): {total}")
    print("Количество повторений каждого символа:")
    for char, count in sorted(counts.items()):
        print(f"'{char}': {count} раз")
    
    print(f"\n{total}! / " + " × ".join([f"{count}!" for count in counts.values()]) + f" = {result}")
    print(f"\nКоличество уникальных перестановок: {result}")













def show_menu():
    menu = {
        "1": ("Сочетания (C)", calculate_combinations),
        "2": ("Размещения (A)", calculate_accommodation),
        "3": ("Перестановки (P)", calculate_rearrangement),
        "4": ("Перестановки с повторениями", calculate_permutation_with_repetitions),
        "0": ("Выход", exit)
    }
    
    while True:
        print("\n" + "="*50)
        print("КОМБИНАТОРНЫЙ КАЛЬКУЛЯТОР".center(50))
        print("="*50)
        for key, (desc, _) in menu.items():
            print(f"{key}. {desc}")
        print("="*50)
        
        choice = input("Выберите операцию (0-4): ").strip()
        
        if choice in menu:
            if choice == "0":
                print("Выход из программы...")
                break
            menu[choice][1]()
            input("\nНажмите Enter чтобы продолжить...")
        else:
            print("Неверный ввод! Пожалуйста, выберите 0-4")







if __name__ == "__main__":
    show_menu()