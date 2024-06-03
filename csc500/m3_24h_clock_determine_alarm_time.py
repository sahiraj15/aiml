import time
import math
from collections import namedtuple

print("This program outputs the result assuming time input in 24H format and alarm wait time in 1 hour intervals.")
tuple_alarm_set = namedtuple('tuple_alarm_set', ['current_time_hours', 'set_alarm_time_hours'])
tup_currtime_alarmtime = tuple_alarm_set(float(input("Enter current time in hours: ")), float(input("Enter the alarm wait time in hours: ")))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Data validation and raise exceptions
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if (tup_currtime_alarmtime[0] - math.trunc(tup_currtime_alarmtime[0])) > 0:
    raise "Please enter the current time in integer format only."
elif (tup_currtime_alarmtime[1] - math.trunc(tup_currtime_alarmtime[1])) > 0:
    raise "Please enter the alarm time in integer format only."
elif tup_currtime_alarmtime[0] > 23 or tup_currtime_alarmtime[0] < 0:
    raise "Invalid current time in hours, it must be in between 0-23."
elif tup_currtime_alarmtime[1] < 1:
    raise "Invalid alarm time in hours, it must be greater than 0."
else:
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Evaluate the clock time on alarm off
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    sum_of_time_in_hours = tup_currtime_alarmtime[0] + tup_currtime_alarmtime[1]
    time_on_alarm_time = sum_of_time_in_hours % 24

    print("The alarms goes off at {}:00.".format(math.trunc(time_on_alarm_time)))