from enum import Enum

class Service(Enum):
    WMS = 1
    WFS = 2
    WCS = 3

class Operation(Enum):
    GetMap = 1
    GetFeatureInfo = 2
    GetFeature = 3

class RetrievalMode(Enum):
    OFFSET = 1
    EXTENT = 2

class Format(Enum):
    GEORSS = 1
    KML = 2
