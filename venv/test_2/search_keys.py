import re,sys,os,xlwt

"""
脚本使用格式：
python3 xx.py pattern file_name
"""
script_name = sys.argv[0]
pattern = sys.argv[1]
file_name = sys.argv[2]
file = file_name.split('.')[0]
result_file = file + "_result.txt" #结果文件名

# base_path = os.path.dirname(os.path.abspath(__file__))
r = re.compile(pattern)

with open(result_file,'w') as res:
    with open(file_name,'r') as f:
        for line in f:
            if r.search(line):
                res.write(r.search(line).group() + '\n')
