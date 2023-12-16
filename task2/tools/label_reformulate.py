import os
import numpy as np
import SimpleITK as sitk
from copy import deepcopy
from .sitk_stuff import read_nifti
from .paths_dirs_stuff import path_contents_pattern, create_path


def main_reformat(main_out):
    seg_in = os.path.join(main_out, 'seg_fullres_int')
    nii_out = os.path.join(main_out, 'seg_fullres_separate')
    mha_out = os.path.join(main_out, 'gross-tumor-volume-segmentation')
    create_path(mha_out)
    seg_files = path_contents_pattern(seg_in, '.nii.gz')
    n_files = len(seg_files)
    
    
    oars_mapping_dict = {
            0: 'GTVp',
            1: 'GTVnd'}
    
    segrap_subset = {
        'GTVp': 1,
        "GTVnd": 2}
    
    for ix, item in enumerate(seg_files):
        print('label reformulation in progress for subject {} out {}'.format(ix+1,n_files))
        src_path = os.path.join(seg_in, item)
        subject_name = item.split('.nii.gz')[0]
        dst_path_mha = os.path.join(mha_out, subject_name+'.mha')
        subject_folder_nii = os.path.join(nii_out, subject_name)
        create_path(subject_folder_nii)
        
        seg_array, seg_itk, _, seg_spacing, seg_origin, seg_direction = read_nifti(src_path)

        stacked = []
        for keys, values in oars_mapping_dict.items():
            
            old_labels = segrap_subset[values]
            temp_mask = deepcopy(seg_array)
            if type(old_labels) == list:
                for sub_label in old_labels:
                    sub_label_idx = np.where(temp_mask==sub_label)
                    temp_mask[sub_label_idx] = 200
                temp_mask[temp_mask!=200] = 0
                temp_mask[temp_mask==200] = 1
                
            else:
                sub_label_idx = np.where(temp_mask==old_labels)
                temp_mask[sub_label_idx] = 200
                temp_mask[temp_mask!=200] = 0
                temp_mask[temp_mask==200] = 1
            
            temp_itk = sitk.GetImageFromArray(temp_mask, isVector=False)
            temp_itk.SetSpacing(seg_spacing)
            temp_itk.SetOrigin(seg_origin)
            temp_itk.SetDirection(seg_direction)
            dst_path_nii = os.path.join(subject_folder_nii, values+'.nii.gz')
            sitk.WriteImage(temp_itk, dst_path_nii)
            
            stacked.append(temp_itk)
            output_itk = sitk.JoinSeries(stacked)         
            
        sitk.WriteImage(output_itk, dst_path_mha, True)
        
    return None
