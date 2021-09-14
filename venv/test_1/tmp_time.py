import time

print('当前时间:',time.localtime())
print('格式化后的时间：',time.strftime('%Y-%m-%d %H:%M',time.localtime()))

print('时间戳：',time.time())

print(time.asctime())