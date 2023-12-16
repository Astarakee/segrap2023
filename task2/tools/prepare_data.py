import os
from .sitk_stuff import read_nifti
from .writer import write_nifti_from_vol
from .preprocess import windowing_intensity
from .paths_dirs_stuff import path_contents_pattern, create_path


def main_prepare(main_in, main_out):
    main_ct_in = os.path.join(main_in, 'head-neck-ct')
    main_ct_enh_in = os.path.join(main_in, 'head-neck-contrast-enhanced-ct')
    model_in = os.path.join(main_in, 'model_in')
    model_out1 = os.path.join(main_out, 'seg_cropped_int')
    model_out2 = os.path.join(main_out, 'seg_fullres_int')
    model_out3 = os.path.join(main_out, 'seg_fullres_separate')
    create_path(model_in)
    create_path(model_out1)
    create_path(model_out2)
    create_path(model_out3)
       
    ct_files = path_contents_pattern(main_ct_in, '.mha')
    ct_enh_files = path_contents_pattern(main_ct_enh_in, '.mha')
    
    n_subject = len(ct_enh_files)
    
    for ixx in range(n_subject):
        
        print('preprocessing in progress for subject {} out of {}'.format(ixx+1, n_subject))
        
        ct_subject = ct_files[ixx]
        ct_enh_subject = ct_enh_files[ixx]
        
        subject_name = ct_subject.split('.mha')[0]
        
        ch1_name = subject_name+'_0000.nii.gz'
        ch2_name = subject_name+'_0001.nii.gz'
        
        src_ch1 = os.path.join(main_ct_enh_in, ct_enh_subject)
        src_ch2 = os.path.join(main_ct_in, ct_subject)
        
        dst_ch1 = os.path.join(model_in, ch1_name)
        dst_ch2 = os.path.join(model_in, ch2_name)
        
        img_array1, img_itk1, _, img_spacing1, img_origin1, img_direction1 = read_nifti(src_ch1)
        img_array2, _, _, _, _, _ = read_nifti(src_ch2)    
        
        arr_enh_ch1 = windowing_intensity(img_array1, -1000, 1000)
        arr_ch2 = windowing_intensity(img_array2, -600, 600)
        
        write_nifti_from_vol(arr_enh_ch1, img_origin1, img_spacing1, img_direction1, dst_ch1)
        write_nifti_from_vol(arr_ch2, img_origin1, img_spacing1, img_direction1, dst_ch2)
        
    return None
