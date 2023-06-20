from yaramo.model import Node


class PointMonitorResult(object):

    def __init__(self, yaramo_point: Node):
        self.yaramo_point = yaramo_point
        self.was_turned_left = False
        self.was_turned_right = False

    def get_coverage(self):
        if self.was_turned_left and self.was_turned_right:
            return 1.0
        if not self.was_turned_left and not self.was_turned_right:
            return 0.0
        return 0.5
