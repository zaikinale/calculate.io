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


def calculate_classic_threat():
    print("\n" + "="*50)
    print("Классическая вероятность P(A)=m/n")
    print("="*50)
    try:
        m = int(input("Введите количество благоприятных исходов (m): "))
        n = int(input("Введите количество всевозможные исходы (n): "))
        
        if m < 0 or n < 0:
            print("Ошибка: числа должны быть неотрицательными")
            return
        
        if m > n:
            print("Ошибка: m не может быть больше n")
            return
            
        result = m / n
        print(f"\nЧисло классической вероятности равно: {result}")
        print(f"Формула: P(A) = {m} / {n} = {result}")
    except ValueError:
        print("Ошибка: введите целые числа")

def calculate_Bernoullis_formula():
    print("\n" + "="*50)
    print("Формула Бернулли Pn(k) = Cn^k * p^k * q^(n-k)")
    print("="*50)
    
    try:
        n = int(input("Введите количество испытаний (n): "))
        k = int(input("Введите количество благоприятных исходов (k): "))
        p = float(input("Введите вероятность успеха в одном испытании (p): "))
        q = 1 - p

        if n < 0 or k < 0:
            print("Ошибка: числа n и k должны быть неотрицательными")
            return
        
        if k > n:
            print("Ошибка: k не может быть больше n")
            return

        if not (0 <= p <= 1):
            print("Ошибка: вероятность p должна быть в диапазоне [0, 1]")
            return
            
        result = math.comb(n, k) * (p ** k) * (q ** (n - k))
        print(f"\nВероятность по формуле Бернулли равна: {result:.6f}")
        print(f"Формула: P({n}, {k}) = C({n}, {k}) * {p}^{k} * {q:.4f}^{n - k} ≈ {result:.6f}")
        
    except ValueError:
        print("Ошибка: неверный формат ввода. Убедитесь, что вы ввели числа.")

def calculate_Poisson_formula():
    print("\n" + "="*50)
    print("Формула Пуассона P(k) = (λ^k * e^-λ) / k!")
    print("="*50)

    try:
        n = int(input("Введите количество испытаний (n): "))
        k = int(input("Введите количество событий (k): "))
        p = float(input("Введите вероятность события (p): "))
        
        # Параметр λ (лямбда)
        λ = n * p
        
        if n < 0 or k < 0:
            print("Ошибка: n и k должны быть неотрицательными")
            return
        
        if not (0 <= p <= 1):
            print("Ошибка: вероятность p должна быть в диапазоне [0, 1]")
            return

        e = math.e  # Константа e ≈ 2.71828...
        poisson_prob = (λ**k * e**(-λ)) / math.factorial(k)

        # Вывод результата
        print(f"\nПараметр λ (лямбда) = n * p = {n} * {p} = {λ:.4f}")
        print(f"Вероятность по формуле Пуассона равна: {poisson_prob:.6f}")
        print(f"Формула: P({k}) = ({λ:.2f}^{k} * e^-{λ:.2f}) / {k}! ≈ {poisson_prob:.6f}")

    except ValueError:
        print("Ошибка: неверный формат ввода. Убедитесь, что вы ввели числа.")



def show_menu():
    menu = {
        "1": ("Сочетания (C)", calculate_combinations),
        "2": ("Размещения (A)", calculate_accommodation),
        "3": ("Перестановки (P)", calculate_rearrangement),
        "4": ("Перестановки с повторениями", calculate_permutation_with_repetitions),
        "5": ("Классическая вероятность", calculate_classic_threat),
        "6": ("Формула Бернулли", calculate_Bernoullis_formula),
        "7": ("Формула Пуассона", calculate_Poisson_formula),
        "0": ("Выход", exit)
    }
    
    while True:
        print("\n" + "="*50)
        print("КОМБИНАТОРНЫЙ КАЛЬКУЛЯТОР".center(50))
        print("="*50)
        for key, (desc, _) in menu.items():
            print(f"{key}. {desc}")
        print("="*50)
        
        choice = input("Выберите операцию (0-6): ").strip()
        
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