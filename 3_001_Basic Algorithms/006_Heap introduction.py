#%% Imports and functions declaration


class Heap:
    def __init__(self, initial_size):
        self.cbt = [None for _ in range(initial_size)]  # initialize arrays
        self.next_index = 0  # denotes next index where new element should go

    def _parent_index(self, children_index):
        return (children_index - 1)//2

    def _parent_value(self, children_index):
        return self.cbt[self._parent_index(children_index)]

    def _childrens_index(self, parent_index):
        return (2 * parent_index) + 1, (2 * parent_index) + 2

    def _childrens_value(self, parent_index):
        index_children_1, index_children_2 = self._childrens_index(parent_index)
        return self.cbt[index_children_1], self.cbt[index_children_2]

    def up_heapify(self, index):

        if index == 0:  # End of heap
            return

        index_parent = self._parent_index(children_index=index)
        value_parent = self._parent_value(children_index=index)
        value_children = self.cbt[index]

        if value_parent > value_children:  # Switch parent <-> children
            self.cbt[index] = value_parent  # Children Update
            self.cbt[index_parent] = value_children  # Parent Update
            self.up_heapify(index_parent)

        else:
            pass

    def insert(self, data):
            """
            Insert `data` into the heap
            """

            if self.next_index < len(self.cbt) - 1:
                self.cbt[self.next_index] = data
                self.up_heapify(self.next_index)
                self.next_index += 1
            else:  # Full heap
                pass

    def size(self):
        return self.next_index

    def down_heapify(self, index):

        if heap._childrens_index(index)[0] > self.size():
            return

        index_children_1, index_children_2 = self._childrens_index(parent_index=index)
        value_children_1, value_children_2 = self._childrens_value(parent_index=index)
        value_parent = self.cbt[index]

        if value_children_2 is None:
            if value_children_1 < value_parent:
                self.cbt[index] = value_children_1  # Parent Update
                self.cbt[index_children_1] = value_parent  # Parent Update
                self.down_heapify(index_children_1)
            else:
                pass

        elif value_children_1 < value_children_2:
            if value_children_1 < value_parent:
                self.cbt[index] = value_children_1  # Parent Update
                self.cbt[index_children_1] = value_parent  # Parent Update
                self.down_heapify(index_children_1)
            else:
                pass
        elif value_children_2 < value_children_1:
            if value_children_2 < value_parent:
                self.cbt[index] = value_children_2  # Parent Update
                self.cbt[value_children_2] = value_parent  # Parent Update
                self.down_heapify(value_children_2)
            else:
                pass
        else:
            pass

    def remove(self):
        """
        Remove and return the element at the top of the heap
        """

        value_pop = self.cbt[0]
        self.cbt[0] = self.cbt[self.next_index-1]  # Update with las nodes value
        self.cbt[self.next_index - 1] = None  # Delete last value

        self.down_heapify(index=0)

        return value_pop


#%% Testing - Insert
heap = Heap(initial_size=10)
test = [10, 20, 40, 50, 30, 70, 60, 75]

for number in test:
    heap.insert(number)

heap.insert(15)
print(heap.cbt)
# result = [10, 15, 40, 20, 30, 70, 60, 75, 50]

heap.remove()
print(heap.cbt)
# result = [15, 20, 40, 50, 30, 70, 60, 75]

