class MaxHeap:
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

    def heapify_max(self, size, node):
        """
        Function repairs our heap to proper max-heap.
        """
        n = size
        m = node
        _left = self.left(node)
        _right = self.right(node)

        if _left <= n - 1 and self.array[_left] > self.array[m]:
            m = _left
        else:
            m = node
        if _right <= n - 1 and self.array[_right] > self.array[m]:
            m = _right

        if m != node:
            self.swap(node, m)
            self.heapify_max(n, m)

    def build_max_heap(self):
        """
        Function creates max-heap from scratch.
        """
        n = int((self.heap_size - 1) / 2)
        for i in range(n, -1, -1):
            self.heapify_max(self.heap_size, i)

    def max_heap_sort(self):
        """
        Heapsort in-place algorithm in O(nlogn) time.
        """
        n = self.heap_size
        self.build_max_heap()
        for i in range(n - 1, -1, -1):
            self.swap(0, i)
            self.heapify_max(i, 0)

    def get_root_value(self):
        return self.array[0]

    def extract_max(self):
        if self.heap_size < 1:
            return "Error: Heap is empty."

        max_val = self.array[0]
        self.swap(0, self.heap_size - 1)
        self.array.pop()
        self.heap_size -= 1
        self.heapify_max(self.heap_size, 0)

        return max_val

    def increase_key(self, index, key):
        if key < self.array[index]:
            return "New key is smaller than actual key."

        self.array[index] = key
        while (index > 0
               and self.array[index] > self.array[self.parent(index)]):
            self.swap(index, self.parent(index))
            index = self.parent(index)

    def max_heap_insert(self, key):
        self.array.append(key)
        self.heap_size += 1
        self.increase_key(self.heap_size - 1, key)


def main():
    # Tests for max-heap functionality.
    tab = [1, 2, 3, 4, 7, 8, 9, 10, 14, 16]
    print("MAX-HEAP")
    heap = MaxHeap(tab)
    print(f"before:\n\t{tab}")
    heap.build_max_heap()
    print(f"build max-heap:\n\t{tab}")

    heap.increase_key(5, 18)
    print(f"\nIncreased key on index 5 to 18: {tab}\n")

    print(f"max value in heap: {heap.get_root_value()}")
    print(f"extracted max value: {heap.extract_max()}")
    print(f"extracted max value: {heap.extract_max()}")
    print(f"new max value in heap: {heap.get_root_value()}")

    heap.max_heap_insert(5)
    print(f"\ninserted value 5: {tab}\n")

    heap.max_heap_sort()
    print(f"sorted list: {tab}")


if __name__ == "__main__":
    main()
