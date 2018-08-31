
import jieba
import time

str = "广东省广州市中信大厦"

begin_time = int(time.time() * 1000)


segs = jieba.cut_for_search(str)
for s in segs:
    print(s)

time1 = int(time.time() * 1000)
print(time1 - begin_time)


str2 = "广东省深圳市南山区软件园"
segs = jieba.cut_for_search(str2)
for s in segs:
    print(s)

time2 = int(time.time() * 1000)
print(time2 - time1)
