from .interlockinglogicmonitor import InterlockingLogicMonitor
from .monitorinfrastructureprovider import MonitorInfrastructureProvider
from .model import CoverageCriteria


class Evaluation(object):

    def __init__(self,
                 interlocking_logic_monitor: InterlockingLogicMonitor,
                 monitor_infrastructure_provider: MonitorInfrastructureProvider):
        self.interlocking_logic_monitor = interlocking_logic_monitor
        self.monitor_infrastructure_provider = monitor_infrastructure_provider

    def get_coverage(self, coverage_criteria: CoverageCriteria):
        if coverage_criteria == CoverageCriteria.INFRASTRUCTURE_ONLY:
            return self._get_infrastructure_coverage()
        if coverage_criteria == CoverageCriteria.ROUTES_ONLY:
            return self._get_routes_coverage()
        return (self._get_infrastructure_coverage() + self._get_routes_coverage()) / 2

    def _get_infrastructure_coverage(self):
        coverage_sum = sum(map(lambda point_result: point_result.get_coverage(),
                               self.monitor_infrastructure_provider.point_results)) + \
                       sum(map(lambda signal_result: signal_result.get_coverage(),
                               self.monitor_infrastructure_provider.signal_results))
        return coverage_sum / (len(self.monitor_infrastructure_provider.point_results) +
                               len(self.monitor_infrastructure_provider.signal_results))

    def _get_routes_coverage(self):
        coverage_sum = sum(map(lambda routes_result: routes_result.get_coverage(),
                               self.interlocking_logic_monitor.route_results))
        return coverage_sum / len(self.interlocking_logic_monitor.route_results)