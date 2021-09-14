import re,csv

if __name__ == '__main__':
    while True:
        try:
            pattern = input('请输入要查询的正则表达式：')
            title = pattern.split('=')[0]
            file_name = input('请输入当前路径需要筛选的文件：')
            file = file_name.split('.')[0]
            result_file = input('请输入筛选后的文件名：')   #如果不输入会自动生成一个**_result.csv的文件
            if result_file == '':
                result_file = file + "_result.csv"  # 结果文件名
            r = re.compile(pattern)

        except Exception as e:
            print('error:',e)

        else:
            with open(result_file,'w',newline='') as csv_f:
                w = csv.writer(csv_f)
                w.writerow([title])
                with open(file_name,'r') as f:
                    for line in f:
                        if r.search(line):
                            w.writerow([r.search(line).group().split('=')[-1]])

            choice = input('还需要继续筛选文件吗？(y/n)：')
            if choice == 'n' or choice == 'N':
                print('\n')
                break
            else:
                continue

    input('输入Enter推出程序...')
