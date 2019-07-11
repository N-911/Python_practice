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

dd= SIterator(2,5)

for w in SIterator(1,5):
    print(w, end= ', ')


