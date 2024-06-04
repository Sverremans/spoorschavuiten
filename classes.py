class Station:
    # FIXME: type hints
    def __init__(self, name: str, x: float, y: float) -> None:
        self._name = name
        self._connections = {}
        self._x = x
        self._y = y

    def add_connection(self, station: str, dist: int) -> None:
        self._connections[station] = dist