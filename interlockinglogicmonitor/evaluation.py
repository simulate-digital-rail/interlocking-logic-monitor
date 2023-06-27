from .interlockinglogicmonitor import InterlockingLogicMonitor
from .monitorinfrastructureprovider import MonitorInfrastructureProvider
from .model import CoverageCriteria
import logging


class Evaluation(object):

    def __init__(self,
                 interlocking_logic_monitor: InterlockingLogicMonitor,
                 monitor_infrastructure_provider: MonitorInfrastructureProvider):
        self.interlocking_logic_monitor = interlocking_logic_monitor
        self.monitor_infrastructure_provider = monitor_infrastructure_provider

    def get_coverage(self, coverage_criteria: CoverageCriteria = CoverageCriteria.ALL):
        if coverage_criteria == CoverageCriteria.INFRASTRUCTURE_ONLY:
            return self._get_infrastructure_coverage()
        if coverage_criteria == CoverageCriteria.ROUTES_ONLY:
            return self._get_routes_coverage()
        return (self._get_infrastructure_coverage() + self._get_routes_coverage()) / 2

    def _get_infrastructure_coverage(self):
        point_results = self.monitor_infrastructure_provider.point_results
        signal_results = self.monitor_infrastructure_provider.signal_results
        coverage_sum = sum(map(lambda point_uuid: point_results[point_uuid].get_coverage(), point_results)) + \
                       sum(map(lambda signal_uuid: signal_results[signal_uuid].get_coverage(), signal_results))
        return coverage_sum / (len(self.monitor_infrastructure_provider.point_results) +
                               len(self.monitor_infrastructure_provider.signal_results))

    def _get_routes_coverage(self):
        route_results = self.interlocking_logic_monitor.route_results
        coverage_sum = sum(map(lambda routes_uuid: route_results[routes_uuid].get_coverage(), route_results))
        return coverage_sum / len(self.interlocking_logic_monitor.route_results)

    def print_evaluation(self):
        logging.debug("###")
        logging.debug("Monitoring Evaluation")
        self.interlocking_logic_monitor.print_evaluation()
        self.monitor_infrastructure_provider.print_evaluation()
        logging.debug(f"Total Coverage: {self.get_coverage(CoverageCriteria.ALL)}")
        logging.debug(f"Infrastructure Coverage: {self.get_coverage(CoverageCriteria.INFRASTRUCTURE_ONLY)} ")
        logging.debug(f"Routes Coverage: {self.get_coverage(CoverageCriteria.ROUTES_ONLY)}")
        logging.debug("###")

