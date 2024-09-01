class HashMap:

    def __init__(self):
        # Initialize an empty list to store key-value pairs
        self.map = []

    def put(self, key: int, value: int) -> None:
        # Check if the key already exists in the map
        for i, (k, v) in enumerate(self.map):
            if k == key:
                # Update the value if the key is found
                self.map[i] = (key, value)
                return
        # If the key is not found, add the new key-value pair
        self.map.append((key, value))

    def get(self, key: int) -> int:
        # Iterate through the map to find the key
        for k, v in self.map:
            if k == key:
                return v
        # If the key is not found, return -1
        return -1

    def remove(self, key: int) -> None:
        # Iterate through the map to find the key and remove the key-value pair
        for i, (k, v) in enumerate(self.map):
            if k == key:
                self.map.pop(i)
                return


# Example of usage:
# from structs.hashmap import HashMap
# obj = HashMap()
# obj.put(key, value)
# param_2 = obj.get(key)
# obj.remove(key)
