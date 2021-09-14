import  re

r = re.compile(r'mcs=[0-9]{2}')
with open(r'C:\Temp\SP1427\test.txt','w') as f:
    with open(r'C:\Temp\SP1427\test.dec', 'r') as dec:
        for line in dec:
            if r.search(line):
                f.write(r.search(line).group() + '\n')