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

if __name__=='__main__':
    a = test()
    a.test_a()
    print(a.table)