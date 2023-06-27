from yaramo.model import Signal
import logging


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

    def print_evaluation(self):
        logging.debug(f"{self.yaramo_signal.name} Set Halt: {self.was_set_halt}; "
                      f"Set Go: {self.was_set_go}; Coverage: {self.get_coverage()}")
