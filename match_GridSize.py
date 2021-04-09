import SimpleITK as sitk
import numpy as np

def change_sitk_shape(image1, image2):
    '''
    Resize image 2 to grid size of image1 through zero padding.

    :param image1: SimpleITK image of larger grid size as reference
    :param image2: SimpleITK image to be resized to grid size of image1
    :return:
    NewImage: SimpleITK image from image2 with grid size of image1
    '''
    # Size of image is same as CT other than the dimensions which were bigger
    new_size = [image2.GetSize()[0], image1.GetSize()[1], image2.GetSize()[2]]
    NewImage = sitk.Image(new_size, sitk.sitkFloat32)  # initialized to zero
    # Origin from image 2 for dimention 0 and 2 and from image 1 inte resized dimention.
    image1_origin = image1.GetOrigin()
    image2_origin = image2.GetOrigin()
    NewImage.SetOrigin((image2_origin[0], image1_origin[1], image2_origin[2]))
    img2_size = image2.GetSize()
    # Find grid index from origin of image 2
    xpos_physical, ypos_physical, zpos_physical = np.around(image2.GetOrigin())  # Physical position of image2
    xpos, ypos, zpos = np.array(image1.TransformPhysicalPointToContinuousIndex([xpos_physical, ypos_physical, zpos_physical])).astype(int)
    NewImage[xpos:(xpos + img2_size[0]), ypos:(ypos + img2_size[1]), :] = image2  # Paste image2 onto zero image

    return newImage

