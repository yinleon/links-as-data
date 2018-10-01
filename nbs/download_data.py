"""
After changing your working directory in `config.py`, run this IE python setup.py
"""

import os
import tarfile
from tqdm import tqdm
import s3
import config

local_f = os.path.join(config.RAW_TWEETS_DIRECTORY, 
                       os.path.basename(config.RAW_TWEETS_S3))

print("downloading raw tweets...")
if not os.path.exists(local_f):
    s3.wget(config.RAW_TWEETS_S3, local_f)
    print("Untarring the raw tweets...")
    tar = tarfile.open(local_f, "r:bz2")  
    tar.extractall(config.RAW_TWEETS_DIRECTORY)
    tar.close()
else:
    print("Already loaded and expanded here {}".format(config.RAW_TWEETS_DIRECTORY))

s3_files = s3.ls(os.path.join(config.INTERMEDIATE_S3, '*'))
print("Downloading intermediate files...")
for f in tqdm(s3_files):
    local_f = os.path.join(config.INTERMEDIATE_DIRECTORY, 
                           os.path.basename(f))
    if not os.path.exists(local_f):
        s3.wget(f, local_f)
        
s3_files = s3.ls(os.path.join(config.CONGRESS_METADATA_S3 , '*.csv'))
for f in tqdm(s3_files):
    local_f = os.path.join(config.CONGRESS_METADATA_DIRECTORY , 
                           os.path.basename(f))
    if not os.path.exists(local_f):
        s3.wget(f, local_f)
    
    
    
    
    