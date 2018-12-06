#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ETL import *

dataset=OurDataset('../training/images/','../training/groundtruth/',(400,400),(400,400))
angles=np.arange(10,360,10)
dataset.augment_dataset(angles)

#cnn=...


