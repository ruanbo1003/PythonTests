
import jieba

# str = "美高梅"
str = "腾讯控股有限公司"
# str = "美高梅中国控股有限公司"
# str = "业绩会"

for s in jieba.cut_for_search(str):
    print(s)

print('cur_all:True')
for s in jieba.cut(str, cut_all=True):
    print(s)

print('cur_all:False')
for s in jieba.cut(str, cut_all=False):
    print(s)

L = jieba.cut(str, cut_all=False)
