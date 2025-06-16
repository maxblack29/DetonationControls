import nidaqmx
from nidaqmx.constants import LineGrouping
import numpy as np
import time


device_name = "cDAQ9188-169338EMod3/port0/line0:7" 

port = 'port0'
state = [False, False, False, False, False, False, False, False]

k = 0
while k < 5:
    state = np.logical_not(state)
    k = k+1
    with nidaqmx.Task() as task:
        task.do_channels.add_do_chan(device_name, line_grouping=LineGrouping.CHAN_PER_LINE)
        task.write(state)
    time.sleep(1)

#First state is [False, False, False, False, False, False, False, False]
#Second state must move to [False, True, True, False, True, True, F]