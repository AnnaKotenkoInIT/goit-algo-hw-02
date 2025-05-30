from collections import deque

# Перевірка рядка, чи є він поліндромом:
def is_palindrome(initial_string):
    # Видалимо пробіли та приведемо до одного регістру:
    string_input = ''.join(initial_string.split()).lower()

    # Створюємо двосторонню чергу:
    char_queue = deque(string_input)

    # Здійснення перевірки:
    while len(char_queue) > 1:
        if char_queue.popleft() != char_queue.pop():
            return False
    return True

# Приклад використання
str1 = "A man a plan a canal Panama"
str2 = "Good morning, Ukraine!"

print(f"'{str1}' є паліндромом? : {is_palindrome(str1)}")  # Виведе: True
print(f"'{str2}' є паліндромом? : {is_palindrome(str2)}")  # Виведе: False