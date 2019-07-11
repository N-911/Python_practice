"""Python’s with statement supports the concept of a runtime context defined by a context manager.
This is implemented using a pair of methods that allow user-defined classes to define a runtime
context that is entered before the statement body is executed and exited when the statement ends:
contextmanager.__enter__()
contextmanager.__exit__(exc_type, exc_val, exc_tb)¶
"""

class open_file:
    def __init__(self, filename, mode):
        self.f = open(filename, mode)

    def __enter__(self):
        return self.f


    def __exit__(self, *args):
        self.f.close()


if __name__ == "main":
    with open_file(f'k:\Github\111.txt', 'w') as f:
        f.write('write with context manadger')

    with open(f'k:\Github\111.txt', 'r') as f:
        print(f.readline())