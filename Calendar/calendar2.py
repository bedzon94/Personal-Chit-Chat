#!/usr/bin/env python3
import calendar

calendar.setfirstweekday(calendar.SUNDAY)
x = calendar.TextCalendar()
print(x.pryear(2022))
