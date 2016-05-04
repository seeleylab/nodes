import nibabel as nib
import numpy as np
import glob
import os

node_list = glob.glob('/data/mridata/jdeng/sd_bvftd/nodes/all_nodes_2/node*')
node_list.sort()

gm = nib.load('/data/mridata/jbrown/brains/merged_ho_cereb_stn_max_bin.nii').get_data()
gm = np.where(gm.ravel() == 1)[0]

current_gm_nodes = len(glob.glob('/data/mridata/jdeng/sd_bvftd/nodes/all_nodes_in_gm_2/node*'))

for i in node_list:
    print i
    node = nib.load(i).get_data()
    node = np.where(node.ravel() == 1)[0]
    gm_voxels_in_node = len(np.where(np.in1d(node, gm) == 1)[0])
    total_voxels_in_node = len(np.in1d(node, gm))
    if (float(gm_voxels_in_node) / float(total_voxels_in_node)) >= 0.5:
        os.rename(i, '/data/mridata/jdeng/sd_bvftd/nodes/all_nodes_in_gm_2/node_%s.nii' % current_gm_nodes+1)
        current_gm_nodes += 1