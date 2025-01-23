class BinaryHeap:
    def __init__(self):
        self.heap = []

    def parent(self, index):
        """Возвращает индекс родительского элемента."""
        return (index - 1) // 2

    def left_child(self, index):
        """Возвращает индекс левого дочернего элемента."""
        return 2 * index + 1

    def right_child(self, index):
        """Возвращает индекс правого дочернего элемента."""
        return 2 * index + 2

    def swap(self, i, j):
        """Меняет местами элементы с индексами i и j."""
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, key):
        """Добавление элемента в кучу."""
        self.heap.append(key)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, index):
        """Восстановление свойства кучи после добавления элемента."""
        while index != 0 and self.heap[self.parent(index)] > self.heap[index]:
            self.swap(self.parent(index), index)
            index = self.parent(index)

    def extract_min(self):
        """Удаление минимального элемента из кучи."""
        if not self.heap:
            raise IndexError("extract_min from empty heap")
        min_element = self.heap[0]
        last_element = self.heap.pop()
        if self.heap:
            self.heap[0] = last_element
            self.heapify_down(0)
        return min_element

    def heapify_down(self, index):
        """Восстановление свойства кучи после удаления элемента."""
        smallest = index
        left = self.left_child(index)
        right = self.right_child(index)

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left

        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self.swap(index, smallest)
            self.heapify_down(smallest)

    def build_heap(self, elements):
        """Построение кучи из списка элементов."""
        self.heap = elements[:]
        n = len(self.heap)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify_down(i)

    def merge(self, other_heap):
        """Объединение двух куч."""
        merged_heap = BinaryHeap()
        merged_heap.heap = self.heap + other_heap.heap
        merged_heap.build_heap(merged_heap.heap)
        return merged_heap

    def heap_sort(self):
        """Пирамидальная сортировка."""
        sorted_list = []
        temp_heap = BinaryHeap()
        temp_heap.heap = self.heap[:]
        while temp_heap.heap:
            sorted_list.append(temp_heap.extract_min())
        return sorted_list

    def __str__(self):
        return str(self.heap)
    
if __name__ == "__main__":
    heap = BinaryHeap()
    elements = [5, 3, 8, 1, 2, 9, 4]
    heap.build_heap(elements)
    print("Куча:", heap)

    heap.insert(0)
    print("После добавления 0:", heap)

    min_element = heap.extract_min()
    print("Извлеченный минимальный элемент:", min_element)
    print("Куча после извлечения:", heap)

    heap2 = BinaryHeap()
    elements2 = [7, 6, 10]
    heap2.build_heap(elements2)
    merged_heap = heap.merge(heap2)
    print("Объединенная куча:", merged_heap)

    sorted_list = merged_heap.heap_sort()
    print("Отсортированный список:", sorted_list)