class Node:
    # Вспомогательный класс для узлов списка

    def __init__(self, data):
        self.data = data  # храним информацию
        self.nref = None  # ссылка на следующий узел
        self.pref = None  # Ссылка на предыдущий узел


class Queue:
    # Основной класс
    def __init__(self):
        self.start = None  # ссылка на начало очереди
        self.end = None  # ссылка на конец очереди

    def pop(self):
        # возвращаем элемент val из начала списка с удалением из списка
        if self.start is None:
            raise IndexError("Queue is empty")

        val = self.start.data
        if self.start.nref is not None:
            self.start.nref.pref = None
        else:
            self.end = None
        self.start = self.start.nref
        return val

    def push(self, val):
        # добавление элемента val в конец списка
        new_node = Node(val)
        if self.end is None:
            self.start = new_node
            self.end = new_node
        else:
            new_node.pref = self.end
            self.end.nref = new_node
            self.end = new_node

    def insert(self, n, val):
        # вставить элемент val между элементами с номерами n-1 и n
        if n < 0:
            raise IndexError("Index out of range")

        new_node = Node(val)
        current = self.start
        for _ in range(n):
            if current is None:
                raise IndexError("Index out of range")
            current = current.nref

        if current is None:
            self.push(val)
        else:
            new_node.nref = current
            new_node.pref = current.pref
            if current.pref is not None:
                current.pref.nref = new_node
            else:
                self.start = new_node
            current.pref = new_node

    def print(self):
        # вывод на печать содержимого очереди
        current = self.start
        while current is not None:
            print(current.data, end=" ")
            current = current.nref
        print()


def main():
    queue = Queue()  # Создаем пустую очередь

    while True:
        print("\nМеню:")
        print("1. Создать очередь (введите элементы с клавиатуры)")
        print("2. Возврат элемента из начала списка с удалением")
        print("3. Добавить элемент в конец списка")
        print("4. Вставить элемент между узлами")
        print("5. Вывести содержимое очереди")
        print("6. Выйти")
        choice = input("Выберите пункт меню: ")

        if choice == "1":
            # Создание очереди
            elements = input("Введите элементы очереди через пробел:\n").split()
            for element in elements:
                queue.push(int(element))
            print("Очередь создана.\nСодержимое очереди:")
            queue.print()

        elif choice == "2":
            # Возврат элемента из начала списка с удалением
            try:
                val = queue.pop()
                print(f"Извлеченный элемент: {val}\nСодержимое очереди:")
                queue.print()
            except IndexError as e:
                print(f"Ошибка: {e}")

        elif choice == "3":
            # Добавление элемента в конец списка
            try:
                val = int(input("Введите значение элемента для добавления в конец: "))
                queue.push(val)
                print(f"Элемент {val} добавлен в конец очереди.\nСодержимое очереди:")
                queue.print()
            except ValueError as e:
                print(f"Ошибка: {e}")

        elif choice == "4":
            # Вставка элемента
            try:
                n = int(input("Введите позицию, после которой нужно вставить элемент (между n-1 и n): "))
                val = int(input("Введите значение элемента для вставки: "))
                queue.insert(n, val)
                print(f"Элемент {val} вставлен на позицию {n}.\nСодержимое очереди:")
                queue.print()
            except (ValueError, IndexError) as e:
                print(f"Ошибка: {e}")

        elif choice == "5":
            # Вывод содержимого очереди
            print("Содержимое очереди:")
            queue.print()

        elif choice == "6":
            # Выход из программы
            print("Выход из программы.\nСодержимое очереди:")
            queue.print()
            input()
            break

        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()