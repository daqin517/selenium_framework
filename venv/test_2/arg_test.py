import argparse

parser = argparse.ArgumentParser(description='just a description')
parser.add_argument('file')
args = parser.parse_args()
print(args.file )