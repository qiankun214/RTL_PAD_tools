from sim.module import module,reg

class test(module):

    def __init__(self) -> None:
        super(test,self).__init__()
        self.din_valid()
        self.din_busy()

    @reg(initial_value=0)
    def din_valid(self):
        print("valid is",self.value.din_valid)
        return self.value.din_busy

    @reg(initial_value=1)
    def din_busy(self):
        print("busy is",self.value.din_busy)
        return self.value.din_valid


if __name__=='__main__':
    a = test()
    a()