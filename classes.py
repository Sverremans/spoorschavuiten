class Station:
    # FIXME: type hints
    def __init__(self, name: str, connections: dict[str, int] , x: float, y: float):
        self._name = name
        self._connections = connections
        self._x = x
        self._y = y

if __name__ == "__main__":
    AMS = Station("Amsterdam Centraal", {"Amsterdam Sloterdijk": 6.5}, 4.900277615, 52.37888718)
    print(AMS._connections)
    # AMS._name = "Amsterdam Centraal"
    #print(AMS._name)