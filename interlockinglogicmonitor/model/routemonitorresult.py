from yaramo.model import Route


class RouteMonitorResult(object):

    def __init__(self, yaramo_route: Route):
        self.yaramo_route = yaramo_route
        self.was_set = False
        self.was_free = False
        self.was_reset = False

    def get_coverage(self):
        count = 0
        if self.was_set:
            count = count + 1
        if self.was_free:
            count = count + 1
        if self.was_reset:
            count = count + 1
        return count / 3
