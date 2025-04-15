import random
class RandomizedSet:

    def __init__(self):
        # self.set = set()
        self.dt = defaultdict(int)
        self.lst = []
        # self.count = 0

    def insert(self, val: int) -> bool:
        if val not in self.dt:
            # self.set.add(val)
            # self.count += 1
            self.dt[val] = len(self.lst)
            self.lst.append(val)
            return True
        else:
            return False        

    def remove(self, val: int) -> bool:
        # print(val, self.dt)
        if val in self.dt:
            # self.set.remove(val)
            last_elem = self.lst[-1]
            idx = self.dt[val]

            # elem_to_rm = self.lst[idx]
            self.lst[idx] = last_elem
            self.dt[last_elem] = idx
            
            self.lst.pop()
            self.dt.pop(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        # return self.lst[random.randint(0, len(self.set)-1)]
        return random.choice(self.lst)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()