import copy
class fixed(object):

    def __init__(self,width,init=0) -> None:
        super(fixed,self).__init__()
        self.as_width(width)
        self.data = init

    def as_width(self,width):
        self.width = width
        self.max_data = 2 ** width - 1
        self.min_data = 0
        return copy.deepcopy(self)

    def _overflow(self):
        if self.data > self.max_data or self.data < self.min_data:
            length = self.max_data - self.min_data + 1
            self.data = (self.data - self.min_data) % length
            self.data += self.min_data

    def _get_data_basetype(self,other):
        if type(other) == int:
            return other,None
        elif type(other) == float:
            raise ValueError("ERROR:get float data in fixed opreater")
        elif hasattr(other,"data") and hasattr(other,'width'):
            return other.data,other.width
        else:
            raise ValueError("ERROR:unsupport dtype {}".format(type(other)))

    def gen_operate_object(self,other):
        other_data,other_width = self._get_data_basetype(other)
        if other_width is None:
            return other_data,copy.deepcopy(self)
        else:
            result = copy.deepcopy(self)
            result.as_width(max(self.width,other_width))
            return other_data,result

        
    def __add__(self,other):
        other,result = self.gen_operate_object(other=other)
        result.data = other + self.data
        result._overflow()
        return result

    def __sub__(self,other):
        other,result = self.gen_operate_object(other=other)
        result.data = self.data - other
        result._overflow()
        return result

    def __mul__(self,other):
        other,result = self.gen_operate_object(other=other)
        result.data = self.data * other
        result._overflow()
        return result

    def __eq__(self, other) -> bool:
        other,_ = self._get_data_basetype(other)
        return other == self.data

    def __neq__(self, other) -> bool:
        other,_ = self._get_data_basetype(other)
        return other != self.data

    def __lt__(self,other):
        other,_ = self._get_data_basetype(other)
        return self.data < other

    def __gt__(self,other):
        other,_ = self._get_data_basetype(other)
        return self.data > other

    def __le__(self,other):
        other,_ = self._get_data_basetype(other)
        return self.data <= other

    def __ge__(self,other):
        other,_ = self._get_data_basetype(other)
        return self.data >= other

    def __repr__(self) -> str:
        return "{}({})".format(self.data,self.width)

if __name__ == '__main__':
    a = fixed(8,156)
    b = 5
    print(a < b,a > b,a <= b,a>= b,a == b,a != b)