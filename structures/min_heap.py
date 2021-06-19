class MinHeap:
    def __init__(self, array):
        self.array = array
        self.heap_size = len(self.array)

    @staticmethod
    def left(i):
        return 2 * i + 1

    @staticmethod
    def right(i):
        return 2 * i + 2

    @staticmethod
    def parent(i):
        return int((i - 1) / 2)

    def swap(self, index1, index2):
        """
        Swaps value in a list under index1 with value under index2.
        """
        copy_index1 = self.array[index1]
        self.array[index1] = self.array[index2]
        self.array[index2] = copy_index1

    def heapify_min(self, size, node):
        """
        Function repairs our heap to proper min-heap.
        """
        n = size
        m = node
        _left = self.left(node)
        _right = self.right(node)

        if _left <= n - 1 and self.array[_left] < self.array[m]:
            m = _left
        else:
            m = node
        if _right <= n - 1 and self.array[_right] < self.array[m]:
            m = _right

        if m != node:
            self.swap(node, m)
            self.heapify_min(n, m)

    def build_min_heap(self):
        """
        Function creates min-heap from scratch.
        """
        n = int((self.heap_size - 1) / 2)
        for i in range(n, -1, -1):
            self.heapify_min(self.heap_size, i)

    def get_root_value(self):
        return self.array[0]

    def extract_min(self):
        if self.heap_size < 1:
            return "Error: Heap is empty."

        min_val = self.array[0]
        self.swap(0, self.heap_size - 1)
        self.array.pop()
        self.heap_size -= 1
        self.heapify_min(self.heap_size, 0)

        return min_val

    def decrease_key(self, index, key):
        if key > self.array[index]:
            return "New key is bigger than actual key."

        self.array[index] = key
        while (index > 0
               and self.array[index] < self.array[self.parent(index)]):
            self.swap(index, self.parent(index))
            index = self.parent(index)

    def min_heap_insert(self, key):
        self.array.append(key)
        self.heap_size += 1
        self.decrease_key(self.heap_size - 1, key)


def main():
    # Tests for min-heap functionality.
    print("\nMIN-HEAP")
    tab = [16, 14, 10, 9, 8, 7, 4, 3, 2, 1]
    heap = MinHeap(tab)
    print(f"before:\n\t{tab}")
    heap.build_min_heap()
    print(f"build min-heap:\n\t{tab}")

    heap.decrease_key(6, 3)
    print(f"\nDecreased key on index 6 to 3: {tab}\n")

    heap.min_heap_insert(20)
    print(f"inserted value 20: {tab}")
    heap.min_heap_insert(0)
    print(f"inserted value 0: {tab}")

    print(f"\nmin value in heap: {heap.get_root_value()}")
    print(f"extracted min value: {heap.extract_min()}, {tab}")
    print(f"extracted min value: {heap.extract_min()}, {tab}")
    print(f"new min value in heap: {heap.get_root_value()}")


if __name__ == "__main__":
    main()
