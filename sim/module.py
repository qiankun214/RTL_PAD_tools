import sys,os
sys.path.append(os.path.split(sys.path[0])[0])


from enum import Enum
class MODENAME(Enum):
    build = 0
    init = 1
    reg_value = 2
    reg_renew = 3
    wire_value = 4
    wire_renew = 5


from signal.signalboard import signalboard 


class module(object):

    def __init__(self) -> None:
        super(module,self).__init__()
        self.mode = MODENAME.build
        self.reg_board = signalboard()
        self.wire_board = signalboard()
        self.dtype_info = {}
        # self.value_dict = {}

    def reg(func):
        def reg_wrapper(self):
            reg_name = func.__name__
            if self.mode == MODENAME.build:
                self._build_value(reg_name,"reg")
                self.value_dict[reg_name] = func
            elif self.mode == MODENAME.init:
                pass
            elif self.mode == MODENAME.reg_value:
                

        return reg_wrapper

    def _build_value(self,name,dtype):
        if self.dtype_info.get(name) is not None:
            raise ValueError("ERROR: value {} is already declaration")
        if "reg" in dtype:
            self.dtype_info[name] = "reg"
            self.reg_board.register_signal(name)
        else:
            self.dtype_info[name] = "wire"
            self.wire_board.register_signal(name)
        