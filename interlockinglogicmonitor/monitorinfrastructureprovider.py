from interlocking import InfrastructureProvider
from yaramo.model import Topology
from .model import PointMonitorResult, SignalMonitorResult


class MonitorInfrastructureProvider(InfrastructureProvider):

    def __init__(self, yaramo_topology: Topology):
        super().__init__()
        self.yaramo_topology = yaramo_topology
        self.point_results = {}
        for uuid, node in yaramo_topology.nodes.items():
            # if node.is_point(): TODO: Only for points
            self.point_results[uuid] = PointMonitorResult(node)
        self.signal_results = {}
        for uuid, signal in yaramo_topology.signals.items():
            self.signal_results[uuid] = SignalMonitorResult(signal)

    async def turn_point(self, yaramo_point, target_orientation: str):
        # if node.is_point(): TODO: Only for points
        if target_orientation == "left":
            self.point_results[yaramo_point.uuid].was_turned_left = True
        if target_orientation == "right":
            self.point_results[yaramo_point.uuid].was_turned_right = True

    async def set_signal_state(self, yaramo_signal, target_state):
        if target_state == "go":
            self.signal_results[yaramo_signal.uuid].was_set_go = True
        if target_state == "halt":
            self.signal_results[yaramo_signal.uuid].was_set_halt = True