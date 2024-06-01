# DSC_PJAIT_2024

We advise to use precompiled clients in 
./bin folder, however if you want to compile
source code by yourself, follow instructions below:

# Linux instalation

You must have `pip, python, c++, g++`

Additionaly if you want to contribute to
changes of client or server written,
you must install boost:
`sudo apt-get install libboost-all-dev
`

## Compilation example
To compile server or client, run these commands:
```bash
g++ -o client client.cpp -lboost_system -lpthread
g++ -o server server.cpp -lboost_system -lpthread
```

## To recieve dataset from server run in the root of project directory:
```
./bin/{your_os}/client ./absolut/path/to/file/file_to_save.csv
```

### MACOS WARNING
it is tested on macos and we encountered few problems
if you install boost library using brew, it will endup 
being relocated for some reason on /usr/* and your 
compiler will not find it
So you will need to use brew info boost to find presize 
location and specificaly link it using -I
If you have any problems, reachout to nikborsh.ufo@gmail.com
Additional warning is that on m1 you might need to compile 
like this :
```
g++ -std=c++17 -o client client.cpp -I/opt/homebrew/Cellar/boost/1.85.0/include -L/opt/homebrew/Cellar/boost/1.85.0/lib -lboost_system -lpthread
```

## To run your own server, compile your version of server.cpp
## and run in the root of project directory:
```
./bin/{your_os}/server
```

# Windows instalation 

If you want to avoid downloading VSCode and other heavy stuff for C++: download MSYS64
You will need to install using pacman c++ 
next using pacman you will need install boost
https://sajidifti.medium.com/how-to-install-gcc-and-gdb-on-windows-using-msys2-tutorial-0fceb7e66454
https://stackoverflow.com/questions/68913457/how-do-i-compile-c-code-with-boost-on-msys2

To compile client from source code, you can run:
```
g++ -o client client.cpp -lboost_system-mt -lws2_32
```

# Services description

## DatasetService
Deprecated service that we used to retrieve dataset using API
we replaced this service with c++ written client that fetch
data from our server with our server software written in c++ 
eventually it speeds up to +-6 minutes for retrieving whole 
dataset instead of 1 hour+ using API (1*10^6 rows per +-20 mins)
Example of usage: 
```python
DATASET_ID = "qgea-i56i"
API_URL = f"https://data.cityofnewyork.us/resource/{DATASET_ID}.csv"

ds = DatasetService(API_URL)

async def main():
    await ds.fetch_all_and_apply([
        ds.log_iterations,
        ds.log_size
    ], './../data/dataset.csv')

asyncio.run(main())
```

## GeoService
Service for working with maps
We use it for rendering crimes on the map with interactivity 
additional included components are: tooltips, labels, pins etc. 
Example of usage: 

```python
from map_point import MapPoint
map_focus_point = MapPoint(
    45,                      # X center
    -121,                    # Y center
    "some_test_crimes",      # will be used for file name when you will render map to html
    "map representing..."    # not yet used when passed as a central point
)
gs = GeoService(map_focus_point)

gs.add_points([
    MapPoint(45.3288, -121.6625, "test point 1", "some description 1"),
]).add_trailed_points([
    MapPoint(45.3311, -121.7113, "test point 2", "some description 2"),
    MapPoint(45.4500, -121.600, "test point 3", "some connection"),
    MapPoint(45.4000, -121.6600, "test point 4", "some connection")
], "connected crimes").save_to_file()

# P.S.: instead of .save_to_file() you can use .get_map() to render it directly in Jupiter
```

# NycBoroughService
service that we use to populate data in dataset
where borough name is not available, there will be 
always available latitude or longitude, that we will 
use to identify borough
Example:
```python
print(NycBoroughService.get_borough_by_xy(40.5790, -74.1590))
```
Will return one of boroughs that match by location most closely:
```
POINT: Staten Island (x:40.5795, y: -74.1592)
```