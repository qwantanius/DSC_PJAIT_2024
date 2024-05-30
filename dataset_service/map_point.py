class MapPoint:    
    def __init__(self, x: float, y: float, label: str, content: str) -> None:
        self.x = x
        self.y = y
        self.label = label
        self.content = content
        
    def __str__(self) -> str:
        return f"POINT: {self.label} (x:{self.x}, y: {self.y})"