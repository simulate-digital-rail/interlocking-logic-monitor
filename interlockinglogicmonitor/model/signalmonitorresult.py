from yaramo.model import Signal


class SignalMonitorResult(object):

    def __init__(self, yaramo_signal: Signal):
        self.yaramo_signal = yaramo_signal
        self.was_set_halt = False
        self.was_set_go = False

    def get_coverage(self):
        if self.was_set_halt and self.was_set_go:
            return 1.0
        if not self.was_set_halt and not self.was_set_go:
            return 0.0
        return 0.5
