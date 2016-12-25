#!/usr/bin/env python
import scipy.io
import json
import os
import glob

in_out_path = 'dataset/UCF_CC_50'

ann_file_names = glob.glob(os.path.join(in_out_path, '*_ann.mat'))
for  ann_file_name in ann_file_names:
    j_data = map(lambda pt: {'x': pt[0], 'y': pt[1]}, scipy.io.loadmat(ann_file_name)['annPoints'])
    out_j_file_name = ann_file_name.replace('_ann.mat', '.json')
    with open(out_j_file_name, 'w') as out_j_file:
        json.dump(j_data, out_j_file)
        print ann_file_name, '->', out_j_file_name
