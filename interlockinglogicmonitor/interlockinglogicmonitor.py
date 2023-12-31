from yaramo.model import Topology, Route
from .model import RouteMonitorResult


class InterlockingLogicMonitor(object):

    def __init__(self, yaramo_topology: Topology):
        self.route_results = {}
        for uuid, route in yaramo_topology.routes.items():
            self.route_results[uuid] = RouteMonitorResult(route)

    def monitor_set_route(self, yaramo_route: Route):
        self.route_results[yaramo_route.uuid].was_set = True

    def monitor_free_route(self, yaramo_route: Route):
        self.route_results[yaramo_route.uuid].was_freed = True

    def monitor_reset_route(self, yaramo_route: Route):
        self.route_results[yaramo_route.uuid].was_reset = True

    def print_evaluation(self):
        for uuid, route_monitor_result in self.route_results.items():
            route_monitor_result.print_evaluation()
