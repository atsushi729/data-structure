import unittest



#######################################################
#              Not working code below!                #
#######################################################
class FreqStack:

    def __init__(self):
        self.stack = []
        self.counter = {}

    def push(self, val: int) -> None:
        self.counter[val] = self.counter.get(val, 0) + 1
        self.stack.append(val)

    def pop(self) -> int:
        sorted_list = sorted(self.counter.items(), key=lambda x: x[1], reverse=True)
        most_frequent_val = sorted_list[-1][0]
        self.counter[most_frequent_val] -= 1

        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i] == most_frequent_val:
                self.stack.remove(i)
                return most_frequent_val
