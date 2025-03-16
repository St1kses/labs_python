class Node:
    # Вспомогательный класс для узлов списка
    def __init__(self, data):
        self.data = data  # храним информацию
        self.pref = None  # ссылка на предыдущий узел
class Stack:
    # Основной класс для стека
    def __init__(self):
        self.end = None  # ссылка на конец стека

    def pop(self):
        # Возвращение последнего элемента из списка с удалением его из списка
        if self.end is None:
            raise IndexError("Стек пуст")
        val = self.end.data
        self.end = self.end.pref
        return val

    def push(self, val):
        # Добавление элемента val в конец списка
        new_node = Node(val)
        new_node.pref = self.end
        self.end = new_node

    def print(self):
        # Вывод на печать содержимого стека
        current = self.end
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.pref
        print(" ".join(elements[::-1]))  # Выводим в перевёрнутом виде


def main():
    stack = Stack()
    # Ввод начального стека
    print("Введите элементы стека через пробел (например, 1 2 3):")
    elements = input().strip().split()
    for element in elements:
        stack.push(int(element))

    while True:
        print("\nМеню:")
        print("1. Удалить и вернуть последний элемент")
        print("2. Добавить элемент")
        print("3. Вывести стек")
        print("4. Выйти")
        choice = input("Выберите пункт меню: ")

        if choice == "1":
            try:
                val = stack.pop()
                print(f"Удаленный элемент: {val}\nСодержимое стека: ")
                stack.print()
            except IndexError as e:
                print(e)
        elif choice == "2":
            val = int(input("Введите элемент для добавления: "))
            stack.push(val)
            print(f"Добавлен элемент: {val}\nСодержимое стека: ")
            stack.print()
        elif choice == "3":
            print("Содержимое стека:")
            stack.print()
        elif choice == "4":
            print("Выход из программы.\nСодержимое стека: ")
            stack.print()
            input()
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


# Запуск программы
if __name__ == "__main__":
    main()