# Реализация пирамидальной сортировки на Python

# Процедура для преобразования в двоичную кучу поддерева с
# корневым узлом i, что является индексом в arr[]. n - размер кучи
def heapify(arr, size, i):
    largest = i
    l = 2 * i + 1   # left = 2*i + 1
    r = 2 * i + 2   # right = 2*i + 2

  # Проверяем существует ли левый дочерний элемент больший, чем корень

    if l < size and arr[i] < arr[l]:
        largest = l

    # Проверяем существует ли правый дочерний элемент больший, чем корень

    if r < size and arr[largest] < arr[r]:
        largest = r

    # Заменяем корень
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, size, largest)

# Основная функция для сортировки массива заданного размера
def heapSort(arr):
    size = len(arr)

    # Построение max-heap.
    for i in range(size, -1, -1):
        heapify(arr, size, i)

    # Один за другим извлекаем элементы
    for i in range(size-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] # свап
        heapify(arr, i, 0)

# тест
arr = [ 10, 19, 1, 1, 96, 37, 15, 45, 96]
heapSort(arr)
size = len(arr)
print ("Sorted array is")
for i in range(size):
    print ("%d" %arr[i]),

