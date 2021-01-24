import keyboard

from mss.windows import MSS as mss
import mss.windows as mssw

RESOLUTION = 128

monitor = {"top": 428, "left": 848, "width": RESOLUTION, "height": RESOLUTION}
output = "sct-{top}x{left}_{width}x{height}.png".format(**monitor)

