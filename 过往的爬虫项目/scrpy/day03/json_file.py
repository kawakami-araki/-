# import json
# list_1 = []
# with open('./001.json', 'w', encoding='utf-8') as f:
#     for i in range(100):
#         list_1.append({'name':'我是%d'% i,'age': 66})
#         f.write(json.dumps(list_1,ensure_ascii=False,indent=4))

import csv

with open('data.csv', 'w', encoding='utf-8') as csvf:
    # 构建csv文件基础属性,内容的分隔符
    writer = csv.writer(csvf,delimiter = ',')
    # 写入文件,传入的参数是一个列表
    writer.writerow(['title', 'comment', 'good', 'bad'])

with open('data.csv', 'a', encoding='utf-8') as csvf:
    # 构建csv文件基础属性,内容的分隔符
    writer = csv.writer(csvf,delimiter = ',')
    # 写入文件,传入的参数是一个列表,
    writer.writerow(['title', 'comment', 'good', 'bad'])