class Station:
    def __init__(self, name: str, x: float, y: float) -> None:
        self._name = name
        self._x = x
        self._y = y

    def __repr__(self):
        return self._name
    

class Connection:
    def __init__(self, stationA: str, stationB: str, dist: int) -> None:
        self._stationA = stationA
        self._stationB = stationB
        self._dist = dist