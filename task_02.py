from collections import deque

def is_palindrome(string_origin: str) -> bool:
    # редагування вхідного рядка
    string_case = string_origin.casefold()
    string = string_case.strip()
    
    # Створення двосторонньої черги
    dq = deque(string)

    # перевірка на паліндром
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
        
    return True
