#!/usr/bin/env python
# -*- coding: utf-8 -*-


import jpush as jpush
from jpush import common
import MySQLdb
import datetime

#app_key = ""
#master_secret=""

app_key = ""
master_secret=""

def push_test():
    _jpush = jpush.JPush(app_key, master_secret)
    push = _jpush.create_push()
    _jpush.set_logging("DEBUG")

    user_account = "18500000000"
    push.audience = jpush.audience(jpush.alias(user_account))

    msg = "AlphalionGroup JPush Test"
    meeting_ids = "extras information"

    android_msg = jpush.android(alert=msg, extras={'m': meeting_ids})
    ios_msg = jpush.ios(alert=msg, extras={'m': meeting_ids}, badge=1)

    push.notification = jpush.notification(alert=msg, ios=ios_msg, android=android_msg)
    push.platform = jpush.all_

    try:
        push.send()
        print('jpush test ok')
    except common.Unauthorized:
        print('jpush unauthorized')
        #raise common.Unauthorized("Unauthorized")
    except common.APIConnectionException:
        print('jpush conn error')
        #raise common.APIConnectionException("conn error")
    except common.JPushFailure:
        print('jpush failure')
        #print ("JPushFailure")
    except:
        print('jpush others exception')
        #print ("Exception")

    pass


if __name__ == '__main__':
    push_test()


