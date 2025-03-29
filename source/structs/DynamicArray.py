import typing

class Array:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.arr = [0] * capacity


    def get(self, index: int) -> int:
        return self.arr[index]

    
    def set(self, index: int, n: int):
        self.arr[index] = n

    
    def pushback(self, n: int):
        if self.length == self.capacity:
            self.resize()

        self.arr[self.length] = n
        self.length += 1


    def popback(self) -> int:
        if self.length > 0:
            self.length -= 1

        return self.arr[self.length]


    def resize(self):
        self.capacity = self.capacity * 2
        new_arr = [0] * self.capacity

        for n in range(self.length):
            new_arr[n] = self.arr[n]
        self.arr = new_arr

    
    def getSize(self) -> int:
        return self.length
    

    def getCapacity(self) -> int:
        return self.capacity

"""
Space Complexity -> O(n)
when resizing it doubles leading to O(capacity)

Time Complexity -> O(1)
get() immediately gets arr[index]
set() immediately sets an index to n
pushback() is O(1) since it puts n at end of lists unless it resizes which is O(n)
popback() returns last after temp setting self.length one back
resize() doubles arrays but copies each O(n)
getSize() instantly returns attribute
getCapacity() instantly returns attribute
"""