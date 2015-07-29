#!/usr/bin/env python3

import datetime
from dateutil.rrule import rrule, MONTHLY


def main():

    day_counter = 0
    wednesday_iso = 3
    start_date = datetime.date(1852, 1, 12)
    end_date = datetime.date(2010, 6, 18)

    for dt in rrule(MONTHLY, dtstart=start_date, until=end_date):
        if dt.isoweekday() == wednesday_iso:
            day_counter += 1

    print(day_counter)

if __name__ == "__main__":
    main()
