# # from .. import settings
# import os
# import pandas as pd
#
# temp_files_path = '/Users/fengdong/PycharmProjects/flowpredict000/flowpredict/static/download/temp_files/'
# down_path = '/Users/fengdong/PycharmProjects/flowpredict000/flowpredict/static/download/'
# if not os.path.exists(temp_files_path):
#     os.mkdir(temp_files_path)
#
# work_id = '21dcb051-80ef-4bdb-ba20-424e9c5e1b61'
# files = os.listdir(temp_files_path)
# files_len = len(files)
# if files_len > 0:
#     if work_id in files[0]:
#         for i in range(files_len):
#
#             lines = open(os.path.join(temp_files_path, files[i])).readlines()
#             one_line = lines[0].split(',')[0] + ','
#             # print(len(lines))
#             for line in lines:
#                 city_day_flow = line.split(',')
#                 one_line = one_line + city_day_flow[1] + ':' + str(round(float(city_day_flow[2]), 2)) + ','
#             print(one_line)
#             with open(os.path.join(down_path, work_id + '.csv'), 'a+') as f:
#                 f.write(one_line + '\n')
#             os.remove(os.path.join(temp_files_path, files[i]))
