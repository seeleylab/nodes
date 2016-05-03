import nibabel as nib
import numpy as np
import glob
import os

node_list = glob.glob('/data/mridata/jdeng/sd_bvftd/nodes/all_nodes_2/node*')
node_list.sort()

gm = nib.load('/data/mridata/jbrown/brains/merged_ho_cereb_stn_max_bin.nii').get_data()
gm = np.where(gm.ravel() == 1)[0]

for i in node_list:
    node = nib.load(i).get_data()
    node = np.where(node.ravel() == 1)[0]
    if np.in1d(node, gm).all():
        new_index = len(glob.glob('/data/mridata/jdeng/sd_bvftd/nodes/all_nodes_in_gm/node*')) + 1
        os.rename(i, '/data/mridata/jdeng/sd_bvftd/nodes/all_nodes_in_gm/node_%s.nii' % new_index)