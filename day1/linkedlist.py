class Node:
    def __init__(self, dataval=None, comparators=None):
        self.compare = comparators
        self.dataval = dataval
        self.nextval = None


class LinkedList:
    def __init__(self, headval=None):
        self.headval = headval
        self.len = 1

    def __len__(self):
        return self.len

    def iterate(self, times=None):
        val = self.headval
        if times != None:
            for i in range(0, times):
                preval = val.dataval
                val = val.nextval
                yield preval
                continue
        else:
            while val != None:
                yield val.dataval
                val = val.nextval
                continue

    def get(self, number):
        val = self.headval
        for i in range(0, number):
            val = val.nextval
        return val

    def insert_end(self, node):
        val = self.headval
        if self.headval.nextval != None:
            for i in range(0, self.len):
                val = val.nextval
            val.nextval = node
            self.len += 1
        else:
            val.nextval = node

    def delete(self, integer):
        val = self.get(integer)
        other = self.get(integer+1)
        val = other
        self.len -= 1

    def deleteall(self, value):
        val = self.headval
        for i in range(0, self.len+1):
            if val.compare == None:
                if val.dataval == value:
                    if i == 0:
                        self.headval = val.nextval
                        val = self.headval
                        self.len -= 1
                        continue
                    else:
                        val = val.nextval
                        self.len -= 1
                        continue
                else:
                    continue
            else:
                for j in val.compare:
                    if hasattr(val.dataval, j) and hasattr(value, j):
                        if getattr(val.dataval, j) == getattr(value, j):
                            tok = self.search(val.dataval)
                            tok = tok[0]
                            if tok == 0:
                                self.headval = val.nextval
                                val = self.headval
                                self.len -= 1
                                continue
                            else:
                                self.delete(i)
                                continue
                        else:
                            continue
                    else:
                        continue

    def search(self, value):
        val = self.headval
        points = []
        for i in range(0, self.len+1):
            if val.compare == None:
                if val.dataval == value:
                    points.append(i)
                    val = val.nextval
                    continue
                else:
                    val = val.nextval
                    continue
            else:
                for j in val.compare:
                    if hasattr(val.dataval, j) and hasattr(value, j):
                        if getattr(val.dataval, j) == getattr(value, j):
                            points.append(i)
                            val = val.nextval
        if len(points) == 0:
            return False
        else:
            return points

    def insert_beginning(self, node):
        node.nextval = self.headval
        self.headval = node
