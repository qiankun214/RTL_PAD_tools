
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