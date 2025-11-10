class HashTableArray:   # separate chaining class
    class Entry:    # bucket entry type
        def __init__(self, key, value):
            self.key = key
            self.value = value

    def __init__(self, capacity=10):    # constructor
        self.capacity = capacity #size of the array of the hash table
        self.table = [[] for _ in range(capacity)]
        self.size = 0 # number of items in has table

    def _hash(self, key):   # hash function
        return hash(key) % self.capacity
    
    def insert(self, key, value):   # insert method
        index = self._hash(key)  
        bucket = self.table[index] #

        for entry in bucket:
            if entry.key == key: #  if same key is found, update value
                entry.value = value 
                return

        bucket.append(self.Entry(key, value))
        self.size += 1  
    
    def search(self, key, value):   # search method
        index = self._hash(key)
        bucket = self.table[index]

        for entry in bucket:
            if entry.key == key:
                return entry.value
            
        return None #key is not found in the hash table bucket

    def delete(self, key):  # delete method
        index = self._hash(key)
        bucket = self.table[index]
        for i, e in enumerate(bucket):
            if e.key == key:
                del bucket[i]
                self.size -= 1
                return True
        return False

    def __len__(self):  # length method for size of hash table
        return self.size
    
    def print_table(self):  # print method
        for i, bucket in enumerate(self.table):  # fixed loop
            print(f'{i}: ', end='')
            for entry in bucket:
                print(f'[{entry.key}, {entry.value}]', end=' ')
            print()

    # Question 1.2
    class BabyProduct:
        def __init__(self, sku, name, price, stock, category):
            self.sku = sku
            self.name = name
            self.price = price
            self.stock = stock
            self.category = category

        def __repr__(self):
            return f"{self.name} | RM{self.price} | Stock: {self.stock} | Category: {self.category}"


if __name__ == "__main__":
    hash_table = HashTableArray()

    p1 = BabyProduct("D001", "Drypers Wee Wee Diapers", 29.90, 100, "Diapers")
    p2 = BabyProduct("B002", "Pigeon Baby Bottle 240ml", 24.50, 50, "Feeding")
    p3 = BabyProduct("W003", "Pureen Baby Wipes 80s", 9.90, 200, "Care")
    p4 = BabyProduct("L004", "Johnson’s Baby Lotion 200ml", 16.90, 80, "Skincare")

    hash_table.insert(p1.sku, p1)
    hash_table.insert(p2.sku, p2)
    hash_table.insert(p3.sku, p3)
    hash_table.insert(p4.sku, p4)


    print('Get banana: ', hash_table.search('banana'))
