import folium
from dataset_service.map_point import MapPoint
import os

class GeoService:
    current_points = []
    
    def __init__(self, map_location: MapPoint):
        self.map_location = map_location
        self.current_map_name = map_location.label
        self.current_map = folium.Map(location=(
            map_location.x, 
            map_location.y
        ))
        
    def add_point(self, point: MapPoint, marker_type='pin', color='blue'):
        self.current_points.append(point)
        
        if marker_type == 'dot':
            return folium.CircleMarker(
                location=[point.x, point.y],
                radius=5,
                color=color,
                fill=True,
                fill_color=color,
                tooltip=point.label,
                popup=point.content,
            ).add_to(self.current_map)
        else:
            return folium.Marker(
                location=[point.x, point.y],
                tooltip=point.label,
                popup=point.content,
                icon=folium.Icon(icon="cloud"),
            ).add_to(self.current_map)
    
    def add_points(self, points, marker_type='pin'):
        for point in points:
            self.add_point(point, marker_type)

        return self
    
    def add_trailed_points(self, points,  trail_name: str, marker_type='pin'):
        trails = []
        for point in points:
            self.add_point(point, marker_type)
            trails.append((point.x, point.y))

        folium.PolyLine(trails, tooltip=trail_name).add_to(self.current_map)
        return self
    
    def save_to_file(self):
        current_dir = os.getcwd()
        output_path = os.path.join(current_dir, 'tmp', f'{self.current_map_name}.html')
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        self.current_map.save(output_path)
        return
        
    def get_map(self):
        return self.current_map
    
    def get_points(self):
        return self.current_points