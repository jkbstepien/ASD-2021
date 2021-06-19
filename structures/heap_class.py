class Heap:
    def __init__(self, array):
        self.array = array
        self.heap_size = len(self.array)

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
        _left = node * 2 + 1
        _right = node * 2 + 2
        m = node

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

    def heapify_min(self, size, node):
        """
        Function repairs our heap to proper min-heap.
        """
        n = size
        _left = node * 2 + 1
        _right = node * 2 + 2
        m = node

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

    def get_elem(self):
        pass


def main():
    # Tests for max-heap functionality.
    tab1 = [1, 2, 3, 4, 7, 8, 9, 10, 14, 16]
    print("MAX-HEAP")
    heap1 = Heap(tab1)
    print(f"before:\n\t{tab1}")
    heap1.build_max_heap()
    print(f"build max-heap:\n\t{tab1}")
    heap1.max_heap_sort()
    print(f"sorted list:\n\t{tab1}")

    # Tests for min-heap functionality.
    print("\nMIN-HEAP")
    tab2 = sorted(tab1, reverse=True)
    heap2 = Heap(tab2)
    print(f"before:\n\t{tab2}")
    heap2.build_min_heap()
    print(f"build min-heap:\n\t{tab2}")


if __name__ == "__main__":
    main()
