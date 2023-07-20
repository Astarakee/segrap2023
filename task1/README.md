# SegRap2023 OAR segmentation

basic info:
The challenge aims to auto-segmenting the OARs from head-neck region
by employing coregistered CT and ContrastCT volumes.

They provided .nii.gz files of 120 subjects with 45 OAR labels.
After a while, they upgraded the label list to 54 but the final goal
is to predict the 45 OARs (merging some overlapping regions from 54 to 45).


## Conducted processing steps:

    1 - Intensity clipping applied to the volumes to increase the contrast.
    The intensity of the enhanced volumes were clipped in the range of [-400,2000]
    and the normal CT were clipped in the range of [-300, 800].
    
    2 - All volumes were cropped around the target regions bcs the size of the 
    original volume is super large. In the validation phase, however, the 
    organizer provides the cropped volumes, so this steps is excluded from the
    pipeline.
    
    3 - nnUnetV1_NoMirror training was employed for segmenting 54 OARs
    to preserve the symmetrical properties of symmetric structures.
    
    4 - The segmentation masks were postprossed tp create 45 OARs from
    54 labels.
    
    5 - In the validation phase, organizers decided to provide the data in 
    ".mha" format. So from the very beginning, the images were reformated
    into ".nii.gz" before intensity clipping.
    
    6 - In the validation phase, orhanizers decided to accept the segmentation
    masks in ".mha" format with the size of [45,...] which essentially is a 
    4D binary tensor in which each layer stands for one binary structure.

## code structure:
   
The structure of the code is in line with the above-described steps and follow
the instruction (in, out paths) provided by the organizer:
https://github.com/HiLab-git/SegRap2023 

    0 - According to their instruction the input and outputs are:
    `/input/images/head-neck-ct/` for normal CT and `/input/images/head-neck-contrast-enhanced-ct/`
    for contrast CT. The output dir is `/output/images/head-neck-segmentation/` as well.
    
    1 - `main.py` take two argumens for input and output dir like `~/Downloads/test_segRap/input/` and  `~/Downloads/test_segRap/output/`
    
    This code contains the following scripts:
    `main_prepare(path_in,path_out)` to convert ".mha" into ".nii.gz" followed by intensity clipping and renaming into nnUnet structure.
    
    Then:
    `os.system('nnUNet_predict -i %s -o %s -t 606 -m 3d_fullres -tr nnUNetTrainerV2_noMirroring --disable_tta' % (nnunet_in, nnunet_out))`
    to predict 54 labels and save the masks.
    
    Finally:
    `main_reformat(save_path_out)` 
    to convert the output of nnUnet into 4D .mha tensors.
    
    
## Requirements:
    The whole scripts is compatible with nnUnet requirements.
    
## Additional notes:
    In the 'Docker' branch I added another script to download the model
    checkpoint from GoogleDrive.
    `weight_dl.py`

        
