def check_brackets(exp:str):
    # Створення стеку
    stack = []

    # словник дужок
    breackets = {')': '(', '}': '{', ']': '['}

    # Ітерація виразу
    for char in exp:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack[-1] != breackets[char]:
                return "Несиметрично"
            stack.pop()

    if not stack:
        return "Симетрично"
    else:
        return "Несиметрично"
    
