import os 
import shutil
from tqdm import tqdm 
import base as b 
import datetime as dt
import core as c 
import pandas as pd 


def copy_all_in_folder(infile):
    
    for folder in tqdm(os.listdir(infile)):
        
        path_out = os.path.join(infile, folder[-1])
        b.make_dir(path_out)
        path_folder = os.path.join(infile, folder)
        
        if 'B' in folder:
        
            for file in os.listdir(path_folder):
                src = os.path.join(path_folder, file)
                dst = os.path.join(path_out, file)
                
                if file.endswith('SAO'):
                    shutil.copy(src, dst)
                    
                    
def fn2dn(file):
    
    date_string = file.split('_')[1][:-4]
    fmt = '%Y%j%H%M%S'
    return dt.datetime.strptime(date_string, fmt)
    

def range_times(start):
    
    delta = dt.timedelta(hours = 14)
    end = start + delta
    
    return pd.date_range(start, end, freq = '10min')



def copy_by_time(PATH, dates, site):
    
    path_out = f'{PATH}{site}'
    
    for dn in dates:
        
        folder = dn.strftime(f'%Y%m%d{site}')
         
        path_folder = os.path.join(PATH, folder)
        
        for file in os.listdir(path_folder):
            
            src = os.path.join(path_folder, file)
            dst = os.path.join(path_out, file)
            
            # if dn == fn2dn(file):
            shutil.copy(src, dst)
                

PATH = 'database/ionogram/'

def main():
    
    dn = dt.datetime(2015, 12, 1, 18)
    dn = dt.datetime(2017, 9, 17, 20)
    
    dates = c.undisturbed_days(dn, threshold = 8)

    PATH = 'database/ionogram/'
        
    for site in ['B', 'S', 'F', 'C']:
        
        b.make_dir(f'{PATH}/{site}')
    
        # for start in tqdm(dates, site):
    
        copy_by_time(PATH, dates, site)
            
            
# main()

# dn = dt.datetime(2013, 3, 17, 20)
 
# dates = c.undisturbed_days(dn, threshold = 8)
# dates = dates[:5] 
# site = 'S'
# b.make_dir(f'{PATH}/{site}')
# copy_by_time(PATH, dates, site)