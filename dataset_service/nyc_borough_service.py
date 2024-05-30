from map_point import MapPoint

class NycBoroughService:
    areas = [
        MapPoint(40.7831, -73.9712, "Manhattan", ""),
        MapPoint(40.6782, -73.9442, "Brooklyn", ""),
        MapPoint(40.7282, -73.7949, "Queens", ""),
        MapPoint(40.8448, -73.8648, "The Bronx", ""),
        MapPoint(40.5795, -74.1592, "Staten Island", "")
    ]
    
    @staticmethod
    def get_borough_by_xy(x: float, y: float):
        smallest_diff_x = float('inf')
        smallest_diff_y = float('inf')
        closest_point = None
        
        for area in NycBoroughService.areas:
            x_diff = abs(x - area.x)
            y_diff = abs(y - area.y)
            xhit = False
            yhit = False
            
            if (x_diff < smallest_diff_x):
                smallest_diff_x = x_diff
                xhit = True
                
            if (y_diff < smallest_diff_y):
                smallest_diff_y = y_diff
                yhit = True
            
            if (xhit and yhit):
                closest_point = area
        
        return closest_point