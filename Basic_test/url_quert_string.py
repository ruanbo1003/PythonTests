

import urllib
import urllib3
from urllib.parse import urlencode


paramters = {
    "name": "Joe",
    "job": "sde"
}

str = urlencode(paramters)
print(str)
