class Note:
    def __init__(self, name: str, duration: float, freq: float) -> None:
        self.name = name
        self.duration = duration
        self.freq = freq
    

    def __ne__(self, other: object) -> bool:
        if not isinstance(other, Note):
            raise TypeError("Операнд справа должен иметь тип Note!")
        return self.name != other.name or self.duration != other.duration or self.freq != other.freq
