from yaramo.model import Route
import logging


class RouteMonitorResult(object):

    def __init__(self, yaramo_route: Route):
        self.yaramo_route = yaramo_route
        self.was_set = False
        self.was_freed = False
        self.was_reset = False

    def get_coverage(self):
        count = 0
        if self.was_set:
            count = count + 1
        if self.was_freed:
            count = count + 1
        if self.was_reset:
            count = count + 1
        return count / 3

    def print_evaluation(self):
        logging.debug(f"{self.yaramo_route.start_signal.name} -> {self.yaramo_route.end_signal.name} "
                      f"Set: {self.was_set}; Freed: {self.was_freed}; Reset: {self.was_reset}; "
                      f"Coverage: {self.get_coverage()}")
