# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 15:48:17 2020

@author: Administrator
"""


import os
import numpy as np

# Read imge file from specified directory
image_files = []
extension = ['.jpg','.png', '.jpeg']
for _dir in os.listdir(os.getcwd()):
    if os.path.isdir(_dir):
        print("Current directory: ",_dir )
        for _file in os.listdir(os.path.join(os.getcwd(), _dir)):
            if os.path.splitext(_file)[-1].lower() in extension:
                print("Current file: ",_file )
                image_files.append("traindata/" + _dir+'/'+ _file)
    
# Modify a sequence in-place by shuffling its contents.
np.random.shuffle(image_files)

# Random index for validation set
rand_idx =  np.random.randint(0, len(image_files), int(len(image_files)*0.2))
 
# Write to file .txt               
with open("custom_train.txt", "w") as f:
    for idx in np.arange(len(image_files)):
        if idx not in rand_idx:
            f.write(image_files[idx])
            f.write("\n")
    f.close()
    
# Write valid.txt
with open("custom_valid.txt", "w") as f:
    for idx in np.arange(len(image_files)):
        if idx in rand_idx:
            f.write(image_files[idx])
            f.write("\n")
    f.close()

    
    
                
    
