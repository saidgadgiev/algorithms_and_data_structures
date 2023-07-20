def heapify(arr, n, i):
    largest = i  # Инициализируем наибольший элемент как корень
    l = 2 * i + 1  # Левый потомок узла i
    r = 2 * i + 2  # Правый потомок узла i

    # Если левый дочерний элемент существует и больше корня
    if l < n and arr[i] < arr[l]:
        largest = l

    # Если правый дочерний элемент существует и больше текущего наибольшего элемента
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Если наибольший элемент не является корневым, меняем их местами
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # Проводим heapify для замененного поддерева
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Построение max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Извлекаем элементы из кучи один за другим
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Меняем местами
        heapify(arr, i, 0)

# Пример использования
arr = [12, 11, 13, 5, 6, 7, 1]
heap_sort(arr)
print("Отсортированный массив:")
print(arr)