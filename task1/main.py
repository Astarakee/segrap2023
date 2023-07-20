import os
import argparse
from tools.prepare_data import main_prepare
from tools.label_reformulate import main_reformat

parser = argparse.ArgumentParser(description='SegRap2023 Challenge_taks1')
parser.add_argument('-i', type=str, help='main path to input data', required=True)
parser.add_argument('-o', type=str, help='main path to save masks', required=True)
args = parser.parse_args()

main_path_in = args.i
save_path_out = args.o

main_path_in = os.path.join(main_path_in, 'images')
save_path_out = os.path.join(save_path_out, 'images')

def main():
    main_prepare(main_path_in, save_path_out)
    nnunet_in = os.path.join(main_path_in, 'model_in')
    nnunet_out = os.path.join(save_path_out, 'seg_temp1')
    print('\n'*5)
    print('Predicting the segmentation labels begins ...')
    print('\n'*5)
    os.system('nnUNet_predict -i %s -o %s -t 606 -m 3d_fullres -tr nnUNetTrainerV2_noMirroring --disable_tta' % (nnunet_in, nnunet_out))
    print('\n'*4)
    print('Segmentation process finished successfully!')
    print('\n'*4)
    main_reformat(save_path_out)
    print('\n'*4)
    print('The pipeline was executed successfully')
    return None

if __name__ == '__main__':
    main()
