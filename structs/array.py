class Array:
    def __init__(self):
        self.data = []
        self.size = 0

    def add_element(self, element):
        self.data.append(element)
        return self.data

    def remove_element(self, element):
        self.data.remove(element)
        return self.data

    def access_element(self, element):
        if element in self.data:
            index = self.data.index(element)
            return self.data[index]


"""
Example usage

from structs.array import Array

a = Array()

for i in range(10):
    a.add_element(i)

print(a.data)

a.access_element(4)

a.remove_element(4)

a.access_element(4)

print(a.data)
"""