from sim.module import module,reg,drive

class test(module):

    def __init__(self) -> None:
        super(test,self).__init__()
        self.din_valid()
        self.din_busy()
        self.din_valid_reg()

    @reg(initial_value=0)
    def din_valid(self):
        print("valid is",self.value.din_valid)
        return self.value.din_valid_reg

    @reg(initial_value=1)
    def din_busy(self):
        print("busy is",self.value.din_busy)
        return self.value.din_valid % 2 

    @drive(initial_value=1)
    def din_valid_reg(self):
        print("valid reg is ",self.value.din_valid_reg)
        yield 1
        print("valid reg is ",self.value.din_valid_reg)
        yield 2
        print("valid reg is ",self.value.din_valid_reg)
        yield 3
        print("valid reg is ",self.value.din_valid_reg)
        yield 4


if __name__=='__main__':
    a = test()
    a()