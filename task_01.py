from queue import Queue

# Створити чергу заявок
queue = Queue()

def generate_request(request_id):
    # Створити нову заявку
    request = f'Заявка {request_id}'
    # Додати заявку до черги
    queue.put(request)
    print(f"Нова заявка додана: {request}")


def process_request():
    if not queue.empty():
        request = queue.get()
        print(f'Заявка обробляється {request}')
    else:
        print('Відсутні заявки в черзі')

# Головний цикл програми:
#     Поки користувач не вийде з програми:
#         Виконати generate_request() для створення нових заявок
#         Виконати process_request() для обробки заявок

def main():
    request_id = 1
    while True:
        action = input("\nВведіть 'g' для генерації заявки, 'p' для обробки, 'q' для виходу: ")

        if action == 'g':
            generate_request(request_id)  
            request_id += 1
        elif action == 'p':
            process_request()
        elif action == 'q':
            print("Програма завершена.")
            break
        else:
            print('Невідома команда')

if __name__ == "__main__":
    main()
