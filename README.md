# Interlocking Logic Monitor

This monitor is analysing the behaviour of an instance of the [interlocking logic](https://github.com/simulate-digital-rail/interlocking).

## Usage
To use this monitor, a monitoring infrastructure provider and an interlocking logic monitor are necessary. Both
need the yaramo topology of the interlocking logic instance.

```python
from interlockinglogicmonitor import MonitorInfrastructureProvider, InterlockingLogicMonitor, Evaluation, CoverageCriteria
from yaramo.model import Topology
topology = Topology()
mip = MonitorInfrastructureProvider(topology)
ilm = InterlockingLogicMonitor(topology)
```

The interlocking logic monitor is monitoring, which routes are set, freed or reset.
The monitoring infrastructure provider is monitoring the operations on the points and signals.

When instantiating the interlocking, both needs to be passed to the interlocking object:

```python
from interlocking.interlockinginterface import Interlocking
interlocking = Interlocking([mip], Settings(max_number_of_points_at_same_time=3), ilm)
interlocking.prepare(topology) 
```

Now the behaviour of the interlocking logic is monitored.

After operating the interlocking logic (or in between), it's possible to print the (current) evaluation results. 
Therefore, an evaluation is necessary:

```python
evaluation = Evaluation(ilm, mip)
evaluation.print_evaluation()
```

It's also possible to print the operation coverage of the interlocking logic.
The operation coverage is the percentage of operations on routes (routes coverage), points and signals (infrastructure coverage).
Examples:

* If the topology contains one point and this point was turned to left, the coverage is `0.5`. If it was turned to left and right, the coverage is `1.0`.
* If the topology contains two routes and one was being set and freed, the coverage is `0.33`, since each route can have three operations (set, free, reset) and for one route two operations were accessed.

Getting the coverage, just run:

```python
evaluation.get_coverage() # acts like evaluation.get_coverage(coverage_criteria=CoverageCriteria.ALL)
evaluation.get_coverage(coverage_criteria=CoverageCriteria.ROUTES_ONLY)
evaluation.get_coverage(coverage_criteria=CoverageCriteria.INFRASTRUCTURE_ONLY)
```

More is coming...