import os
os.chdir('/Users/ness001/dayoff/static')
l=os.listdir('/Users/ness001/dayoff/static')
for file in l:
    os.rename(file,file.replace(' ','_'))