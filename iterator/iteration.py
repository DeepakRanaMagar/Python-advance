class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self 
    def __next__(self):
        if self.a <= 10:
            self.a +=1
            x = self.a
            return x
        else:
            raise StopIteration
myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)
 