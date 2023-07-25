import os
import argparse
from tools.prepare_data import main_prepare
from tools.label_reformulate import main_reformat
from tools.cropping_stuff import get_body_mask, get_bounding_box, get_cropped_volumes, crop_to_fullres

parser = argparse.ArgumentParser(description='SegRap2023 Challenge_taks2')
parser.add_argument('-i', type=str, help='main path to data with two subdirs standing for two modalities', required=True)
parser.add_argument('-o', type=str, help='main path to save masks', required=True)
args = parser.parse_args()

main_path_in = args.i
save_path_out = args.o
main_path_in = os.path.join(main_path_in, 'images')
save_path_out = os.path.join(save_path_out, 'images')


def main():
    
    body_mask_path = os.path.join(main_path_in, 'cropped_in')
    crop_log_path = os.path.join(main_path_in, 'crop_log')
    fullres_in = os.path.join(main_path_in, 'model_in')
    nnunet_in = os.path.join(main_path_in, 'nnunet_in')
    nnunet_out = os.path.join(save_path_out, 'seg_cropped_int')
    fullsize_seg_path = os.path.join(save_path_out ,'seg_fullres_int')
    
    main_prepare(main_path_in, save_path_out)
    
    print('\n'*5)
    print(' Extracting body mask begins ...')
    print('\n'*5)    
    get_body_mask(fullres_in, body_mask_path)
    
    print('\n'*5)
    print('Calculating the BBox coordinates begins ...')
    print('\n'*5)   
    get_bounding_box(body_mask_path)
    
    print('\n'*5)
    print('Extracting cropped volume process begins ...')
    print('\n'*5)    
    get_cropped_volumes(fullres_in, body_mask_path, nnunet_in, crop_log_path)
    
    print('\n'*5)
    print('Segmenting the cropped volume begins ...')
    print('\n'*5)   
    os.system('nnUNet_predict -i %s -o %s -t 609 -m 3d_fullres --disable_tta' % (nnunet_in, nnunet_out))
    
    print('\n'*5)
    print('Projecting cropped mask into full resolutional masks begins ...')
    print('\n'*5)   
    crop_to_fullres(save_path_out, crop_log_path, fullsize_seg_path)    
    
    print('\n'*4)
    print('Segmentation process finished successfully!')
    print('\n'*4)
    main_reformat(save_path_out)
    
    print('\n'*4)
    print('The pipeline was executed successfully')
    return None

if __name__ == '__main__':
    main()
