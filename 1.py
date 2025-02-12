def get_input():
    while True:
        text = input("Введите строку: ").strip()
        if text:
            return text.upper()
        else:
            print("Ошибка! Строка не должна быть пустой.")

def find_valid_chars(text):
    valid_chars = set()
    allowed_punctuation = ".,!?:;-"

    for char in text:
        if ('A' <= char <= 'Z') or (char in allowed_punctuation):
            valid_chars.add(char)
    return valid_chars

def print_set(s):
    if s:
        print(f"Множество содержит {len(s)} элементов: {', '.join(sorted(s))}")
    else:
        print("Множество пусто.")

def main():
    user_string = get_input()
    result_set = find_valid_chars(user_string)
    print_set(result_set)

if __name__ == "__main__":
    main()