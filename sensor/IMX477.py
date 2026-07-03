from sensor.sensor import Sensor
from sensor.bayeroffset import BayerOffset

class IMX477(Sensor):
    def __init__(self):
        super().__init__(
            'imx708',                               # Name
            4608,                                   # X Resolution
            2592,                                   # Y Resolution 
            16,                                     # Bits per pixel. Note, even though the sensor is 12bits, we're sending as 16
            2,                                      # Binning. Sensor must have a resolution equal to resolution divided by this number
            1.4,                                   # Native pixel size
            16,                                     # Max gain. Min gain is always zero
            0.00006,                                # Min exposure (secs)
            600,                                    # Max exposure (secs)
            [11.4,11.25,6.22,4.17,3.13,                   # Electrons per ADU. This should be an array of size 0 to <max gain>.                
             2.51,2.09,1.8,1.58,1.38,                   # Find the e/ADU values from Sharpcap sensor analysis
             1.25,1.13,1.04,0.94,0.88,
             0.82,0.76],                            
            [11524, 11524, 6365, 4272, 3205,     # Full well capacity. This should be an array of size 0 to <max gain>.
             2575, 2143, 1843, 1614, 1411,     # Fine the full well capacity values from Sharpcap sensor analysis
             1284, 1158, 1065, 964, 904, 
             836, 782],
            'SBGGR10_CSI2P',                              # unpacked RAW format
            BayerOffset.create_instance('BGGR')     # Bayer Pattern                   
        )
