from dataset_service import map_point
# CONSTANTS SPECIFICATION
#
# Configure dataset loading
CHUNK_SIZE = 10_000
DATASET_PATH = "data/NYPD_Complaint_Data_Historic_20240528.csv"
DATE_FORMAT = '%H:%M:%S'
# Configure data convertion errors behaviour
# To set NaN when there is any error during convertion:
ERROR_HANDLING_STRATEGY = 'coerce'
# System needed
SECONDS_IN_AN_HOUR = 3600.0
THRESHOLD_HOURS=24
# Dataset specific
VALID_AGE_GROUPS = ['<18', '18-24', '25-44', '45-64', '65+', 'UNKNOWN']
NYC_CENTER_POINT = map_point.MapPoint(40.7128, -74.0060, "NYC", "Center of New York City")
STR_NULL = '(null)'
UNKNOWN = 'UNKNOWN'
# Visualisation variables
MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']