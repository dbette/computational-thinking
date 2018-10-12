class Node:

    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None

    def add(self, key, data):
        if self.key < key:
            if self.right == None:
                self.right = Node(key, data)
            else:
                self.right.add(key, data)
        else:
            if self.left == None:
                self.left = Node(key, data)
            else:
                self.left.add(key, data)

    def get(self, key):
        if key == self.key:
            print(self.data)
        elif key < self.key:
            if self.left.key == key:
                print(self.left.data)
            else:
                self.left.get(key)
        elif key > self.key:
            if self.right.key == key:
                print(self.right.data)
            else:
                self.right.get(key)
        else:
            print("Key not found")

classroom = Node("Felix", 24)
classroom.add("Sitong", 23)
classroom.add("Zitong", 23)
classroom.add("Michelle", 23)
classroom.add("Jiayao", 26)
classroom.add("Dominik", 25)

for name in ["Felix", "Sitong", "Zitong", "Michelle", "Jiayao", "Dominik"]:
    classroom.get(name)
