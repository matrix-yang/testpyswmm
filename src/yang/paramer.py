class Paramer:
    name=''
    arr=[]
    index=1;

    def __init__(self,arr,name):
        self.arr = arr
        self.name=name

    def getCurrent(self):
        return self.arr[self.index]

    def get(self,index):
        return self.arr[index]

    def nextNum(self):
        if (self.index == len(self.arr)):
            return
        rs= self.arr[self.index]
        self.index += 1
        return rs

    def getArr(self):
        return self.arr

    def optIdx(self,num):
        self.index=self.index+num

    def getName(self):
        return self.name