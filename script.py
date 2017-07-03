import subprocess


class Decode:
    #
    # def __init__(self):
    #     self.inputD = str(subprocess.check_output(['pacmd', 'list-cards']))

    def list_cards(self):
        self.inputD = str(subprocess.check_output(['pacmd', 'list-cards']))
        _l = self.inputD.split("   ")
        _l = _l[1:]
        return _l

    def list_profiles(self):
        _L = []
        _l = []
        for _card in self.list_cards():
            _namedev = str(
                (_card.split("\\t\\tdevice.description = \"")[1]).split("\"")[0])
            _ul1, _uf1 = _card.split("name: <")
            _ipdev, _uf2 = _uf1.split(">\\n\\tdriver")
            _ul3, _uf3 = _uf2.split("\\n\\tprofiles:")
            _uf4, _ul4 = _uf3.split("\\n\\tactive profile:")
            _lbfr = _uf4.split(u"\\n\\t\\t")
            _lbfr = _lbfr[1:]
            for _profile in _lbfr:
                _lprof = _profile.split(": ")
                _l += [_lprof[0]]
            _L += [[_namedev, _ipdev, _l]]
            _l = []

        return _L

    def __str__(self):
        return str(self.list_profiles())


class Cmd(Decode):

    def __init__(self, _dev = 0, _prof = 0):
        super().__init__()
        self.inputC = self.list_profiles()
        self.device = _dev
        self.profile = _prof

    def set_dev_as_def(self):
        subprocess.call(["pacmd", "set-default-sink %s" % (self.inputC[self.device][1])])

    def set_profiles(self):
        for _card in self.inputC:
            subprocess.call(["pacmd", "set-card-profile %s off" % (_card[1])])
        subprocess.call(["pacmd", "set-card-profile %s %s" % (self.inputC[self.device][1], self.inputC[self.device][2][self.profile])])


def main():
    pass

if __name__ == "__Decode__" or __name__ == "Cmd":
   main()
