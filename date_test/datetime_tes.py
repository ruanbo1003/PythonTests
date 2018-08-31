
import datetime
import time

from django.contrib.humanize.templatetags import humanize

if __name__ == "__main__":
    print(humanize.naturalday(datetime.datetime.fromtimestamp(int(time.time()))))

    pass

