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
    

path_in = 'D:\\iono\\bv\\2014\\'
def copy_files(path_in):
    path_out = 'database/ionogram/B/'
    # b.make_dir(path_out)
    
    

    for folder in os.listdir(path_in):
        
        path_folder = os.path.join(path_in, folder)
        
        for file in tqdm(os.listdir(path_folder, folder)):
            
            dn = fn2dn(file)
            
            if ((dn.time() < dt.time(23, 50)) & 
                (dn.time() > dt.time(18, 0))): 
                
                
                src = os.path.join(path_folder, file)
                dst = os.path.join(path_out, file)
                
                shutil.copy(src, dst)
    

# copy_files(path_in)