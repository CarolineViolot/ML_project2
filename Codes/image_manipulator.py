#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 18:11:06 2018

@author: jean
"""

from PIL import Image
import numpy as np
import os

def image_transformations(img_name,lab_name,angles):
    
    operations= [ Image.FLIP_LEFT_RIGHT , Image.FLIP_TOP_BOTTOM , Image.TRANSPOSE ]
    extensions= [ "_flr" , "_ftb" , "_t" ]
    
    image=Image.open(img_name)
    label=Image.open(lab_name)
    
    save_img_path=os.path.splitext(img_name)[0]
    save_lab_path=os.path.splitext(lab_name)[0]

    
    for op,ext in zip(operations,extensions):
        
        image_=image.transpose(op)
        image_.save(save_img_path+ext+".png")
        
        label_=label.transpose(op)
        label_.save(save_lab_path+ext+".png")

    
    
    width,height=image.size
    box_=(int(width/2),int(height/2),int(3*width/2),int(3*height/2))
    
    for angle in angles:
        
        image_=image.resize((int(np.sqrt(2)*width),int(np.sqrt(2)*height)),Image.BILINEAR)
        image_=image_.rotate(angle,expand=True)
        image_=image_.crop(box=box_)
    
        label_=label.resize((int(np.sqrt(2)*width),int(np.sqrt(2)*height)),Image.BILINEAR)
        label_=label_.rotate(angle,expand=True)
        label_=label_.crop(box=box_)
    
        image_.save(save_img_path+"_rot"+str(angle)+".png")
        
        label_.save(save_lab_path+"_rot"+str(angle)+".png")


