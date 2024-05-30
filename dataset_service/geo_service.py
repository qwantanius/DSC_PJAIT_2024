import folium
from map_point import MapPoint

class GeoService:
    current_points = []
    
    def __init__(self, map_location: MapPoint):
        self.map_location = map_location
        self.current_map_name = map_location.label
        self.current_map = folium.Map(location=(
            map_location.x, 
            map_location.y
        ))
        
    def add_point(self, point: MapPoint):
        self.current_points.append(point)
        
        return folium.Marker(
            location=[point.x, point.y],
            tooltip=point.label,
            popup=point.content,
            icon=folium.Icon(icon="cloud"),
        ).add_to(self.current_map)
    
    def add_points(self, points: list[MapPoint]):
        for point in points:
            self.add_point(point)

        return self
    
    def add_trailed_points(self, points: list[MapPoint], trail_name: str):
        trails = []
        for point in points:
            self.add_point(point)
            trails.append((point.x, point.y))

        folium.PolyLine(trails, tooltip=trail_name).add_to(self.current_map)
        return self
    
    def save_to_file(self):
        self.current_map.save(f"./../tmp/{self.current_map_name}.html")
        return
        
    def get_map(self):
        return self.current_map
    
    def get_points(self):
        return self.current_points
