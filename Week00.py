Cristian Arroyo
Comp 363 - 002
9/5/25

def left_child(parent: int) -> int:
    """Index of the left child."""
    return 2 * parent + 1

def right_child(parent: int) -> int:
    """Index of the right child."""
    return 2 * (parent + 1)

def parent(child: int) -> int:
    """Index of the parent."""
    return (child - 1) // 2

def swap(heap_array: list, i: int, j: int) -> None:
    """In-place swap of two array elements."""
    if i != j:
        heap_array[i], heap_array[j] = heap_array[j], heap_array[i]

class MinHeap:
    """A simple minimum-heap implementation using a Python list."""

    def __init__(self):
        self.heap_array: list = []
        self.element_counter: int = 0

    def _heapify_up(self, index: int) -> None:
        """Restore the min-heap property from bottom to top."""
        # bubble up while parent is larger
        while index > 0 and self.heap_array[parent(index)] > self.heap_array[index]:
            p = parent(index)
            swap(self.heap_array, p, index)
            index = p

    def _heapify_down(self, index: int) -> None:
        """Restore the min-heap property from top to bottom."""
        done = False
        while not done:
            left = left_child(index)
            right = right_child(index)
            smallest = index

            if left < self.element_counter and self.heap_array[left] < self.heap_array[smallest]:
                smallest = left
            if right < self.element_counter and self.heap_array[right] < self.heap_array[smallest]:
                smallest = right

            if smallest != index:
                swap(self.heap_array, index, smallest)
                index = smallest
            else:
                done = True  # exit loop without break

    def add(self, text: str) -> None:
        """Add a new element to the heap."""
        if self.element_counter < len(self.heap_array):
            self.heap_array[self.element_counter] = text
        else:
            self.heap_array.append(text)
        self.element_counter += 1
        self._heapify_up(self.element_counter - 1)

    def remove(self) -> str | None:
        """Remove and return the smallest element from the heap."""
        removed = None
        if self.element_counter > 0:
            removed = self.heap_array[0]
            self.element_counter -= 1
            if self.element_counter > 0:
                self.heap_array[0] = self.heap_array[self.element_counter]
                self._heapify_down(0)
            self.heap_array.pop()
        return removed

    def peek(self) -> str | None:
        """Return the smallest element without removing it."""
        result = None
        if self.element_counter > 0:
            result = self.heap_array[0]
        return result

    def size(self) -> int:
        """Return the number of elements currently stored in the heap."""
        return self.element_counter

    def __str__(self) -> str:
        """String representation for debugging."""
        return str(self.heap_array[:self.element_counter])

# Simple test block
if __name__ == "__main__":
    heap = MinHeap()
    heap.add("delta")
    heap.add("alpha")
    heap.add("charlie")
    heap.add("bravo")

    print("Heap:", heap)
    print("Smallest element:", heap.peek())
    print("Removed:", heap.remove())
    print("Heap after removal:", heap)
    print("Heap size:", heap.size())

