class HashTable: 
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hashvalue = self.hashfunction(key, len(self.slots))

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data # replace 
            else:
                nextslot = self.rehash(hashvalue, len(self.slots))
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    naxtslot = self.rehash(hashvalue, len(self.slots))        

                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data #replace 

    def hashfunction(self, key, size):
        return key%size

    def rehash(self, oldhash, size):
        return (oldhash+1)%size

    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots))

        found = False
        stop = False
        data = None 

        while self.slots[startslot] != None and not found and not stop:
            if self.slots[startslot] == key:
                found = True
                data = self.data[startslot]
            else:
                position = self.rehash(startslot, len(self.size))
                if self.slots[startslot] == self.slots[position]:
                    stop = True        

        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        return self.put(key, data)                



if __name__ == "__main__":
    H = HashTable()
    H[12] = 'Dasha'
    print(H[12], 'H')
    print(H)