from enum import Enum


class CoverageCriteria(Enum):
    ALL = 0
    INFRASTRUCTURE_ONLY = 1
    ROUTES_ONLY = 2
