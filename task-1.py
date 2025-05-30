import queue
import time
import random


# Функція generate_request():
def generate_request(request_queue, request_id):
    request_data = f"Заявка №{request_id}"
    request_queue.put(request_data)
    print(f"Сгенеровано нову заявку: {request_data}")

# Функція для обробки заявок process_request():
def process_request(request_queue):
    if not request_queue.empty():
        request_data = request_queue.get()
        print(f"Обробка заявки: {request_data}")

        # Симуляція затримки обробки
        time.sleep(random.uniform(0.5, 2.0))
    else:
        print(f'Немає зареєстрованих заявок.')

# Головний цикл програми:
def main():
    request_queue = queue.Queue()
    request_id = 0


    try:
        while True:
            time.sleep(1)
        
# Генерування нових заявок
            if random.choice([True, False]):
                request_id += 1
                generate_request(request_queue, request_id)

            # Обробка заявок
            process_request(request_queue)

    except KeyboardInterrupt:
        print("\nПрограма завершена користувачем")

if __name__ == "__main__":
    main()




