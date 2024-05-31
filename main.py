from dataset_service import geo_service
from dataset_service import map_point


gs = geo_service.GeoService(map_point.MapPoint(1,1,"asdf","adfs"))
gs.add_point(map_point.MapPoint(2,2, "test", "test"), marker_type="dot")
gs.save_to_file()