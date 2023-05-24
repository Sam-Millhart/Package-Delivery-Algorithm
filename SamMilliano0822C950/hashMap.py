class HashMap:
    def __init__(self, capacity=10):
        self.map = []
        for _ in range(capacity):
            self.map.append([])

# Create hash key
# Space-time complexity is O(1)
    def createHashKey(self, key):
        return int(key) % len(self.map)


# Insert package into hash table
# Space-time complexity is O(N)
    def insert(self, key, value):
        keyHash = self.createHashKey(key)
        keyValue = [key, value]

        if self.map[keyHash] == None:
            self.map[keyHash] = list([keyValue])
            return True
        else:
            for pair in self.map[keyHash]:
                if pair[0] == key:
                    pair[1] = keyValue
                    return True
            self.map[keyHash].append(keyValue)
            return True

# Update package in hash table
# Space-time complexity is O(N)
    def update(self, key, value):
        keyHash = self.createHashKey(key)
        if self.map[keyHash] != None:
            for pair in self.map[keyHash]:
                if pair[0] == key:
                    pair[1] = value
                    print(pair[1])
                    return True
        else:
            print('There was an error with updating on key: ' + key)

# Get a value from hash table
# Space-time complexity is O(N)
    def getValue(self, key):
        keyHash = self.createHashKey(key)
        if self.map[keyHash] != None:
            for pair in self.map[keyHash]:
                if pair[0] == key:
                    return pair[1]
        return None

# Delete a value from hash table
# Space-time complexity is O(N)
    def delete(self, key):
        keyHash = self.createHashKey(key)

        if self.map[keyHash] == None:
            return False
        for i in range(0, len(self.map[keyHash])):
            if self.map[keyHash][i][0] == key:
                self.map[keyHash].pop(i)
                return True
        return False

class HashTableEntry:
    def __init__(self, key, item):
        self.key = key
        self.item = item