class Paramer:
    arr=[]
    index=0;

    def __init__(self,arr):
        self.arr = arr

    def get(self,index):
        return self.arr[index]

    def nextNum(self):
        if (self.index == len(self.arr)):
            return
        yield self.arr[self.index]
        self.index+=1

    def getArr(self):
        return self.arr