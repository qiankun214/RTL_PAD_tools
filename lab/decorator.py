class test(object):
    
    def __init__(self) -> None:
        super(test,self).__init__()
        self.table = []

    def decorator(func):
        def print_name(self):
            print("func name is {}".format(func.__name__))
            self.table.append(func.__name__)
            return func(self)
        return print_name

    @decorator
    def test_a(self):
        print("my name is test_a")

class test2(test):

    def __init__(self) -> None:
        super(test2,self).__init__()

    @decorator
    def test_b(self):
        print("my name is test_b")
        
if __name__=='__main__':
    a = test()
    a.test_a()
    print(a.table)