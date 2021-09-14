import re,sys,os,csv

"""
脚本使用格式：
python3 xx.py pattern file_name
"""
script_name = sys.argv[0]
pattern = sys.argv[1]
title = pattern.split('=')[0]
file_name = sys.argv[2]
file = file_name.split('.')[0]
result_file = file + "_result.csv" #结果文件名

# base_path = os.path.dirname(os.path.abspath(__file__))
r = re.compile(pattern)


with open(result_file,'w',newline='') as csv_f:
    w = csv.writer(csv_f)
    w.writerow([title])
    with open(file_name,'r') as f:
        for line in f:
            if r.search(line):
                w.writerow([r.search(line).group().split('=')[-1]])
