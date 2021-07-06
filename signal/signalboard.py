
class valueboard(object):

    def __init__(self) -> None:
        super(valueboard,self).__init__()


class signalboard(object):

    def __init__(self) -> None:
        super(signalboard,self).__init__()
        self.this_signal = {}
        self.history_signel = {}

    def register_signal(self,name,initial_value=0):
        if self.this_signal.get(name) is not None:
            raise ValueError("ERROR:signal {} is already declaration")
        self.this_signal[name] = initial_value
        self.history_signel[name] = [initial_value]

    def set_value(self,name,value):
        self.this_signal[name] = value

    def renew(self):
        for name in self.this_signal.keys():
            value = self.this_signal[name]
            self.history_signel[name].append(value)

    def generate_valueboard(self):
        board = valueboard()
        for name in self.this_signal.keys():
            setattr(board,name,self.this_signal[name])
        return board


class signaldraw(object):

    def __init__(self,board) -> None:
        super(signaldraw,self).__init__()
        self.data = None
        self.dtype_dict = {}
        self.max_name_len = 0
        self.get_board(board)
        self.get_dtype()

    def get_board(self,board):
        self.data = board.self.history_signel

    def get_dtype(self):
        for name in self.data.keys():
            value_list = self.data[name]
            self.get_max_name_len(name)
            self.dtype_dict[name] = True
            for i in value_list:
                if i != 0 or i != 1:
                    self.dtype_dict[name] = False
                    break
        
    def get_max_name_len(self,name):
        if len(name) > self.max_name_len:
            self.max_name_len = len(name)