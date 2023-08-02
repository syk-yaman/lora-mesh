
# Copyright (c) 2020, Pycom Limited.
#
# This software is licensed under the GNU GPL version 3 or any
# later version, with permitted additional terms. For more information
# see the Pycom Licence v1.0 document supplied with this file, or
# available at https://www.pycom.io/opensource/licensing

try:
    from pymesh_debug import print_debug
except:
    from _pymesh_debug import print_debug
    
import time
# from pytrack import Pytrack
# from L76GNSS import L76GNSS
from machine import Timer

__version__ = '1'
"""
* initial version
"""

class Gps:
    # Pycom office GPS coordinates
    lat = 51.45
    lon = 5.45313

    l76 = None
    _timer = None
    #is_set = False
    
    @staticmethod
    def set_location(latitude, longitude):
        dlat = str(type(latitude))
        dlon = str(type(longitude))
        if dlat == dlon == "<class 'float'>":
            Gps.lat = latitude
            Gps.lon = longitude            
            is_set = True
        else:
            print_debug(3, "Error parsing ", latitude, longitude)

    @staticmethod
    def get_location():
        return (Gps.lat, Gps.lon)

    # @staticmethod
    # def init_static():
    #     is_pytrack = True
    #     try:
    #         py = Pytrack()
    #         Gps.l76 = L76GNSS(py, timeout=30)
    #         #l76.coordinates()
    #         Gps._timer = Timer.Alarm(Gps.gps_periodic, 30, periodic=True)
    #         print_debug(3, "Pytrack detected")
    #     except:
    #         is_pytrack = False
    #         print_debug(3, "Pytrack NOT detected")
    #     #TODO: how to check if GPS is conencted
    #     return is_pytrack

    # @staticmethod
    # def gps_periodic(alarm):
    #     t0 = time.ticks_ms()
    #     coord = Gps.l76.coordinates()
    #     if coord[0] != None:
    #         Gps.lat, Gps.lon = coord
    #         print_debug(3, "New coord ", coord)
    #     dt = time.ticks_ms() - t0
    #     print_debug(3, " =====>>>> gps_periodic ", dt)

    # @staticmethod
    # def terminate():
    #     if Gps._timer is not None:
    #         Gps._timer.cancel()
    #     pass

"""
from pytrack import Pytrack
from L76GNSS import L76GNSS
py = Pytrack()
l76 = L76GNSS(py, timeout=30)
t0 = time.ticks_ms()
l76.coordinates()
y = time.ticks_ms() - t0
y
"""
