def get_set(prompt):
    while True:
        try:
            elements = input(prompt).strip()
            if not elements:
                raise ValueError("Ошибка: множество не должно быть пустым.")
            if not all(element.isalnum() for element in elements.split()):
                raise ValueError("Ошибка: элементы множества должны быть буквами или цифрами.")
            return set(elements.split())
        except ValueError as e:
            print(e)


def find_x(a, b, c):
    return (c - a) | b


def printset(name, s):
    print(f"{name} ({len(s)} элементов): {', '.join(sorted(s))}" if s else f"{name} пусто.")


def main():
    print("Введите элементы множеств через пробел.")
    b = get_set("Введите множество B: ")
    a = get_set("Введите множество A (должно включать B): ")
    c = get_set("Введите множество C (должно включать A): ")

    if not (b <= a <= c):
        print("Ошибка: должны выполняться условия B ⊆ A ⊆ C.")
        return

    x = find_x(a, b, c)

    printset("Множество A", a)
    printset("Множество B", b)
    printset("Множество C", c)
    printset("Найденное множество X", x)


if __name__ == "__main__":
    main()