"""
The iterator objects themselves are required to support the following two methods, which together form the iterator protocol:
iterator.__iter__()
iterator.__next__()¶
"""

iterator_object = iter([10,20,4])      #funtcion iter      metod - next

class SIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        result = self.current**2
        self.current +=1
        return result

"""
 iterator realaised  with method __getitem__   
 acsess to element for index
"""

class IndexIterable:
    def __init__(self):
        self.obj = self

    def __getitem__(self, index):
        return self.obj[index]

if __name__ == "__main__":
    dd = SIterator(2, 5)
    for w in SIterator(1, 5):
        print(w, end=', ')
    print('\n')

    print(next(iterator_object))
