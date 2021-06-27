import os,sys
sys.path.append(os.path.split(sys.path[0])[0])
from signal.signalboard import signalboard

class waveboard(object):

    def __init__(self,board) -> None:
        super(waveboard,self).__init__()
        self.data = board.history_signel
        self._get_max_name_len()
        self.wave = {}
        self.gen_clk_wave()
        # print(self.data)

    def _get_max_name_len(self):
        self.name_len = 0
        self.wave_len = 0
        for name in self.data.keys():
            if len(name) > self.name_len:
                self.name_len = len(name)
            self.wave_len = len(self.data[name])
        self.name_len += 4

    def _get_signal_dtype(self,name):
        for s in self.data[name]:
            if s != 0 and s!= 1:
                return False # is data
        return True # is bool

    def gen_clk_wave(self):
        clk_wave = "".join(['        ']+['/```\...' for _ in range(self.wave_len-1)])
        self.wave["clk"] = clk_wave

    def gen_bool_wave(self,name):
        wave_list = []
        last_data = self.data[name][0]
        for s in self.data[name]:
            if s == 1 and last_data == 1:
                wave_list.append('````````')
            elif s == 0 and last_data == 1:
                wave_list.append('`\......')
            elif s == 1 and last_data == 0:
                wave_list.append('./``````')
            elif s == 0 and last_data == 0:
                wave_list.append('........')
            last_data = s
        return "".join(wave_list)

    def gen_data_wave(self,name):
        wave_list = []
        last_data = None
        for s in self.data[name]:
            if s == last_data:
                wave_list.append('--------')
            elif s <= 999999:
                wave_list.append('-|{}'.format(s).ljust(8,'-'))
            else:
                this_char = str(s)[:6]
                wave_list.append('-|{}'.format(s))
            last_data = s
        return "".join(wave_list)

    def draw(self):
        for name in self.data.keys():
            dtype = self._get_signal_dtype(name)
            if dtype:
                self.wave[name] = self.gen_bool_wave(name)
            else:
                self.wave[name] = self.gen_data_wave(name)
        # print(self.wave)

    def gen_wave(self):
        wave_list = []
        wave_list.append("{}{}".format("clk".ljust(self.name_len),self.wave['clk']))
        for name in self.wave.keys():
            if name == 'clk':
                continue
            name_char = name.ljust(self.name_len)
            wave_list.append('{}{}'.format(name_char,self.wave[name]))
        # print(wave_list)
        return "\n".join(wave_list)

    def dump(self,path):
        with open(path,'w') as f:
            f.write(self.gen_wave())

    def print(self):
        print("INFO:this is wave")
        print(self.gen_wave())
