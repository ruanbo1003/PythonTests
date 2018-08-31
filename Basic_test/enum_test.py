
from enum import Enum

JPushRetCode = Enum("RetCode", ("OK", "UnAuth", "ApiConnectionFail", "PushFail", "Error"))

ret = JPushRetCode.OK

print(JPushRetCode.OK)

print(ret == JPushRetCode.OK)

print(ret is JPushRetCode.OK)
