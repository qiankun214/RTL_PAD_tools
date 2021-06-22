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

def reg(initial_value):
    def reg_wrapper(func):
        def inter_wrapper(self):
            reg_name = func.__name__
            if self.mode == MODENAME.build:
                self._build_value(reg_name,"reg",initial_value)
                self.value_dict[reg_name] = inter_wrapper
            elif self.mode == MODENAME.init:
                pass
            elif self.mode == MODENAME.reg_value:
                self.board.set_value(reg_name,func(self))
            elif self.mode == MODENAME.reg_renew:
                pass
            elif self.mode == MODENAME.wire_value:
                pass
            elif self.mode == MODENAME.wire_renew:
                pass
            else:
                raise ValueError("FATAL:mode undefined")
        return inter_wrapper
    return reg_wrapper

def drive(initial_value):
    def drive_wrapper(func):
        def inter_wrapper(self):
            drive_name = func.__name__
            if self.mode == MODENAME.build:
                self._build_value(drive_name,"reg",initial_value)
                self.value_dict[drive_name] = inter_wrapper
                self.drive_dict[drive_name] = func(self)
            elif self.mode == MODENAME.init:
                pass
            elif self.mode == MODENAME.reg_value:
                try:
                    result = next(self.drive_dict[drive_name])
                    self.board.set_value(drive_name,result)
                except StopIteration as e:
                    print("WARNING: cannot get data from drive {} at timestep {}".format(drive_name,self.time))
                    # self.board.set_value(drive_name)
            elif self.mode == MODENAME.reg_renew:
                pass
            elif self.mode == MODENAME.wire_value:
                pass
            elif self.mode == MODENAME.wire_renew:
                pass
            else:
                raise ValueError("FATAL:mode undefined")
        return inter_wrapper
    return drive_wrapper
# V = None

class module(object):

    def __init__(self) -> None:
        super(module,self).__init__()
        self.mode = MODENAME.build
        self.board = signalboard()
        self.value_dict = {}
        self.dtype_info = {}
        self.drive_dict = {}
        self.value = None
        self.time = 0
        # global V
        # V = self.value
        print("INFO:module build start")


    def _build_value(self,name,dtype,initial_value):
        if self.dtype_info.get(name) is not None:
            raise ValueError("ERROR: value {} is already declaration")
        self.board.register_signal(name,initial_value)
        if "reg" in dtype:
            self.dtype_info[name] = "reg"
        else:
            self.dtype_info[name] = "wire"
        print("INFO:build value {},initial {}".format(name,initial_value))

    def __call__(self,times=10):
        # initial
        self.time = 0
        for i in range(times):
            # before reg value
            print("INFO: timestep {}".format(self.time))
            self.mode = MODENAME.reg_value
            self.value = self.board.generate_valueboard()
            # reg value
            for name in self.value_dict.keys():
                self.value_dict[name](self)
            # reg renew
            self.mode = MODENAME.reg_renew
            self.board.renew()
            # wire value
            self.mode = MODENAME.wire_value

            # wire renew
            self.mode = MODENAME.wire_renew

            # post 
            self.time += 1
