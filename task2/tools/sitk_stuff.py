import SimpleITK as itk



def read_nifti(image_path):
    """
    loading the data array and some of the metadata of nifti a nifti file.
    note that itk loads volumes as channel first.
    
    Parameters
    ----------
    image_path : string
        absolute path to the image file.
        
    Returns
    -------
    img_array : numpy array
        tensor array of the image data.
    img_itk : itk image
        loaded itk image.
    img_size : tuple
        image data dimension.
    img_spacing : tuple
        voxel spacing.
    img_origin : tuple
        subject coordinates.
    img_direction : tuple
        orientation of the acquired image.
    """
    
    img_itk = itk.ReadImage(image_path)
    img_size = img_itk.GetSize()
    img_spacing = img_itk.GetSpacing() 
    img_origin = img_itk.GetOrigin()
    img_direction = img_itk.GetDirection()
    img_array = itk.GetArrayFromImage(img_itk)
    
    return img_array, img_itk, img_size, img_spacing, img_origin, img_direction


def read_dicom_series(subject_path):
    """
    loading the data array and some of the metadata of a DICOMsery directory.

    Parameters
    ----------
    subject_path : string
        absolute path to the subject directory.

    Returns
    -------
    img_array : numpy array
        tensor array of the image data.
    img_itk : itk image
        loaded itk image.
    img_size : tuple
        image data dimension.
    img_spacing : tuple
        voxel spacing.
    img_origin : tuple
        subject coordinates.
    img_direction : tuple
        orientation of the acquired image.

    """
    reader = itk.ImageSeriesReader()
    dicom_names = reader.GetGDCMSeriesFileNames(subject_path)
    reader.SetFileNames(dicom_names)
    img_itk = reader.Execute()
    img_size = img_itk.GetSize()
    img_spacing = img_itk.GetSpacing()
    img_origin = img_itk.GetOrigin()
    img_direction = img_itk.GetDirection()
    img_array = itk.GetArrayFromImage(img_itk)
        
    return img_array, img_itk, img_size, img_spacing, img_origin, img_direction


def reorient_itk(itk_img):
    '''
    reorient the already loaded itk image into LPS cosine matrix.
    
    Parameters
    ----------
    itk_img : loaded itk image (not volume array)
    Returns
    -------
    reoriented files :array, itk_img, spacing, origin, direction.
    '''
    
    orientation_filter = itk.DICOMOrientImageFilter()
    orientation_filter.SetDesiredCoordinateOrientation("LPS")
    reoriented = orientation_filter.Execute(itk_img)
    reorient_array = itk.GetArrayFromImage(reoriented)
    reoriented_spacing = reoriented.GetSpacing()
    reoriented_origin = reoriented.GetOrigin()
    reoriented_direction = reoriented.GetDirection()
    
    return reorient_array, reoriented, reoriented_spacing, reoriented_origin, reoriented_direction