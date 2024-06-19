import datetime as dt 
import os 
from tqdm import tqdm 
import shutil

def fn2dn(file):
    
    date_string = file.split('_')[1][:-4]
    fmt = '%Y%j%H%M%S'
    return dt.datetime.strptime(date_string, fmt)
date = dt.date(2015, 12, 20)




def remove_data():
    
    path_folder = 'database/ionogram/B/'
    for file in tqdm(os.listdir(path_folder)):
        src = os.path.join(path_folder, file)
        target = fn2dn(file)
        if target.month > 6:
            
            dst = src.replace('B', 'B2')
            shutil.move(src, dst)
            # print(dst)
            
            # os.remove(src)

# remove_data()