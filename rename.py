import os
import re
import argparse

parser = argparse.ArgumentParser(description='Batch rename the entire items in TV series folder.')
parser.add_argument('-n', '--name', required=True)
parser.add_argument('-s', '--source', required=True)
args = parser.parse_args()
for filename in os.listdir(args.source):
    x = re.search("[sS]([0-9][0-9]).*[eE]([0-9][0-9])", filename)
    if x:
        y = re.search(r'(.+)\.(.*)', filename)
        z = args.name + ' - ' + 'S' + x.group(1) + 'E' + x.group(2) + '.' + y.group(2)
        os.rename(args.source+'\\'+filename, args.source+'\\'+z)