import os
import numpy as np
import SimpleITK as sitk
from copy import deepcopy
from .sitk_stuff import read_nifti
from .paths_dirs_stuff import path_contents_pattern, create_path


def main_reformat(main_out):
    seg_in = os.path.join(main_out, 'seg_temp1')
    nii_out = os.path.join(main_out, 'seg_temp2')
    mha_out = os.path.join(main_out, 'head-neck-segmentation')
    create_path(mha_out)
    seg_files = path_contents_pattern(seg_in, '.nii.gz')
    n_files = len(seg_files)
    
    
    oars_mapping_dict = {
            0: 'Brain',
            1: 'BrainStem',
            2: 'Chiasm',
            3: 'TemporalLobe_L',
            4: 'TemporalLobe_R',
            5: 'Hippocampus_L',
            6: 'Hippocampus_R',
            7: 'Eye_L',
            8: 'Eye_R',
            9: 'Lens_L',
            10: 'Lens_R',
            11: 'OpticNerve_L',
            12: 'OpticNerve_R',
            13: 'MiddleEar_L',
            14: 'MiddleEar_R',
            15: 'IAC_L',
            16: 'IAC_R',
            17: 'TympanicCavity_L',
            18: 'TympanicCavity_R',
            19: 'VestibulSemi_L',
            20: 'VestibulSemi_R',
            21: 'Cochlea_L',
            22: 'Cochlea_R',
            23: 'ETbone_L',
            24: 'ETbone_R',
            25: 'Pituitary',
            26: 'OralCavity',
            27: 'Mandible_L',
            28: 'Mandible_R',
            29: 'Submandibular_L',
            30: 'Submandibular_R',
            31: 'Parotid_L',
            32: 'Parotid_R',
            33: 'Mastoid_L',
            34: 'Mastoid_R',
            35: 'TMjoint_L',
            36: 'TMjoint_R',
            37: 'SpinalCord',
            38: 'Esophagus',
            39: 'Larynx',
            40: 'Larynx_Glottic',
            41: 'Larynx_Supraglot',
            42: 'PharynxConst',
            43: 'Thyroid',
            44: 'Trachea'}
    
    segrap_subset = {
        'Brain': [1, 2, 3, 4, 5, 6, 7, 8, 9],
        "BrainStem": 2,
        "Chiasm": 3,
        "TemporalLobe_L": [4, 6],
        "TemporalLobe_R": [5, 7],
        "Hippocampus_L": [8, 6],
        "Hippocampus_R": [9, 7],
        'Eye_L': [10, 12],
        'Eye_R': [11, 13],
        "Lens_L": 12,
        "Lens_R": 13,
        "OpticNerve_L": 14,
        "OpticNerve_R": 15,
        "MiddleEar_L": [18, 16, 20, 24, 28, 30],
        "MiddleEar_R": [19, 17, 21, 25, 29, 31],
        "IAC_L": 18,
        "IAC_R": 19,
        "TympanicCavity_L": [22, 20],
        "TympanicCavity_R": [23, 21],
        "VestibulSemi_L": [26, 24],
        "VestibulSemi_R": [27, 25],
        "Cochlea_L": 28,
        "Cochlea_R": 29,
        "ETbone_L": [32, 30],
        "ETbone_R": [33, 31],
        "Pituitary": 34,
        "OralCavity": 35,
        "Mandible_L": 36,
        "Mandible_R": 37,
        "Submandibular_L": 38,
        "Submandibular_R": 39,
        "Parotid_L": 40,
        "Parotid_R": 41,
        "Mastoid_L": 42,
        "Mastoid_R": 43,
        "TMjoint_L": 44,
        "TMjoint_R": 45,
        "SpinalCord": 46,
        "Esophagus": 47,
        "Larynx": [48, 49, 50, 51],
        "Larynx_Glottic": 49,
        "Larynx_Supraglot": 50,
        "PharynxConst": [51, 52],
        "Thyroid": 53,
        "Trachea": 54}
    
    for ix, item in enumerate(seg_files):
        print('label reformulation in progress for subject {} out {}'.format(ix+1,n_files))
        src_path = os.path.join(seg_in, item)
        subject_name = item.split('.nii.gz')[0]
        dst_path_mha = os.path.join(mha_out, subject_name+'.mha')
        subject_folder_nii = os.path.join(nii_out, subject_name)
        create_path(subject_folder_nii)
        #dst_path_nii = os.path.join(nii_out, subject_name+'.nii.gz')
        
        seg_array, seg_itk, _, seg_spacing, seg_origin, seg_direction = read_nifti(src_path)
        
        #dim1, dim2, dim3 = seg_array.shape
        #seg_mask_4d = np.zeros((45,dim1, dim2, dim3 ), dtype='uint8')
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
                
            temp_itk = sitk.GetImageFromArray(temp_mask)
            temp_itk.SetSpacing(seg_spacing)
            temp_itk.SetOrigin(seg_origin)
            temp_itk.SetDirection(seg_direction)
            dst_path_nii = os.path.join(subject_folder_nii, values+'.nii.gz')
            sitk.WriteImage(temp_itk, dst_path_nii)
            
            #seg_mask_4d[keys,...] = temp_mask
            stacked.append(temp_itk)
            output_itk = sitk.JoinSeries(stacked)
            
        sitk.WriteImage(output_itk, dst_path_mha)
        
    return None
