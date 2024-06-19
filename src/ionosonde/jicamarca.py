import os 
import shutil
# import base as b 
import datetime as dt
# import core as c 
from tqdm import tqdm 

def fn2dn(file):
    
    date_string = file.split('_')[1][:-4]
    fmt = '%Y%j%H%M%S'
    return dt.datetime.strptime(date_string, fmt)
    



def copy_files(path_in):
    path_out = 'database/ionogram/'
    # b.make_dir(path_out)
    
    

    for folder in os.listdir(path_in):
        
        path_folder = os.path.join(path_in, folder)
        
        for file in tqdm(os.listdir(path_folder, folder)):
            
            dn = fn2dn(file)
            
            if dn.month <= 6: 
                folder_out = 'B'
            else:
                folder_out = 'B2'
                
            src = os.path.join(path_folder, file)
            dst = os.path.join(path_out, folder_out, file)
            
            shutil.copy(src, dst)

year = 2015
path_in = f'D:\\iono\\bv\\{year}\\'

copy_files(path_in)