import collections

class ThreeSidedDeque:
    def __init__(self):
        self.front_deque = collections.deque()
        self.back_deque = collections.deque()

    def append_front(self, item):
        self.front_deque.append(item)

    def append_back(self, item):
        self.back_deque.append(item)

    def append_middle(self, item):
        self.back_deque.appendleft(item)

    def pop_front(self):
        if not self.front_deque:
            raise IndexError("pop from an empty deque")
        return self.front_deque.pop()

    def pop_back(self):
        if not self.back_deque:
            raise IndexError("pop from an empty deque")
        return self.back_deque.pop()

    def pop_middle(self):
        if not self.back_deque:
            raise IndexError("pop from an empty deque")
        return self.back_deque.popleft()

    def __len__(self):
        return len(self.front_deque) + len(self.back_deque)

    def __repr__(self):
        return "ThreeSidedDeque({})".format(list(self.front_deque) + list(self.back_deque))

      
      deque = ThreeSidedDeque()
deque.append_front(1)
deque.append_front(2)
deque.append_back(4)
deque.append_middle(3)

print(deque)  # Output: ThreeSidedDeque([2, 1, 3, 4])

deque.pop_front()  # Output: 2
deque.pop_middle()  # Output: 3
deque.pop_back()  # Output: 4

print(deque)  # Output: ThreeSidedDeque([1])
