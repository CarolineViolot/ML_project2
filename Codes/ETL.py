#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import torch
import numpy.random as rdm
import glob
from torch.utils.data import Dataset
from image_manipulator import *

class OurDataset(Dataset):
    
    def __init__(self,img_dir,lab_dir,size_img,size_lab):
        self.img_path=img_dir
        self.lab_path=lab_dir
        self.files=sorted(glob.glob(img_dir+'*.png'))
        self.labels=sorted(glob.glob(lab_dir+'*.png'))
        self.size=[size_img]
        self.size_img =size_img
        self.size_label=size_lab
        self.shuffling()

    def __len__(self):
        return len(self.files)
    
    
    def ___getitem__(self,idx):
        img=np.asarray(Image.open(self.files[idx]).resize(self.size_img))
        label=np.asarray(Image.open(self.labels[idx]).resize([self.size_lab]))
        return img,label
    
    ######## CREATION AND EXPANSION OF DATASET THROUGH SYMMETRIES AND ROTATIONS OF THE IMAGES (SATELLITE AND GROUNDTRUTH)
    def augment_dataset(self,angles=[45]):
        for img_name,lab_name in zip(self.files,self.labels):
            print(img_name)
            image_transformations(img_name,lab_name,angles)
        self.files=sorted(glob.glob(self.img_path+'*.png'))
        self.labels=sorted(glob.glob(self.lab_path+'*.png'))
        self.shuffling()
    #######
    
    ####### SHUFFLING THE DATASET (USED BEFORE SPLITTING IN CROSS-VALIDATION)
    def shuffling(self):
        indexes=np.arange(0,len(self),dtype=np.int)
        rdm.shuffle(indexes)
        self.files=[self.files[i] for i in indexes]
        self.labels=[self.labels[i] for i in indexes]