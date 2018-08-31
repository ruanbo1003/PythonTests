import datetime

import humanize
import time

start_day = datetime.datetime.fromtimestamp(time.time() - 3600)
print(humanize.naturaltime(start_day))
print(start_day)


if __name__ == "__main__":
    print(humanize.naturalday(datetime.datetime.now() + datetime.timedelta(seconds=3600*24)))

    print(humanize.naturalday(1516446617))

